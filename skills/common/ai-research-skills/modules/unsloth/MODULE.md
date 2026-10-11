# Module: unsloth

> Upstream orchestra-research/AI-research-SKILLs skill, unchanged. Paths are relative to this module folder.
> Original trigger scope: Expert guidance for fast fine-tuning with Unsloth - 2-5x faster training, 50-80% less memory, LoRA/QLoRA optimization

# Unsloth Skill

Comprehensive assistance with unsloth development, generated from official documentation.

## When to Use This Skill

This skill should be triggered when:
- Working with unsloth
- Asking about unsloth features or APIs
- Implementing unsloth solutions
- Debugging unsloth code
- Learning unsloth best practices

## Quick Reference

### Practical workflow

1. Select a supported checkpoint and a small representative dataset. Confirm
   PyTorch/CUDA/Unsloth/TRL compatibility in the live official docs.
2. Load with `FastLanguageModel.from_pretrained(..., load_in_4bit=True)` for
   QLoRA, then attach adapters with `FastLanguageModel.get_peft_model(...)`.
3. Inspect the dataset's chat template, EOS and assistant-only loss masking.
   Run a short training/evaluation smoke test before scaling sequence length.
4. Use the installed TRL API (`SFTConfig`, `processing_class`) and select
   BF16 only when supported; otherwise supported GPU FP16. Save tokenizer and
   adapter together and compare held-out outputs before/after training.

Portable profiles: CPU is for dataset/tokenizer checks (use Transformers/TRL for
tiny CPU training); a small compatible GPU starts with a 0.5–3B QLoRA model,
batch 1 and short context. Linux multi-GPU needs an explicitly supported backend.
Remote notebooks require a chosen budget and data scope. Native Windows support
depends on the exact release and dependency matrix.

## Reference Files

This skill includes comprehensive documentation in `references/`:

- [index.md](references/index.md) — available reference inventory.
- [llms-txt.md](references/llms-txt.md) — documentation entry points.
- [llms.md](references/llms.md) — local documentation snapshot.
- [llms-full.md](references/llms-full.md) — large snapshot; search targeted headings.

Use the host's read/search tools for targeted sections. Snapshots may contain
historical APIs; verify against https://docs.unsloth.ai/ before execution.

## Working with This Skill

### For Beginners
Start with `references/index.md` and the current official getting-started guide.

### For Specific Features
Search the actual reference files above for the model family or feature.

### For Code Examples
Use linked official notebooks matching your model and installed version.

## Resources

### references/
Organized documentation extracted from official sources. These files contain:
- Detailed explanations
- Code examples with language annotations
- Links to original documentation
- Table of contents for quick navigation

This module does not ship executable helper scripts or asset templates.

## Notes

- This skill was automatically generated from official documentation
- Reference files preserve the structure and examples from source docs
- Code examples include language detection for better syntax highlighting
- Quick reference patterns are extracted from common usage examples in the docs

## Updating

To refresh this skill with updated documentation:
1. Re-run the scraper with the same configuration
2. The skill will be rebuilt with the latest information

<!-- Trigger re-upload 1763621536 -->



