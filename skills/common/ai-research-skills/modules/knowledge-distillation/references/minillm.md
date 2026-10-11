# MiniLLM: Reverse KL Divergence for LLM Distillation

Based on arXiv 2306.08543 (2024) - MiniLLM: Knowledge Distillation of Large Language Models

## Overview

**Source**: https://arxiv.org/abs/2306.08543
**GitHub**: https://github.com/microsoft/LMOps/tree/main/minillm

MiniLLM replaces forward KLD with reverse KLD for knowledge distillation, achieving better performance on generative language models.

## Problem with Standard KLD

### Forward KL Divergence (Standard)

**Formula (forward)**: `KL(Teacher || Student)`

**Minimization behavior (forward)**: Mode-covering
```
Student penalizes missing probability mass where the teacher assigns mass.
→ Limited capacity can force probability onto undesirable regions.
→ An unconstrained optimum matches the teacher distribution.
```

**Issue for generative models**: A small student may not have capacity to cover the teacher distribution well; quality is task-dependent.

### Illustrative Distribution, Not an Optimization Result

```python
# Teacher distribution (diverse)
teacher_probs = [0.3, 0.3, 0.2, 0.1, 0.1]  # Multiple valid options

# Forward KL minimization
# An unconstrained optimum matches teacher_probs for either KL direction.
# Mode-covering/seeking behavior matters under capacity constraints.
```

## MiniLLM Solution: Reverse KLD

### Reverse KL Divergence

**Formula (reverse)**: `KL(Student || Teacher)`

**Minimization behavior (reverse)**: Mode-seeking
```
Student penalizes its own probability where teacher probability is low.
→ It may concentrate on a subset of teacher modes.
→ Better quality does not guarantee more diversity.
```

### Mathematical Formulation

**Forward KL** (standard distillation):
```
L_forward = Σ p_teacher(x) log(p_teacher(x) / p_student(x))
          = E_{x~teacher} [log p_teacher(x) - log p_student(x)]
```

**Reverse KL** (MiniLLM):
```
L_reverse = Σ p_student(x) log(p_student(x) / p_teacher(x))
          = E_{x~student} [log p_student(x) - log p_teacher(x)]
```

**Key difference**: Expectation over teacher distribution vs student distribution.

## Implementation

### Reverse KLD Loss

```python
import torch
import torch.nn.functional as F

def reverse_kl_loss(student_logits, teacher_logits, labels, temperature=1.0):
    """
    Tokenwise reverse KL: KL(Student || Teacher); not the full MiniLLM algorithm.

    Args:
        student_logits: Model predictions (batch, seq_len, vocab_size)
        teacher_logits: Teacher predictions (batch, seq_len, vocab_size)
        temperature: Softening parameter

    Returns:
        Reverse KL divergence loss
    """
    log_s = F.log_softmax(student_logits[:, :-1].float() / temperature, dim=-1)
    log_t = F.log_softmax(teacher_logits[:, :-1].detach().to(log_s.device).float() / temperature, dim=-1)
    valid = labels[:, 1:].to(log_s.device).ne(-100)
    if not valid.any():
        raise ValueError("No supervised tokens")
    return (log_s.exp() * (log_s - log_t)).sum(-1)[valid].mean() * temperature ** 2
```

### Policy Gradient Optimization

**Challenge**: Sequence-level reverse KL takes an expectation under the student.

**Solution**: Use the official MiniLLM implementation for its student-sampling policy-gradient estimator and variance reduction. The next helper is a teacher-sampled SFT baseline, not MiniLLM or a policy-gradient estimator. It assumes unpadded prompts.

```python
def teacher_sampled_sft(student_model, teacher_model, prompt_batch):
    """
    Teacher-sampled SFT baseline.

    Steps:
    1. Sample responses from teacher
    2. Mask prompt labels
    3. Optimize continuation cross-entropy
    """
    # 1. Generate from teacher (detached)
    with torch.no_grad():
        teacher_outputs = teacher_model.generate(
            prompt_batch,
            max_new_tokens=256,
            do_sample=True,
            temperature=1.0,
            return_dict_in_generate=True,
            output_scores=True
        )

        teacher_sequences = teacher_outputs.sequences
        teacher_scores = teacher_outputs.scores

    # 2. Student evaluates teacher's samples
    labels = teacher_sequences.clone()
    labels[:, :prompt_batch.shape[1]] = -100
    student_outputs = student_model(
        input_ids=teacher_sequences,
        labels=labels
    )

    # 3. Causal cross-entropy, not the mean of logits
    loss = student_outputs.loss

    return loss
```

## Training Procedure

### Two-Stage MiniLLM

**Stage 1**: Tokenwise reverse-KL demonstration (not the full paper recipe)
```python
# Learn to generate like teacher
for epoch in range(num_imitation_epochs):
    for batch in dataloader:
        # Sample from teacher
        with torch.no_grad():
            teacher_samples = teacher.generate(batch['prompts'])
            teacher_logits = teacher(teacher_samples).logits
        labels = teacher_samples.clone()
        labels[:, :batch['prompts'].shape[1]] = -100

        # Student imitates
        loss = reverse_kl_loss(
            student(teacher_samples).logits,
            teacher_logits, labels
        )

        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        optimizer.step()
```

