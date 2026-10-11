# PyTorch Precision and Patching Gotchas

## Transformer patch requirement

OpenPI PyTorch requires custom patches applied to the installed `transformers` package. Training or inference without the patch produces subtle incompatibilities.

**Apply patches:**

```bash
cp -r ./src/openpi/models_pytorch/transformers_replace/* \
  .venv/lib/python3.11/site-packages/transformers/
```

**Verify the patch is active:**

Compare the installed patch files with the pinned repository's replacement files
(content hashes), then run the repository's documented import/smoke check.
Timestamps alone do not establish patch identity or compatibility.

## Reinstall overwrites the patch

If `uv sync` or `pip install` reinstalls `transformers`, the patch is overwritten.

Fix: after inspecting the lockfile, reinstall the matching dependency if needed:

```bash
uv sync --reinstall-package transformers
```

Then reapply the matching patch. `uv cache clean transformers` only clears cache;
it does not modify the installed package. Locate site-packages for the active
interpreter instead of assuming the Python 3.11 Linux path on other platforms.

## OOM while loading checkpoints

Set memory allocation strategy before loading large models:

```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

## Resume mode

- `--resume` requires `--exp_name` to match the prior run exactly.
- At least one numeric checkpoint directory must exist under `checkpoints/<config_name>/<exp_name>/`.
- Do not combine `--resume` with other conflicting flags.

## Precision notes

- Default training precision follows the model config.
- When converting from JAX, ensure the output precision matches expectations (bf16 vs fp32).
- Mixed precision settings in PyTorch should align with the source JAX checkpoint precision.
