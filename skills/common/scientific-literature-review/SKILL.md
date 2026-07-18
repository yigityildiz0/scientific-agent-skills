---
name: scientific-literature-review
description: Produces traceable biomedical and life-science literature searches, evidence maps, narrative reviews, scoping reviews, and systematic-review drafts with verified citations. Use for PubMed/MeSH searches, research-gap analysis, evidence synthesis, citation checking, review protocols, PRISMA-style reporting, or literature sections where primary sources, exact search strings, deduplication, screening criteria, and uncertainty must be preserved.
---

# Scientific Literature Review

Build a reproducible evidence trail. Do not generate a polished narrative first and search for citations afterward.

## Choose the review mode

| Mode | Use when | Minimum output |
|---|---|---|
| Rapid evidence map | Time is limited; landscape and gaps matter | search log, source table, themes, gaps |
| Narrative review | Explain a field without claiming exhaustive coverage | scoped search, representative primary evidence, limitations |
| Scoping review | Map concepts, methods, or evidence types broadly | protocol, reproducible search, screening ledger, charted evidence |
| Systematic review | A focused question needs comprehensive, auditable selection | protocol, multi-database search, deduplication, dual/human screening plan, risk-of-bias plan, PRISMA records |
| Meta-analysis support | Comparable effect estimates exist | systematic-review foundation plus statistical protocol and human statistician review |

Never call a review “systematic” merely because many sources were read.

## Workflow

1. Frame the question with the appropriate structure: PICO/PECO for intervention or exposure, PCC for scoping, or a mechanistic question with explicit model, perturbation, comparator, and outcome.
2. Predefine dates, languages, study types, populations/models, outcomes, inclusion/exclusion criteria, and treatment of preprints. Record deviations.
3. Build concept blocks with synonyms, gene/protein aliases, controlled vocabulary, and spelling variants. Read `references/database-search.md`.
4. Search PubMed plus at least one complementary database appropriate to the topic. Preserve the exact query, database, filters, search date, result count, and PubMed Search Details/translation.
5. Export stable identifiers and deduplicate by DOI, PMID/PMCID, accession, then normalized title/author/year. Keep a duplicate-resolution log.
6. Screen title/abstract and then full text against the predefined criteria. For publication-grade or regulated work, a qualified human owns inclusion decisions and conflict resolution.
7. Extract study design, model/population, sample size, intervention/exposure, comparator, outcome, effect estimate, uncertainty, methods, funding/conflicts, and limitations into an evidence table.
8. Appraise evidence using a method appropriate to the study design; do not invent a universal score. Read `references/evidence-appraisal.md`.
9. Verify every citation against a primary bibliographic record before delivery. Read `references/citation-verification.md`.
10. Synthesize by evidence pattern, not paper-by-paper summary. Separate replicated findings, contested findings, methodological causes of disagreement, gaps, and inference.

Use the shared `deep-research` skill for parallel discovery when available, but retain this skill's scientific search log, source hierarchy, screening, and verification rules.

## Non-negotiable quality rules

- Prefer primary papers for scientific claims; use reviews to orient and discover primary evidence.
- Label preprints, conference abstracts, retractions, corrections, and expressions of concern.
- Never infer full-text results from an abstract or search snippet.
- Quote sparingly and preserve the source's meaning; do not transform correlation into causation.
- Do not fabricate DOI, PMID, author, journal, year, sample size, effect, or quotation.
- Distinguish no evidence found from evidence of no effect.
- Report search and access limitations, unavailable full texts, and unsearched databases.
- Do not claim PRISMA compliance unless every applicable checklist item and flow record is complete; otherwise say “PRISMA-informed.”

## Deliverable

Return:

1. question, review mode, scope, and protocol summary;
2. exact search log;
3. inclusion/exclusion and screening summary;
4. evidence table with stable identifiers;
5. synthesis with confidence and contradictory evidence;
6. limitations, gaps, and recommended next searches/experiments;
7. verified references;
8. reproducibility appendix with search date and tool/database versions when available.
