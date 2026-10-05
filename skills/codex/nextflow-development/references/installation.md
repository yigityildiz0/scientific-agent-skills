# Installation

## Contents
- [Quick install](#quick-install)
- [Docker setup](#docker-setup)
- [Singularity setup (HPC)](#singularity-setup-hpc)
- [nf-core tools (optional)](#nf-core-tools-optional)
- [Verify installation](#verify-installation)
- [Common issues](#common-issues)

## Quick install

Follow the current [official Nextflow installation documentation](https://www.nextflow.io/docs/latest/install.html). Inspect the installer or release artifact, install it into a versioned environment, and record `nextflow -version` and `java -version`; do not pipe a remote script directly into a shell.

## Docker setup

### Linux

Use the institution's approved Docker or rootless container installation. System-package, daemon, and group changes require administrator or user approval and are not performed by this skill.

### macOS
Download Docker Desktop: https://docker.com/products/docker-desktop

### Verify
```bash
docker run hello-world
```

## Singularity setup (HPC)

Use the institution's approved Apptainer/Singularity module or installation path and record the exact runtime version. Do not modify a managed HPC environment from this skill.

### Configure cache
```bash
export NXF_SINGULARITY_CACHEDIR="$HOME/.singularity/cache"
mkdir -p $NXF_SINGULARITY_CACHEDIR
echo 'export NXF_SINGULARITY_CACHEDIR="$HOME/.singularity/cache"' >> ~/.bashrc
```

## nf-core tools (optional)

Install nf-core tools only in an isolated environment from a reviewed version, then preserve the exact environment lock. Do not add it to the global Python environment.

Useful commands:
```bash
nf-core list                    # Available pipelines
nf-core launch rnaseq           # Interactive parameter selection
nf-core download rnaseq -r 3.14.0  # Download for offline use
```

## Verify installation

```bash
nextflow run nf-core/demo -profile test,docker --outdir test_demo
ls test_demo/
```

## Common issues

**Java version wrong:**
```bash
export JAVA_HOME=/path/to/java11
```

**Docker permission denied:**
```bash
sudo usermod -aG docker $USER
# Log out and back in
```

**Nextflow not found:**
```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```
