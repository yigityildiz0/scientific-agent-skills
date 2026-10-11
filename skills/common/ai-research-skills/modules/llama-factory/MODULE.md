# Module: llama-factory

> Upstream orchestra-research/AI-research-SKILLs skill, unchanged. Paths are relative to this module folder.
> Original trigger scope: Expert guidance for fine-tuning LLMs with LLaMA-Factory - WebUI no-code, 100+ models, 2/3/4/5/6/8-bit QLoRA, multimodal support

# Llama-Factory Skill

Comprehensive assistance with llama-factory development, generated from official documentation.

## When to Use This Skill

This skill should be triggered when:
- Working with llama-factory
- Asking about llama-factory features or APIs
- Implementing llama-factory solutions
- Debugging llama-factory code
- Learning llama-factory best practices

## Quick Reference

### Common Patterns

The extracted references below contain damaged text and missing tab/code content. Use this verified entry point for executable commands; preserve references as historical context and check the linked upstream page when a section is incomplete.

### Verified quick start (2026-10-08)

Source: https://github.com/hiyouga/LLaMA-Factory and its `examples/README.md`.

```bash
git clone --depth 1 https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e .
pip install -r requirements/metrics.txt
llamafactory-cli version
llamafactory-cli webui
```

For training, inspect an existing YAML under `examples/train_lora/` or `examples/train_qlora/` for the installed commit, select a supported model/template pair, register the dataset in `data/dataset_info.json`, then run `llamafactory-cli train path/to/config.yaml`. Record the commit and effective config with results. Set `stage: sft`, `finetuning_type: lora`, `do_train: true`; QLoRA additionally needs a supported quantization backend and `quantization_bit: 4`. Merge/export with the matching `examples/merge_lora/` recipe; do not merge into an already quantized base.

**Portable local profile:** Windows + a 12 GB NVIDIA GPU should start with a supported small model (roughly 0.5–3B), 4-bit QLoRA where available, batch size 1 and short `cutoff_len` (256–512). Verify the installed PyTorch/CUDA build supports the GPU architecture (including RTX 50-series); an old CUDA wheel is not a universal fix. Measure peak VRAM before increasing context. Linux multi-GPU/DeepSpeed and large-model recipes are separate remote profiles. CPU offload trades speed and RAM for VRAM and is not universal backend support.

## Reference Files

This skill includes comprehensive documentation in `references/`:

- **advanced.md** - Advanced documentation
- **getting_started.md** - Getting Started documentation
- **other.md** - Other documentation

Use the host's read tool to inspect the linked reference files.

## Working with This Skill

### For Beginners
Start with the verified quick start above, then `references/getting_started.md` and its upstream links.

### For Specific Features
Use `references/advanced.md` for training/data/export options and `references/other.md` for supporting material.

### For Code Examples
The quick reference section above contains common patterns extracted from the official docs.

## Resources

### references/
Organized documentation extracted from official sources. These files contain:
- Detailed explanations
- Code examples with language annotations
- Links to original documentation
- Table of contents for quick navigation

### scripts/
Add helper scripts here for common automation tasks.

### assets/
Add templates, boilerplate, or example projects here.

## Notes

- This skill was automatically generated from official documentation
- Reference files preserve the structure and examples from source docs
- Code examples include language detection for better syntax highlighting
- Quick reference patterns are extracted from common usage examples in the docs

## Updating

To refresh this skill with updated documentation:
1. Re-run the scraper with the same configuration
2. The skill will be rebuilt with the latest information


