---
name: bioscience-research-router
description: Routes life-science work across scientific strategy, literature review, experimental design, molecular-genetics assay planning, RStudio reproducible analysis, R data wrangling, R biostatistics, bulk RNA-seq differential expression (DESeq2), ggplot2 figures, Quarto reporting, academic presentations, research synthesis, knowledge organization, single-cell QC, scvi-tools, and nf-core/Nextflow workflows. Use for wet-lab, molecular genetics, bioinformatics, omics, laboratory data, R or RStudio analysis, statistics and modeling, data cleaning and joins, publication figures, scientific report writing, thesis or conference talks, research planning, evidence synthesis, or U.S. research-compliance questions where reproducibility, provenance, privacy, biosafety, IRB/IBC, GLP, or GMP boundaries matter.
---

# Bioscience Research Router

Route the task to the smallest sufficient scientific workflow, then enforce evidence, reproducibility, privacy, and human-review gates.

## Route the work

| Need | Primary skill | Combine with |
|---|---|---|
| Choose or rescue a research problem | `scientific-problem-selection` | `scientific-literature-review`, `experimental-design` |
| Review biomedical evidence | `scientific-literature-review` | shared `deep-research` when available |
| Plan controls, randomization, blocks, batches, or DOE | `experimental-design` | statistics/power skill from the shared master when needed |
| Design or validate PCR/qPCR primers or probes | `molecular-genetics-assay-planning` | `scientific-literature-review` for assay evidence |
| Set up or repair an RStudio project, renv, or a clean reproducible run | `rstudio-reproducible-analysis` | `quarto-authoring` for the report |
| Clean, join, reshape, or validate lab/omics tables in R | `r-bioscience-data-wrangling` | `rstudio-reproducible-analysis` |
| Choose, fit, diagnose, and report an R statistical model or contrast | `r-biostatistics-workflow` | `experimental-design`, `r-bioscience-data-wrangling` |
| Bulk RNA-seq differential expression from a count matrix | `bio-differential-expression-deseq2-basics` | `r-biostatistics-workflow`; `nextflow-development` upstream |
| Publication-quality figures in R with ggplot2 | `bio-data-visualization-ggplot2-fundamentals` | `r-biostatistics-workflow` first |
| Reproducible scientific report (`.qmd`) with code, tables, and citations | `quarto-authoring` | `rstudio-reproducible-analysis` |
| Thesis defense, seminar, lab meeting, grant, or conference presentation | `academic-presentations` | `bio-data-visualization-ggplot2-fundamentals`, `scientific-literature-review` |
| Synthesize interviews, notes, findings, or mixed evidence | `research-synthesis` | `scientific-literature-review` for source-backed literature |
| Organize durable paper, method, protocol, or project notes | `knowledge-base` | `quarto-authoring` for reproducible reports |
| QC `.h5ad` or 10x `.h5` single-cell RNA data | `single-cell-rna-qc` | `scvi-tools` after QC |
| Integrate or model single-cell/multiome data | `scvi-tools` | `single-cell-rna-qc` first |
| Run reproducible RNA-seq, WGS/WES, or ATAC-seq pipelines | `nextflow-development` | `experimental-design`, literature review |
| Check U.S. IRB/IBC/GLP/GMP/FDA context | this skill | read `references/regulatory-routing.md` |

Do not invoke every skill. Use one primary skill and only the supporting skills that close an identified gap.

## Scientific execution contract

1. State the scientific question, biological unit, sample type, organism, reference build, data modality, and intended decision.
2. Separate raw data, derived data, code, parameters, and interpretation. Never overwrite raw data; work on a copy and preserve identifiers or checksums.
3. Record controls, biological versus technical replicates, randomization, blocking, batch structure, exclusion rules, and planned statistics before interpreting results.
4. Verify actual tool and package versions before using examples. Pin an exact tested version for reproducible runs; do not silently upgrade a working pipeline.
5. Run a small validation or test profile before full data. Preserve logs, commands, seeds, environment information, and failure messages.
6. Report evidence, assumptions, uncertainty, alternatives, and validation status separately. Label hypotheses and preprints explicitly.
7. Require a qualified human to approve biological interpretation, wet-lab execution, regulated decisions, clinical relevance, and publication claims.

Read `references/evidence-and-reproducibility.md` for the evidence hierarchy and minimum audit trail.

## Privacy and external systems

- Treat unpublished sequences, patient-linked data, sample identifiers, credentials, and institutional records as sensitive.
- Prefer local processing. Do not upload sensitive or controlled data to a third-party service without explicit authorization and the institution's approved data-use path.
- Remove direct identifiers and unnecessary metadata before sharing. De-identification does not itself prove HIPAA or institutional compliance.
- Use public accession downloads only after confirming the accession and intended dataset. Record the source URL, accession, retrieval date, and checksum when available.

## Safety and compliance boundary

- Provide scientific and regulatory source navigation, not medical, legal, biosafety, IRB, IBC, GLP, GMP, or quality-unit approval.
- Do not decide whether an activity is exempt, compliant, safe, diagnostic, or ready for clinical/manufacturing use.
- For human participants or identifiable biospecimens, stop at a draft/research plan and route the decision to the institution's IRB/privacy office.
- For recombinant or synthetic nucleic acids, engineered organisms, viral vectors, pathogens, toxins, or uncertain containment, route the protocol to the institutional IBC/EHS/biosafety officer before execution.
- For animal work, route design and procedures to the institution's IACUC/veterinary oversight.
- For regulated nonclinical or manufacturing work, distinguish research guidance from controlled SOPs and route final decisions to QA/regulatory professionals.

Read `references/regulatory-routing.md` whenever any regulated trigger appears.

## Deliverable

Return a compact research packet:

- question and scope;
- selected workflow and why;
- inputs and provenance;
- analysis or experiment plan;
- controls and validation gates;
- evidence table with citations;
- assumptions, uncertainties, and alternatives;
- human approvals or institutional reviews required;
- reproducibility record and next safe action.
