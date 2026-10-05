---
name: rstudio-reproducible-analysis
description: "Use RStudio safely for reproducible scientific and genetics data analysis. Use when creating or repairing an RStudio Project, organizing R scripts and data, managing project-local."
license: MIT
metadata:
  source: original synthesis from official Posit RStudio and renv documentation
  reviewed: '2026-07-10'
  compatibility: Requires R; RStudio and renv are optional. Inspect installed versions before giving version-sensitive commands.
---

# RStudio Reproducible Analysis

Build an analysis that can be rerun by another researcher from source data to final outputs. Treat the RStudio interface as an editor around a project on disk; the files, lockfile, scripts, inputs, and recorded parameters are the source of truth.

## Start with discovery

Before editing or running anything:

1. Find the project root. Prefer an existing `.Rproj`, `renv.lock`, `.git`, `_quarto.yml`, or explicit user path. Never insert `setwd()` just to make paths work.
2. Inventory `.R`, `.Rmd`, `.qmd`, `DESCRIPTION`, `renv.lock`, `.Rprofile`, input-data, metadata, notebooks, reports, figures, and tests.
3. Inspect the actual environment with read-only checks such as `R.version.string`, `.libPaths()`, `sessionInfo()`, `renv::status()` when renv is already installed, and `packageVersion()` for packages the analysis uses.
4. Read the study design and data dictionary before choosing transformations, contrasts, models, or plots. Do not infer biological replicates from filenames.
5. Separate facts from assumptions. Record unresolved sample labels, units, exclusions, batch variables, reference levels, and missing-value meaning.

## Choose the narrow workflow

| Need | Workflow |
|---|---|
| Start or organize an analysis | RStudio Project + explicit folders + numbered scripts |
| Reproduce package versions | Existing `renv.lock`; `renv::restore()` only after reviewing the diff and authorization |
| Record a known-good environment | Test first, then `renv::snapshot()` and review the lockfile diff |
| Write a reproducible report | Use the `quarto-authoring` skill for `.qmd` and citations |
| Bulk RNA-seq differential expression | Use `bio-differential-expression-deseq2-basics` after verifying the design and count matrix |
| Publication plots | Use `bio-data-visualization-ggplot2-fundamentals` after the statistical result is validated |
| Debug a failure | Reproduce in a fresh R session, reduce to the smallest failing input, inspect classes and versions |

## Recommended project shape

Adapt to the existing project instead of forcing a template. For a new analysis, prefer:

```text
study-name/
  study-name.Rproj
  README.md
  renv.lock
  renv/
  data-raw/       # immutable source exports; never overwrite
  data-derived/   # generated, reproducible intermediate data
  metadata/       # sample sheet, data dictionary, provenance
  R/              # reusable functions
  scripts/        # numbered pipeline steps
  reports/        # .qmd/.Rmd source
  figures/        # generated outputs
  results/        # generated tables
  tests/          # checks for reusable functions and invariants
```

Do not duplicate protected or sensitive data into a repository. Check `.gitignore`, institutional policy, consent, and de-identification requirements before any commit, upload, or sharing step.

## Reproducible execution

1. Start from a clean R session; do not rely on objects left in `.GlobalEnv`.
2. Configure RStudio to avoid restoring `.RData` and avoid saving workspace images. `.RData` is not a reproducible dependency record.
3. Use project-relative paths with `file.path()` or `here::here()` if already adopted. Keep source inputs read-only and write generated outputs elsewhere.
4. Put parameters, reference levels, thresholds, seeds, and exclusions in source code or a versioned config file.
5. Break the analysis into deterministic steps. Each step checks its inputs, creates named outputs, and fails loudly on invalid dimensions, duplicated identifiers, impossible values, or missing sample metadata.
6. Use `set.seed()` only for stochastic operations and record the algorithm/package versions when randomness affects results.
7. Run the complete pipeline in a fresh session or with `Rscript` before calling it reproducible. Rendering one notebook cell-by-cell is not an end-to-end test.
8. Save `sessionInfo()` or `sessioninfo::session_info()` with the released report when package versions materially affect results.

## Package safety with renv

Use the installed project policy first. Never run `install.packages()`, `BiocManager::install()`, `renv::update()`, `renv::snapshot()`, or `renv::restore()` merely because a package is missing.

```r
# Read-only diagnosis
R.version.string
.libPaths()
if (requireNamespace("renv", quietly = TRUE)) renv::status()
if (requireNamespace("DESeq2", quietly = TRUE)) packageVersion("DESeq2")
```

For an authorized environment change:

1. Back up or commit the current `renv.lock` and `.Rprofile`.
2. Explain which packages and system dependencies will change.
3. Make the smallest project-local change.
4. Run the analysis checks and render the report.
5. Only after success, snapshot and review the lockfile diff.
6. If regression appears, restore the known-good lockfile rather than layering more updates.

Bioconductor packages must be compatible with the installed R/Bioconductor release. Verify with official Bioconductor tooling and installed package documentation; do not mix arbitrary CRAN/GitHub versions into a validated analysis without a recorded reason.

## Debugging ladder

1. Restart R and rerun the smallest failing command.
2. Capture the exact error, `traceback()`, object classes, dimensions, names, factor levels, and a privacy-safe minimal input.
3. Confirm the function comes from the expected package with `getAnywhere()` or an explicit `package::function` call.
4. Check the installed help and signature before adapting code: `?package::function`, `args(package::function)`, `packageVersion()`.
5. Test data invariants: unique sample IDs, matched metadata rows, nonnegative integer counts where required, no hidden unit changes, and expected missingness.
6. Fix the cause in source code. Do not silence warnings globally or wrap unknown failures in `try()`.
7. Add a regression check or minimal test, then rerun from a clean session.

## Scientific quality gates

Before delivering results, verify:

- Experimental unit and biological replicate are explicit; technical replicates are not treated as independent samples.
- Batch, pairing, repeated measures, interactions, and covariates are encoded intentionally.
- The stated statistical question matches the implemented model and contrast.
- Multiple-testing correction and the tested hypothesis family are reported.
- Effect sizes, uncertainty, sample counts, exclusions, and missing data are shown, not only p-values.
- Gene/transcript identifiers include organism, annotation source, and version; mapping losses and duplicates are reported.
- Every table and figure can be regenerated from scripts and recorded inputs.
- No patient, participant, proprietary, or unpublished data is sent to an external service without authorization.

## User-facing output

Report:

1. project path and entry point;
2. exact run order or command;
3. input/output inventory;
4. environment and lockfile status;
5. checks performed and failures;
6. scientific assumptions and limitations;
7. files changed, with a rollback path.

## Example prompts

- “Bu RStudio projesini baştan sona incele; veri dosyalarına dokunmadan çalıştırılabilir ve yeniden üretilebilir hale getir.”
- “`renv.lock` ile kurulu paketleri karşılaştır, yalnız gerekli farkları göster; otomatik güncelleme yapma.”
- “Bu hata için temiz oturumda minimal örnek üret, veri sınıflarını ve paket sürümlerini kontrol et.”
- “Make this genetics analysis reproducible in RStudio and produce a Quarto report with a recorded session.”

## Primary references

- RStudio Projects: https://docs.posit.co/ide/user/ide/guide/code/projects.html
- RStudio IDE User Guide: https://docs.posit.co/ide/user/
- renv workflow: https://rstudio.github.io/renv/
- renv snapshot/restore: https://rstudio.github.io/renv/reference/snapshot.html
- Quarto with R: https://quarto.org/docs/computations/r.html
- Bioconductor installation and release compatibility: https://bioconductor.org/install/
