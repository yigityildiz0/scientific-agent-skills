# Module: deepspeed

> Based on orchestra-research/AI-research-SKILLs; executable entry points repaired 2026-10-08. Paths are relative to this module.
> Trigger scope: distributed training, ZeRO, offload, pipeline/model parallelism, precision, optimizers, profiling, DeepNVMe and MoE.

# DeepSpeed training and profiling

## Choose the smallest appropriate setup

1. Check the installed PyTorch/CUDA/DeepSpeed combination and `ds_report`.
2. On one 12 GB GPU, start with a small model or supported adapter training,
   micro-batch 1 and short sequences; offload consumes host RAM and bandwidth.
3. Use ZeRO-1 for optimizer sharding, ZeRO-2 for gradients too, ZeRO-3 for
   parameters too. Sharding benefits require multiple ranks; CPU/NVMe offload
   is a separate option. NVMe needs supported operators and Linux prerequisites.
4. Choose one precision path supported by hardware and the installed release.
   FP16 is not mandatory. FP32 works; BF16 can be used on supported hardware.
   Never enable both the `fp16` and `bf16` blocks at once. FP8 needs a separately
   validated backend/model recipe, not a generic precision switch.

## Minimal training path

Save as `ds_config.json` (FP32 baseline, one process):

```json
{
  "train_micro_batch_size_per_gpu": 1,
  "gradient_accumulation_steps": 1,
  "optimizer": {"type": "Adam", "params": {"lr": 0.001}},
  "zero_optimization": {"stage": 0},
  "wall_clock_breakdown": false
}
```

Save as `train.py`; this is a small smoke test before adapting the model/data:

```python
import argparse
import torch
import deepspeed

parser = deepspeed.add_config_arguments(argparse.ArgumentParser())
parser.add_argument("--local_rank", type=int, default=-1)
args = parser.parse_args()
model = torch.nn.Linear(8, 1)
engine, optimizer, _, _ = deepspeed.initialize(
    args=args, model=model, model_parameters=model.parameters()
)
for step in range(4):
    x = torch.randn(2, 8, device=engine.device)
    target = x.sum(dim=-1, keepdim=True)
    loss = torch.nn.functional.mse_loss(engine(x), target)
    engine.backward(loss)
    engine.step()  # DeepSpeed manages accumulation and gradient clearing.
engine.save_checkpoint("checkpoints", tag="smoke")  # Every rank must call.
```

```bash
ds_report
deepspeed --num_gpus 1 train.py --deepspeed --deepspeed_config ds_config.json
```

For BF16 add `"bf16": {"enabled": true}` as a sibling field and feed the model
the appropriate floating dtype. With plain PyTorch outside the DeepSpeed engine,
call `optimizer.zero_grad(set_to_none=True)` each step; profiling does not clear
gradients for you.

## Elasticity: typed example

This is a separate multi-rank scheduling configuration, not an addition to the
single-process smoke test. Elastic support depends on the launcher/release.
Do not copy scraped values such as `"max_train_batch_size": "seqlen"`.

```json
{
  "elasticity": {
    "enabled": true,
    "max_train_batch_size": 2000,
    "micro_batch_sizes": [2, 4, 6],
    "min_gpus": 1,
    "max_gpus": 8,
    "min_time": 20,
    "version": 0.2,
    "ignore_non_elastic_batch_info": false,
    "num_gpus_per_node": 1,
    "model_parallel_size": 1
  }
}
```

Keep batch fields within the elasticity configuration rather than silently
ignoring conflicting non-elastic values. JSON needs quoted keys, colons,
commas between members, lowercase booleans and `null` (not Python `None`).

## BERT and profiler integration pattern

This adapter assumes an existing encoder and its hidden dimension. The forward
signature accepts a tokenizer dictionary, so use `model(**inputs)` consistently.

```python
import torch

class BertClassifier(torch.nn.Module):
    def __init__(self, encoder, hidden_size, num_labels):
        super().__init__()
        self.encoder = encoder
        self.classifier = torch.nn.Linear(hidden_size, num_labels)

    def forward(self, input_ids, attention_mask=None, token_type_ids=None):
        encoded = self.encoder(
            input_ids=input_ids, attention_mask=attention_mask,
            token_type_ids=token_type_ids
        )
        return self.classifier(encoded.last_hidden_state[:, 0, :])

# Application supplies encoder, inputs and labels on the same device.
model = BertClassifier(encoder, encoder.config.hidden_size, num_labels=2)
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)
optimizer.zero_grad(set_to_none=True)
logits = model(**inputs)
loss = torch.nn.functional.cross_entropy(logits, labels)
loss.backward()
optimizer.step()
```

## Capability map and retained references

| Need | Reference |
|---|---|
| ZeRO, pipeline parallelism, MoE/MoS, LR range tests, FLOPs profiler, DeepNVMe | [tutorials.md](references/tutorials.md) |
| Config parameters, optimizers, precision, communication, monitoring | [other.md](references/other.md) |
| Inference/MII | [mii.md](references/mii.md) |
| Historical performance and releases | [2020.md](references/2020.md), [2023.md](references/2023.md), [08.md](references/08.md), [09.md](references/09.md), [assets.md](references/assets.md) |
| Complete former scraped overview, retained without content loss | [legacy extraction](references/legacy-extracted-overview.md) |

Use the active host's file/search tools, not a presumed `view` tool. Historical
scrapes preserve context, not current API guarantees. Check release-specific
docs before scaling or selecting an optional operator:

- https://www.deepspeed.ai/getting-started/
- https://www.deepspeed.ai/docs/config-json/
- https://www.deepspeed.ai/tutorials/flops-profiler/
- https://github.com/deepspeedai/DeepSpeed
