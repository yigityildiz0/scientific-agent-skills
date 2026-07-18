---
name: molecular-genetics-assay-planning
description: Plans and validates research-use PCR, RT-PCR, qPCR, and probe assays with explicit target/isoform/reference-build provenance, primer3 candidate design, pair-aware genome/transcriptome specificity checks, thermodynamic screening, and empirical validation gates. Use for primer or probe design, qPCR assay planning, pseudogene/paralog/off-target checks, SNP-at-primer-site review, hairpin/dimer analysis, or troubleshooting assay specificity and efficiency. Not for autonomous clinical diagnostic claims or unreviewed wet-lab execution.
---

# Molecular Genetics Assay Planning

Treat the assay as a measurement system, not as a pair of plausible oligos. In-silico design narrows candidates; it never replaces empirical validation.

## Define the assay before designing

Record:

- research question and intended readout;
- organism and exact genome assembly/reference build;
- target gene, stable ID, transcript/isoform, exon structure, and strand;
- template type (genomic DNA, cDNA, amplicon, plasmid) and sample matrix;
- assay type (endpoint PCR, RT-PCR, SYBR qPCR, hydrolysis probe, genotyping);
- intended amplicon, required junction/variant/region, and excluded regions;
- known paralogs, pseudogenes, repetitive regions, common variants, and sample population;
- actual reaction chemistry/conditions for thermodynamic calculations.

Do not invent a sequence, accession, assembly, transcript, or reaction condition. Resolve ambiguity against an authoritative database or ask for the missing record.

## Route the workflow

1. **Candidate design** — Read `references/primer-design.md`; use Primer3/primer3-py as a local candidate optimizer, not a specificity oracle.
2. **Genome/transcriptome specificity** — Read `references/specificity.md`; use pair-aware in-silico PCR on the correct assembly. Plain single-primer BLAST is exploratory only.
3. **Hairpin and dimer screening** — Read `references/thermodynamic-validation.md`; calculate at the actual monovalent salt, Mg²⁺, dNTP, oligo concentration, and annealing temperature.
4. **qPCR/probe design** — Read `references/qpcr-design.md`; treat amplification efficiency, single-product specificity, reference-gene stability, and standard-curve validation as required evidence.

The longer usage notes are in `references/primer-basics-usage.md`, `references/primer-specificity-usage.md`, `references/primer-validation-usage.md`, and `references/qpcr-primers-usage.md`.

## Deterministic examples

Use the bundled scripts only after verifying `primer3-py` is installed and its API matches the examples:

- `scripts/primer_design.py` — candidate pair design and ranking;
- `scripts/three_prime_anchor.py` — illustrates why 3′ anchoring matters;
- `scripts/validate_primers.py` — hairpin/dimer and pair-Tm checks;
- `scripts/qpcr_design.py` — primer/probe co-design example.

The scripts contain demo sequences. Replace them only in a working copy; preserve the source accession and all parameters in the result record.

## Validation gates

- Verify the intended amplicon sequence and orientation.
- Search the relevant genome and, for RNA assays, the transcriptome; include alternate/unplaced contigs when scientifically relevant.
- Check paralogs, pseudogenes, repetitive regions, and common variants—especially at 3′ primer bases.
- Evaluate the primer pair together: orientation, spacing, product size, and 3′ anchoring.
- Check hairpins, self-dimers, cross-dimers, and 3′-extendable dimers at actual reaction conditions.
- For qPCR, validate a single product, melt curve or probe specificity, efficiency across the intended range, no-template and no-RT controls as applicable, and stable reference genes.
- Confirm performance empirically on representative positive and negative samples before relying on the assay.
- For clinical, regulated, human-subject, recombinant-DNA, or biosafety-sensitive use, route the plan to the appropriate qualified laboratory, IRB/IBC/EHS, QA, and regulatory owners.

## Deliverable

Return:

1. target and reference provenance;
2. candidate table with sequences, orientation, Tm, GC, product size, and design penalty;
3. pair-aware specificity results and databases/assemblies searched;
4. thermodynamic flags at stated conditions;
5. common-variant and pseudogene/paralog findings;
6. empirical validation plan and acceptance criteria;
7. assumptions, unresolved risks, and “research use only” boundary where applicable.

Never label an assay diagnostic, validated, specific, or fit for regulated use solely from in-silico output.
