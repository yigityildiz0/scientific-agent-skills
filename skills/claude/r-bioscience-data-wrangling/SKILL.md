---
name: r-bioscience-data-wrangling
description: "Clean, reshape, join, validate, and document laboratory, genetics, omics, sample-sheet, CSV, TSV, and spreadsheet data in R without corrupting identifiers or silently dropping."
license: MIT
metadata:
  source: original synthesis from official dplyr, tidyr, readr, R, and Posit guidance
  reviewed: '2026-07-10'
---

# R Bioscience Data Wrangling

Turn messy research tables into analysis-ready data without losing biological meaning. The goal is not merely code that runs; it is a traceable transformation where every row, identifier, unit, exclusion, and missing value can be explained.

## Route related work

- Project layout, package versions, `renv`, and clean-session execution: use `rstudio-reproducible-analysis`.
- Statistical model and inference: use `r-biostatistics-workflow`.
- Bulk RNA-seq count models: use `bio-differential-expression-deseq2-basics`.
- Figures: use `bio-data-visualization-ggplot2-fundamentals`.
- Reproducible report: use `quarto-authoring`.

## Discover before transforming

1. Preserve the original file and its hash, source, export date, instrument/software version, delimiter, encoding, decimal convention, sheet, and timezone.
2. Read the data dictionary, protocol, sample sheet, plate map, and expected experimental units.
3. Inspect names, dimensions, classes, representative values, unique-key candidates, missingness, duplicated rows, and impossible ranges.
4. Identify sensitive columns before any external lookup or upload.
5. Define the output contract: one row represents what, one column represents what, which key must be unique, expected units, accepted categories, and permitted missingness.

Never infer biology from a filename alone. Ask or flag ambiguity when `rep1`, `batch2`, `control`, or an abbreviated genotype could mean multiple things.

## Import safely

Prefer explicit column types for critical fields. Gene IDs, sample IDs, plate wells, barcodes, accessions, and postal-like codes are strings even when they look numeric.

```r
library(readr)

samples <- read_csv(
  "data-raw/sample-sheet.csv",
  col_types = cols(
    sample_id = col_character(),
    gene_id = col_character(),
    condition = col_character(),
    batch = col_character(),
    concentration_ng_ul = col_double()
  ),
  na = c("", "NA", "N/A")
)

problems(samples)
stopifnot(nrow(samples) > 0)
```

Guard against:

- spreadsheet scientific notation or date coercion of gene identifiers;
- dropped leading zeros;
- locale-specific commas/decimal marks;
- duplicated or invisible Unicode characters in keys;
- mixed units in one column;
- formulas or merged cells exported as data;
- an Excel display value that differs from the stored value;
- row names treated as identifiers without an explicit column.

If `readr`, `readxl`, `dplyr`, or `tidyr` is not installed, report it. Do not install or update packages automatically.

## Validate keys and joins

Every join must state its intended relationship and prove it.

```r
library(dplyr)

duplicates <- samples |>
  count(sample_id, name = "n") |>
  filter(n != 1)
stopifnot(nrow(duplicates) == 0)

before <- nrow(measurements)
joined <- measurements |>
  left_join(samples, by = "sample_id", relationship = "many-to-one")

stopifnot(nrow(joined) == before)
stopifnot(!any(is.na(joined$condition)))
```

For installed dplyr versions without `relationship=`, implement explicit uniqueness and anti-join checks instead of omitting validation.

Before and after a join, record:

- input and output row counts;
- unique key counts;
- unmatched keys from both sides with `anti_join()`;
- many-to-many expansion;
- duplicated metadata rows;
- missing values introduced in required fields.

Never use `distinct()` to hide an unexpected many-to-many join. Fix or document the key relationship.

## Tidy without changing meaning

Tidy data means variables in columns, observations in rows, and one value per cell. Reshape only after defining the observational unit.

```r
library(tidyr)

long <- plate_export |>
  pivot_longer(
    cols = starts_with("cycle_"),
    names_to = "cycle",
    names_prefix = "cycle_",
    names_transform = list(cycle = as.integer),
    values_to = "fluorescence",
    values_drop_na = FALSE
  )
```

After `pivot_longer()` or `pivot_wider()`, assert expected row/key counts. Aggregation in `pivot_wider(values_fn=...)` is a statistical decision; do not average duplicates merely to make the reshape succeed.

## Missing data, categories, and units

1. Distinguish not measured, below detection, failed QC, not applicable, and truly missing. Do not collapse them to one code without a documented mapping.
2. Keep raw values and create separate derived flags/transforms.
3. Set factor levels explicitly before modeling or plotting; record the reference category.
4. Normalize units only with a named conversion and preserve the source column.
5. Parse dates/times with explicit format and timezone.
6. Do not convert “<LOD” to zero. Preserve the qualifier and use a method appropriate to censored data.
7. Do not impute, winsorize, remove outliers, or correct batches in a cleaning step unless the scientific method and validation are explicitly selected.

## Derived-data contract

Write generated data to `data-derived/`, never over the only raw copy. Prefer interoperable formats for handoff and include a data dictionary.

For each output record:

- source files and hashes;
- transformation script and version;
- timestamp and software/package versions;
- row/column counts;
- key and range checks;
- exclusions and reasons;
- warnings and unresolved mappings.

Example assertions:

```r
stopifnot(!anyDuplicated(analysis$sample_id))
stopifnot(all(analysis$viability_percent >= 0 & analysis$viability_percent <= 100, na.rm = TRUE))
stopifnot(setequal(unique(analysis$condition), c("control", "treated")))
stopifnot(all(analysis$sample_id %in% samples$sample_id))
```

Do not hard-code expected categories if the study design says otherwise; derive assertions from the approved contract.

## Completion checklist

- Raw files unchanged and traceable.
- Column types and missing-value codes explicit.
- Unique keys and observational unit stated.
- Joins have cardinality and unmatched-key checks.
- Reshapes preserve expected observations.
- Units, categories, reference levels, and exclusions documented.
- Derived files can be regenerated in a clean R session.
- A human-readable data dictionary and transformation report accompany the output.

## Example prompts

- “Use $r-bioscience-data-wrangling to clean this sample sheet. Preserve IDs as text, audit duplicates and unmatched keys, and do not overwrite the source workbook.”
- “Bu qPCR plate exportunu R ile long formata çevir; her reshape ve join sonrası satır/anahtar sayılarını doğrula, missing ve failed-QC durumlarını ayır.”
- “Compare the data dictionary with the CSV, list type/unit/category violations, and create a reproducible derived dataset plus validation report.”

## Primary references

- dplyr articles: https://dplyr.tidyverse.org/articles/
- tidyr tidy-data principles: https://tidyr.tidyverse.org/articles/tidy-data.html
- tidyr articles: https://tidyr.tidyverse.org/articles/
- readr column specification: https://readr.tidyverse.org/articles/column-specification.html
- R data frames: https://stat.ethz.ch/R-manual/R-devel/library/base/html/data.frame.html
