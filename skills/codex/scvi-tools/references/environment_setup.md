> Safety: run installation commands only after explicit user approval, inside an isolated environment; pin and record the tested versions.

# Environment Setup for scvi-tools

This reference covers installation and environment configuration for scvi-tools.

## Installation policy

Use an isolated environment and verify the current official installation page before installing. Do not modify a global research environment or guess a CUDA wheel URL. As of 2026-07-10, the current stable documentation supports Python 3.12-3.14 and provides `cuda` and `metal` extras; the repository's latest stable tag observed during this package audit was `1.5.0.post1`.

### CPU environment

```bash
uv venv --python 3.13 .scvi-env
# Linux/macOS: source .scvi-env/bin/activate
# Windows PowerShell: .scvi-env\Scripts\Activate.ps1
uv pip install "scvi-tools==1.5.0.post1" scanpy leidenalg
uv pip freeze > scvi-environment.lock.txt
```

### NVIDIA GPU on supported Linux

```bash
uv pip install "scvi-tools[cuda]==1.5.0.post1" scanpy leidenalg
uv pip freeze > scvi-environment.lock.txt
```

### Apple Silicon

```bash
uv pip install "scvi-tools[metal]==1.5.0.post1" scanpy leidenalg
uv pip freeze > scvi-environment.lock.txt
```

For spatial or MuData workflows, add only the packages needed by the selected model, then regenerate the lock record. Confirm the version and extras against [official scvi-tools installation documentation](https://docs.scvi-tools.org/en/stable/installation.html) because platform support can change.

## Verify Installation

```python
import scvi
import torch
import scanpy as sc

print(f"scvi-tools version: {scvi.__version__}")
print(f"scanpy version: {sc.__version__}")
print(f"PyTorch version: {torch.__version__}")
print(f"GPU available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"GPU device: {torch.cuda.get_device_name(0)}")
    print(f"GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
```

## GPU Configuration

### Check CUDA Version

```bash
nvidia-smi
nvcc --version
```

### PyTorch and accelerator compatibility

Use the accelerator extra recommended by the installed scvi-tools release. If hardware or driver compatibility requires a custom PyTorch build, select it from the current official PyTorch installer, record the resolved versions, and rerun the validation script before training. Do not reuse a hardcoded CUDA wheel command from an old environment.

### Memory Management

```python
import torch

# Clear GPU cache between models
torch.cuda.empty_cache()

# Monitor memory usage
print(f"Allocated: {torch.cuda.memory_allocated() / 1e9:.2f} GB")
print(f"Cached: {torch.cuda.memory_reserved() / 1e9:.2f} GB")
```

## Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| `CUDA out of memory` | GPU memory exhausted | Reduce batch_size, use smaller model |
| `No GPU detected` | CUDA not installed | Install CUDA toolkit matching PyTorch |
| `Version mismatch` | PyTorch/CUDA incompatibility | Reinstall PyTorch with correct CUDA version |
| `Import error scvi` | Missing/incompatible dependencies | Recreate the isolated environment from the reviewed lock; do not patch the global environment |

## Jupyter Setup

Add `ipykernel`, `matplotlib`, and `seaborn` to the active isolated environment from reviewed versions, refresh `scvi-environment.lock.txt`, then register that environment as a Jupyter kernel. Do not install notebook packages globally.

## Package-version record

For reproducibility, preserve the exact resolved environment rather than broad minimum-version ranges:

```bash
python -m pip show scvi-tools scanpy anndata torch
uv pip freeze > scvi-environment.lock.txt
```

Store that lock record with the model, processed AnnData object, training parameters, random seed, and hardware/accelerator details.

## Version Compatibility Guide

### scvi-tools 1.x vs 0.x API Changes

The 1.x release introduced breaking changes. Key differences:

| Operation | 0.x API (deprecated) | 1.x API (current) |
|-----------|---------------------|-------------------|
| Setup data | `scvi.data.setup_anndata(adata, ...)` | `scvi.model.SCVI.setup_anndata(adata, ...)` |
| Register data | `scvi.data.register_tensor_from_anndata(...)` | Built into `setup_anndata` |
| View setup | `scvi.data.view_anndata_setup(adata)` | `scvi.model.SCVI.view_anndata_setup(adata)` |

### Migration from 0.x to 1.x

```python
# OLD (0.x) - DEPRECATED
import scvi
scvi.data.setup_anndata(adata, layer="counts", batch_key="batch")
model = scvi.model.SCVI(adata)

# NEW (1.x) - CURRENT
import scvi
scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key="batch")
model = scvi.model.SCVI(adata)
```

### Model-Specific Setup (1.x)

Each model has its own setup method:

```python
# scVI
scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key="batch")

# scANVI
scvi.model.SCANVI.setup_anndata(adata, layer="counts", batch_key="batch", labels_key="cell_type")

# totalVI
scvi.model.TOTALVI.setup_anndata(adata, layer="counts", protein_expression_obsm_key="protein")

# MultiVI (uses MuData)
scvi.model.MULTIVI.setup_mudata(mdata, rna_layer="counts", atac_layer="counts")

# PeakVI
scvi.model.PEAKVI.setup_anndata(adata, batch_key="batch")

# veloVI
scvi.external.VELOVI.setup_anndata(adata, spliced_layer="spliced", unspliced_layer="unspliced")
```

### Compatibility requirements

Do not infer compatibility from broad minimum versions. Resolve dependencies through the selected scvi-tools release and its extras, inspect the installed APIs, and preserve the exact lock. Model-specific packages such as MuData or scVelo are added only for the selected workflow.

### Check Your Versions

```python
import scvi
import scanpy as sc
import anndata
import torch

print(f"scvi-tools: {scvi.__version__}")
print(f"scanpy: {sc.__version__}")
print(f"anndata: {anndata.__version__}")
print(f"torch: {torch.__version__}")

# Check if using 1.x API
if hasattr(scvi.model.SCVI, 'setup_anndata'):
    print("Using scvi-tools 1.x API")
else:
    print("WARNING: Using deprecated 0.x API - please upgrade")
```

### Known Compatibility Issues

| Issue | Affected Versions | Solution |
|-------|-------------------|----------|
| `setup_anndata` not found | API/environment mismatch | Compare against the installed release docs and recreate the locked environment |
| MuData errors | Missing/incompatible model extras | Recreate the environment with the release's supported MuData extra/dependencies |
| CUDA version mismatch | Accelerator stack mismatch | Recreate from current official scvi-tools/PyTorch guidance |
| NumPy incompatibility | Dependency resolver or old lock | Rebuild from a reviewed compatible lock; do not ad-hoc downgrade a shared environment |

### Changing scvi-tools versions

Never upgrade a model environment in place. Create a separate environment for the proposed version, preserve the old lock, inspect release notes and API changes, rerun data validation and a small representative training/load/DE test, and migrate only after output comparison. Keep the original environment available for existing serialized models.

## Testing Installation

```python
# Quick test with sample data
import scvi
import scanpy as sc

# Load test dataset
adata = scvi.data.heart_cell_atlas_subsampled()
print(f"Loaded test data: {adata.shape}")

# Setup and create model (quick test)
scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key="cell_source")
model = scvi.model.SCVI(adata, n_latent=10)
print("Model created successfully")

# Quick training test (1 epoch)
model.train(max_epochs=1)
print("Training works!")
```
