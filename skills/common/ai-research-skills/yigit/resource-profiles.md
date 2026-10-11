# Hardware and example validation

## Choose the execution profile first

Discover only the task-relevant environment: OS, native/WSL/container runtime,
framework and driver versions, GPU family/count, available VRAM/RAM, model,
precision, sequence length, micro-batch and training versus inference. Do not
persist an individual's machine inventory in this reusable library.

| Profile | Suitable starting point | Required checks |
|---|---|---|
| CPU/local client | Literature, tokenizers, data inspection, tracking, small embeddings, GGUF CPU inference | RAM, data size, explicit local versus remote model/embedding provider |
| One consumer GPU around 12 GB | Small models, measured low-bit inference, partial GGUF offload, bounded PEFT experiments | Runtime/GPU support, context/KV cache, activations and peak memory; begin with a small micro-batch |
| Multi-GPU workstation | Supported distributed training/inference | Actual world size, model divisibility, launcher/rank/rendezvous and checkpoint ownership |
| Linux cluster or cloud | Large-model/full training, robotics and multi-node examples | GPU count and memory per device, supported image, budget and dataset authorization |

A CUDA GPU does not rule out llama.cpp. A single GPU does not gain extra device
memory from FSDP/ZeRO sharding across one rank. Windows is not Linux: label Bash
commands explicitly and use a verified native, WSL2 or container path. Confirm
the selected framework build supports the GPU generation; an old CUDA wheel is
not a general installation recipe for newer hardware.

## Account for memory honestly

For a dense model, raw weight bytes are approximately parameter count times
bytes per parameter: 7 billion FP16/BF16 parameters alone need 14 GB (about
13.0 GiB). Quantization adds scales/metadata; runtime buffers, KV cache and
activations still need memory. Training adds gradients, optimizer state and
possibly reference/teacher models. State offload, adapter sharing and optimizer
precision explicitly. Sparse MoE computation does not mean all expert weights
disappear from storage. Gradient accumulation only reduces per-step activation
memory when the micro-batch is actually reduced.

Measure peak allocated/reserved GPU memory and relevant host RAM for the real
workload. Distinguish model-load OOM, KV-cache capacity and training activation
OOM before changing settings. Do not promise a model fits from weight size alone.

## Make examples reproducible

1. Select one documented API/version family; keep runnable code separate from
   pseudocode and label omitted application-specific parts.
2. Include imports, concrete input shapes, valid configuration syntax, data/model
   paths and required files. Keep shell and Python in separate code blocks.
3. For causal language-model training, verify next-token alignment, padding/loss
   masks, gradient reset/accumulation boundaries and finite loss/gradients before
   updating parameters. Keep old behavior policy and frozen reference distinct.
4. Validate output contracts: decode only generated tokens when appropriate,
   parse exact structured decisions, and report malformed output explicitly.
5. Match launched processes to allocated resources. Avoid nesting an eight-worker
   launcher inside eight tasks per node; document which layer creates workers.
6. For performance claims, record hardware, versions, dtype, batch/context/output
   length, warm-up/compilation and synchronization. Compare equivalent workloads;
   show measured uncertainty and distinguish a published benchmark from a local run.

## Türkçe kısa kullanım

Önce işletim sistemi, GPU sayısı, bellek ve model/iş yükünü belirle. Tek GPU için
küçük ve ölçülebilir bir başlangıç seç; küme tarifini doğrudan yerel kurulum gibi
sunma. Örnek kodun sözdizimi kontrolü, GPU'da çalışması ve bilimsel doğruluğu ayrı
kanıtlardır. Doğal tetikler: “12 GB GPU'ya uygun başlangıç”, “Windows kurulumunu
doğrula”, “eğitim belleğini hesapla”, “benchmark koşullarını karşılaştır”. Bunlar
kayıtlı slash komutları değildir.