**Stage 2**: Self-training (optional)
```python
# Fine-tune on student's own generations
for epoch in range(num_self_train_epochs):
    for batch in dataloader:
        # Student generates
        student_samples = student.generate(batch['prompts'])

        # Self-training loss
        labels = student_samples.clone()
        labels[:, :batch['prompts'].shape[1]] = -100
        loss = student(student_samples, labels=labels).loss

        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        optimizer.step()
```

### Trainer Integration Sketch

Supply a tokenized dataset and a causal data collator (see MODULE.md). Use aligned vocabularies and device placement. The 70B/7B defaults need remote multi-GPU resources (~154 GB FP16 weights alone); choose much smaller models locally. This tokenwise example is not a reproduction of MiniLLM.

```python
from transformers import AutoModelForCausalLM, Trainer, TrainingArguments

def train_minillm(
    teacher_name="meta-llama/Llama-2-70b-hf",
    student_name="meta-llama/Llama-2-7b-hf",
    output_dir="./minillm-7b",
    train_dataset=None,
    data_collator=None,
):
    # Load models
    teacher = AutoModelForCausalLM.from_pretrained(teacher_name, torch_dtype=torch.float16, device_map="auto")
    student = AutoModelForCausalLM.from_pretrained(student_name, torch_dtype=torch.float16)

    # Custom trainer with reverse KLD
    class MiniLLMTrainer(Trainer):
        def compute_loss(self, model, inputs, return_outputs=False, num_items_in_batch=None):
            # Forward both models on the same tokens; generate().scores can be
            # processed logits and have a different length from prompt+output.
            with torch.no_grad():
                teacher.eval()
                teacher_logits = teacher(**inputs).logits
            student_outputs = model(**inputs)

            student_logits = student_outputs.logits

            # Reverse KL loss
            loss = reverse_kl_loss(student_logits, teacher_logits, inputs['labels'])

            return (loss, student_outputs) if return_outputs else loss

    # Training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=5,
        per_device_train_batch_size=2,
        gradient_accumulation_steps=16,
        learning_rate=5e-5,
        warmup_steps=1000,
        logging_steps=100,
        save_steps=1000,
        bf16=True,
    )

    # Train
    trainer = MiniLLMTrainer(
        model=student,
        args=training_args,
        train_dataset=train_dataset,
        data_collator=data_collator,
    )

    trainer.train()
    student.save_pretrained(output_dir)

# Usage
train_minillm(
    teacher_name="meta-llama/Llama-2-70b-hf",
    student_name="meta-llama/Llama-2-7b-hf",
)
```

## Performance Results

**From paper (LLaMA models)**:

| Student | Teacher | Method | MT-Bench Score | AlpacaEval |
|---------|---------|--------|----------------|------------|
| LLaMA-7B | - | Baseline | 5.2 | 55% |
| LLaMA-7B | LLaMA-70B | Forward KL | 5.8 | 62% |
| LLaMA-7B | LLaMA-70B | **MiniLLM (Reverse KL)** | **6.4** | **71%** |

**Key findings**:
- Reverse KL outperforms forward KL by ~10%
- Distilled 7B model approaches 70B performance
- Better diversity and generation quality

## Comparison: Forward vs Reverse KL

### Generation Quality

```python
# Prompt: "Explain quantum computing"

# Forward KL (mode-seeking)
# Student output: "Quantum computing uses quantum bits..."
# → Safe, generic, one mode

# Reverse KL (mode-covering)
# Student output: Multiple diverse valid explanations
# → Covers different valid explanations
# → More creative, diverse
```

### When to Use Each

**Forward KL**:
- Classification tasks
- Single correct answer
- Need deterministic output

**Reverse KL (MiniLLM)**:
- Generative tasks
- Multiple valid outputs
- Need diversity
- Open-ended generation

## Hyperparameters

### Temperature

```python
# Temperature for both teacher and student

T = 1.0  # Standard (from paper)
T = 0.8  # Sharper (less diversity)
T = 1.2  # Softer (more diversity)

# Rule: Use T=1.0 for MiniLLM (higher temps help mode-covering)
```

### Learning Rate

```python
# MiniLLM uses higher LR than standard distillation

lr_forward_kl = 2e-5   # Standard distillation
lr_minillm = 5e-5      # MiniLLM (can handle higher LR)

# Reason: Reverse KL has better gradient properties
```

## Limitations

1. **Computational cost**: Requires sampling from teacher during training
2. **Implementation complexity**: More complex than standard distillation
3. **Memory**: Need to store teacher samples

## Resources

- **Paper**: https://arxiv.org/abs/2306.08543
- **GitHub**: https://github.com/microsoft/LMOps/tree/main/minillm
- **Blog**: https://www.microsoft.com/en-us/research/blog/minillm-small-language-models-via-large-language-model-distillation/
