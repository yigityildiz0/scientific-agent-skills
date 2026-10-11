# Module: constitutional-ai

> Upstream orchestra-research/AI-research-SKILLs skill; reference routes corrected by Yigit, 2026-10-05. Paths are relative to this module folder.
> Original trigger scope: Anthropic's method for training harmless AI through self-improvement. Two-phase approach - supervised learning with self-critique/revision, then RLAIF (RL from AI Feedback). Use for safety alignment, reducing harmful outputs without human labels. Powers Claude's safety system.

# Constitutional AI - Harmlessness from AI Feedback

## Quick start

Constitutional AI (CAI) trains models to be harmless through self-critique and AI feedback, without requiring human labels for harmful outputs.

**Key concept**: Models learn to critique and revise their own responses using a "constitution" (set of principles).

**Two phases**:
1. **Supervised Learning (SL)**: Self-critique + revision
2. **Reinforcement Learning (RL)**: RLAIF (RL from AI Feedback)

**Constitution example**:
```
Principles:
1. Choose the response that is most helpful, honest, and harmless
2. Avoid responses that are toxic, racist, or sexist
3. Prefer responses that explain objections rather than refuse
4. Choose responses that are thoughtful and nuanced
```

## Common workflows

### Workflow 1: Supervised learning phase (self-critique + revision)

**Step 1: Generate initial responses**:
```python
from transformers import pipeline

generator = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")

def generate_texts(texts, **kwargs):
    """One continuation per input; unwrap the pipeline's nested batch output."""
    batches = generator(texts, max_new_tokens=200, return_full_text=False, **kwargs)
    return [batch[0]["generated_text"] for batch in batches]

prompts = [
    "How do I hack a website?",
    "Write something offensive about a group.",
    "Help me cheat on my exam."
]

initial_responses = generate_texts(prompts)
```

**Step 2: Self-critique with constitution**:
```python
critique_prompt = """
Given the question:
{question}

And the response:
{response}

Constitution:
1. Choose responses that are helpful, honest, and harmless
2. Avoid toxic, racist, or sexist content
3. Explain objections rather than refuse

Identify any ways this response violates the constitution:
"""

critiques = generate_texts(
    [critique_prompt.format(question=q, response=r) for q, r in zip(prompts, initial_responses)]
)
```

**Step 3: Revision based on critique**:
```python
revision_prompt = """
Question: {question}
Original response: {response}
Critique: {critique}

Please revise the response to better align with the constitution:
"""

revised_responses = generate_texts(
    [revision_prompt.format(question=q, response=r, critique=c)
     for q, r, c in zip(prompts, initial_responses, critiques)]
)
```

**Step 4: Fine-tune on revised responses**:
```python
from datasets import Dataset
from trl import SFTConfig, SFTTrainer

# Create dataset of (prompt, revised_response) pairs
dataset = Dataset.from_dict({"prompt": prompts, "completion": revised_responses})

trainer = SFTTrainer(
    model=generator.model,
    processing_class=generator.tokenizer,
    args=SFTConfig(output_dir="constitutional-sft", max_length=1024),
    train_dataset=dataset,
)
trainer.train()
```

### Workflow 2: RL phase (RLAIF - RL from AI Feedback)

**Step 1: Generate comparison pairs**:
```python
# Sample multiple responses per prompt
responses_a = generate_texts(prompts, do_sample=True, temperature=0.8)
responses_b = generate_texts(prompts, do_sample=True, temperature=0.8)
```

**Step 2: AI preference evaluation**:
```python
preference_prompt = """
Question: {question}

Response A: {response_a}
Response B: {response_b}

Constitution:
{constitution}

Which response better follows the constitution? Explain your reasoning, then choose A or B.
"""

CONSTITUTION = "Prefer helpful, honest responses that avoid enabling harm."
preferences = generate_texts(
    [preference_prompt.format(question=q, response_a=ra, response_b=rb, constitution=CONSTITUTION)
     for q, ra, rb in zip(prompts, responses_a, responses_b)]
)

# Parse preferences (A or B)
chosen, rejected = parse_preferences(preferences, responses_a, responses_b)
```

**Step 3: Train preference model (reward model)**:
```python
from trl import RewardTrainer, RewardConfig

preference_dataset = create_preference_dataset(prompts, chosen, rejected)

reward_config = RewardConfig(
    output_dir="constitutional-reward-model",
    learning_rate=1e-5,
    num_train_epochs=1
)

reward_trainer = RewardTrainer(
    model=model,
    args=reward_config,
    train_dataset=preference_dataset,
    processing_class=tokenizer
)
reward_trainer.train()
```

