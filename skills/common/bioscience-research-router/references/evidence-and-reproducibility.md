# Evidence and reproducibility checklist

## Evidence hierarchy

Prefer the narrowest authoritative source that answers the question:

1. Current regulation, official agency source, standard, or database record.
2. Primary peer-reviewed study and its supplements/data/code.
3. Systematic review or consensus guideline appropriate to the question.
4. Maintainer documentation and versioned release notes for software behavior.
5. Preprint, conference abstract, vendor material, or secondary commentary, clearly labeled.

Do not treat citation count, journal prestige, or a single statistically significant result as proof.

## Minimum evidence ledger

For each material claim record:

- exact claim;
- source title and stable identifier (DOI, PMID, accession, version, URL);
- source type and date;
- population/model/system;
- method and comparison;
- effect estimate or concrete result;
- limitations and applicability;
- verification status.

## Minimum computational audit trail

- input filenames, accessions, reference build, and checksums when available;
- software and package versions, environment/lockfile, hardware-relevant settings;
- command, parameters, seed, working directory, and timestamp;
- output paths and checksums;
- QC thresholds and reasons;
- warnings, failed attempts, exclusions, and manual edits;
- link between each figure/table and the code/data that produced it.

## Minimum wet-lab planning record

- experimental unit and replicate structure;
- positive, negative, vehicle, mock, and process controls as applicable;
- randomization, blocking, plate/lane/run order, and blinding where feasible;
- reagent lot, instrument, calibration, operator, date, and environmental/batch factors;
- predefined acceptance/exclusion criteria;
- raw-data retention and sample-ID traceability;
- required IRB/IBC/IACUC/EHS/QA approvals.

## Interpretation rules

- Separate exploratory from confirmatory analyses.
- Distinguish technical from biological replication.
- Report effect sizes and uncertainty, not only p-values.
- Treat batch correction as a modeling step, never as a cure for complete confounding.
- Require an independent validation dataset or orthogonal assay for high-impact claims when feasible.
- Preserve null, negative, and contradictory evidence.