**Step 4: RL training with RLAIF**:
```text
Illustrative PPO wiring (not a callable TRL API):
load policy from the SFT checkpoint
load a frozen reference policy and the trained scalar reward model
initialize the value model and tokenized prompt dataset
configure PPO, KL control, rollout/evaluation budgets for the installed TRL version
train policy using reward scores, with held-out human-reviewed evaluations
```

TRL PPO APIs have changed across releases; follow the installed release's PPO
example rather than invented `reward_model_path` constructor arguments. Earlier
steps' `parse_preferences` and `create_preference_dataset` are application hooks:
validate A/B labels, reject ambiguous outputs, randomize order, and build the
documented reward-dataset schema with a scalar sequence-classification model.

### Workflow 3: Chain-of-thought critique

**Enable reasoning transparency**:
```python
cot_critique_prompt = """
Question: {question}
Response: {response}

Let's think step-by-step about whether this response follows our principles:

1. Is it helpful? [Yes/No and reasoning]
2. Is it honest? [Yes/No and reasoning]
3. Is it harmless? [Yes/No and reasoning]
4. Does it avoid toxicity? [Yes/No and reasoning]

Based on this analysis, suggest a revision if needed.
"""

cot_critiques = generator(
    [cot_critique_prompt.format(q=q, r=r) for q, r in zip(prompts, responses)]
)
```

## When to use vs alternatives

**Use Constitutional AI when**:
- Want safety alignment without human labels
- Need explainable AI decisions
- Want to avoid evasive refusals
- Have a clear set of principles/constitution
- Need scalable safety training

**Principles**:
- **RLAIF**: AI-generated preferences (scalable, no human labels)
- **RLHF**: Human preferences (more accurate, expensive)
- **Self-critique**: Iterative improvement
- **Chain-of-thought**: Reasoning transparency

**Use alternatives instead**:
- **RLHF (PPO)**: Need human-validated safety
- **DPO/SimPO**: Have human preference data
- **NeMo Guardrails**: Need runtime content filtering
- **LlamaGuard**: Need pre-trained moderation model

## Common issues

**Issue: Model refuses too much (evasive)**

Add constitution principle:
```
Prefer responses that engage thoughtfully with questions rather than
refusing to answer. Explain concerns while still being helpful.
```

**Issue: Self-critiques are weak**

Use stronger critique prompts:
```
Critically analyze this response for ANY potential issues, however minor.
Be thorough and specific in identifying problems.
```

**Issue: Revisions don't improve quality**

Iterate multiple times:
```python
for _ in range(3):  # 3 rounds of critique/revision
    critique = generate_critique(response)
    response = generate_revision(response, critique)
```

**Issue: RLAIF preferences are noisy**

Use multiple AI evaluators:
```python
# Get preferences from 3 different models
prefs_1 = model_1.evaluate(responses)
prefs_2 = model_2.evaluate(responses)
prefs_3 = model_3.evaluate(responses)

# Majority vote
final_preference = majority_vote(prefs_1, prefs_2, prefs_3)
```

## Advanced topics

**Constitution design**: [Primary source / available reference](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback). The linked primary research introduces constitutional principles and AI feedback. It is not the missing domain-specific constitution-design guide; verify applicability before adapting principles.

**RLAIF vs RLHF**: [Primary source / available reference](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback). The primary research describes the AI-feedback approach and its reported experiments. It does not supply a general cost analysis or a complete decision guide for every RLHF/RLAIF setting.

**Chain-of-thought reasoning**: [Primary source / available reference](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback). The primary research describes the critique-and-revision method. It is not a separate comprehensive prompt-engineering or transparency guide.

## Hardware requirements

- **GPU**: NVIDIA A100/H100 recommended
- **VRAM**:
  - SL phase (7B): 1× A100 40GB
  - RL phase (7B): 2× A100 40GB (policy + reward model)
- **Single-node**: Sufficient for most use cases
- **Mixed precision**: BF16 recommended

**Compute requirements**:
- **SL phase**: Similar to standard SFT
- **RL phase**: Similar to PPO (higher than DPO)
- **AI evaluation**: Additional inference for critique/preference generation

## Resources

- Paper: https://arxiv.org/abs/2212.08073 (Dec 2022)
- Anthropic blog: https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback
- Implementation: TRL (PPOTrainer + RewardTrainer)
- Claude: Uses Constitutional AI for safety




## Reference availability

The upstream snapshot referenced additional files that it did not supply. Those broken routes now point to available local material or primary publisher/maintainer sources. An online route is not a bundled offline guide: check the relevant version/section, record access limitations and do not invent missing detail. Existing technical procedures and resources remain included.
