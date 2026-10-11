# Search Strategy

## Contents

- [Define the review mode](#1-define-the-review-mode)
- [Build the question](#2-build-the-question)
- [Construct the query](#3-construct-the-query)
- [Balance sensitivity and precision](#4-balance-sensitivity-and-precision)
- [Validate the search](#5-validate-the-search)
- [Execute complementary searches](#6-execute-complementary-searches)
- [Keep a reproducible log](#7-keep-a-reproducible-log)
- [Screen without moving the goalposts](#8-screen-without-moving-the-goalposts)

## 1. Define the review mode

| Mode | Suitable request | Minimum documentation |
|---|---|---|
| Targeted lookup | One fact, paper, guideline, DOI, or safety signal | Search terms, sources checked, date |
| Rapid evidence scan | Practical answer under time constraints | PICO/PECO, selected databases, exact core query, limits, key exclusions |
| Structured review | Broad academic or clinical synthesis | Protocol-like criteria, multiple databases, complete log, deduplication, appraisal |
| Scoping review | Map concepts, populations, designs, or gaps | PCC, broad source set, transparent screening and charting |
| Systematic review | Exhaustive predefined review intended for formal use/publication | Protocol/registration where appropriate, information-specialist-quality strategy, full reproducibility, PRISMA/PRISMA-S |

Do not call a rapid scan systematic. State what the chosen mode can and cannot establish.

## 2. Build the question

- **PICO:** Population, Intervention, Comparator, Outcome.
- **PECO:** Population, Exposure, Comparator, Outcome.
- **PCC:** Population, Concept, Context.
- **SPIDER:** Sample, Phenomenon of Interest, Design, Evaluation, Research type.

Create a concept table:

| Concept | Controlled vocabulary | Free-text synonyms | Turkish/local variants | Exclusions only if essential |
|---|---|---|---|---|
| Population/condition | MeSH/Emtree/subject heading | acronyms, old/new names, spelling variants | Turkish names and diacritics | justified exclusions |
| Intervention/exposure | controlled term | generic, brand, technique, dose, device | local names | justified exclusions |
| Outcome/design | usually omit initially if recall would suffer | outcome terms or validated design filter | local terms | justified exclusions |

Do not force every PICO element into the query. Comparator and outcome terms often reduce recall.

## 3. Construct the query

1. Combine synonyms within a concept using `OR`.
2. Combine concepts using `AND`.
3. Use phrase searching, truncation, and proximity only where the database supports them.
4. Combine controlled vocabulary with title/abstract keywords.
5. Inspect automatic term mapping and exploded headings rather than assuming they worked.
6. Use `NOT` rarely; it can silently remove relevant studies.
7. Apply date, language, age, human, or publication-type filters only when justified and document them.

### PubMed pattern

```text
(
  "Condition"[Mesh]
  OR condition*[tiab]
  OR "older term"[tiab]
)
AND
(
  "Intervention"[Mesh]
  OR intervention*[tiab]
  OR synonym*[tiab]
)
```

Useful PubMed fields include `[Mesh]`, `[tiab]`, `[pt]`, `[dp]`, and `[lang]`. Confirm current syntax in the PubMed User Guide. Do not rely on title-only searching unless precision is intentionally prioritized.

### Translate, do not copy

| Platform | Common controlled vocabulary or field form |
|---|---|
| PubMed | MeSH; `[Mesh]`, `[tiab]` |
| Embase | Emtree; `/exp`, `:ti,ab,kw` depending on interface |
| CINAHL/EBSCO | CINAHL Headings; `MH`, `TI`, `AB` |
| Scopus | `TITLE-ABS-KEY(...)` |
| Web of Science | `TS=(...)` |
| Cochrane | MeSH descriptors plus title/abstract/keyword fields |
| PEDro | Advanced Search fields for therapy, problem, body part, subdiscipline, method, and title/abstract |
| TR Dizin / DergiPark / YÖK Thesis | Simpler Turkish and English keyword combinations; use available field filters |

Interfaces change. Verify exact syntax in the live help page before presenting a query as executable.

### PEDro search card

Use [PEDro Advanced Search help](https://pedro.org.au/english/learn/search-help/) rather than PubMed syntax:

- Search English terms in **Abstract & Title**; add only decision-relevant therapy, problem, body-part, subdiscipline or method fields. Start broad rather than filling every field.
- Do not type literal `AND`, `OR`, `NOT`, MeSH tags or PubMed parentheses into free-text fields. Words in one field are combined with implicit AND.
- Select **Match all search terms (AND)** or **Match any search term (OR)** to combine fields. PEDro cannot mix both operators in one query.
- To emulate a synonym block plus a condition, run separate queries and merge/deduplicate their records. For example, search `"low back pain" exercise*`, then `"low back pain" "motor control"`; log each query and all chosen fields. This is an illustrative starting point, not a validated complete strategy.
- Quotation marks match a phrase; `*` expands word variants and `@` replaces one character. Do not place a wildcard inside a quoted phrase.
- Check result pages and source update dates. PEDro's relevance/score ordering is not a filter for clinical benefit; do not screen only the first page or high-score trials.
- Test sentinel records and relax phrase/field restrictions if relevant studies are missed. Verify the live interface before execution.

## 4. Balance sensitivity and precision

Create two variants when useful:

- **Sensitive:** broad synonyms, controlled vocabulary, minimal filters; use for systematic or safety searches.
- **Precise:** core concepts plus justified fields or validated design filters; use for quick triage.

Use validated search filters from authoritative sources for RCTs, diagnostic studies, or other designs. Do not invent a methodological filter. For systematic reviews, avoid filters that exclude newly indexed or incompletely tagged records unless tested.

## 5. Validate the search

- Identify sentinel studies from trusted reviews, guidelines, expert-provided citations, or scoping searches.
- Confirm that the strategy retrieves the sentinel set.
- Inspect a sample of relevant and irrelevant results.
- Add missed terminology and remove only demonstrably noisy terms.
- For formal reviews, consider independent peer review of the strategy using PRESS principles.

## 6. Execute complementary searches

- Run the database-specific strategies.
- Search references of included studies and strong reviews.
- Search forward citations in a citation database.
- Use similar-article tools.
- Search trial registries, review registries, theses, and preprints when unpublished evidence matters.
- Search corrections, retractions, and later versions.
- Stop according to the predefined mode, not because the first plausible answer appeared.

### Use an explicit stopping rule

- For a targeted or rapid scan, complete the predefined core database set, one complementary discovery/citation source, and the relevant registry when unpublished evidence matters.
- Perform at least one backward- and forward-citation pass on the key eligible papers.
- Stop after a documented second search/citation iteration produces no new eligible or conclusion-changing evidence, or when the agreed time limit is reached.
- State that this is a pragmatic saturation rule, not proof of exhaustive retrieval.
- For a systematic review, follow the protocol and database plan; do not replace exhaustive methods with a saturation shortcut.

### Export and deduplicate when the corpus is material

- Preserve raw database exports in a standard format such as RIS, NBIB, BibTeX, or CSV when available.
- Retain source and search-date fields before merging.
- Deduplicate with a reference manager, review platform, or transparent script using DOI/PMID first, then normalized title, year, and author checks.
- Review uncertain matches manually and preserve the deduplication rule and counts.
- If the active environment cannot export or deduplicate, state the limitation and provide exact user-executable steps instead of claiming completion.

## 7. Keep a reproducible log

```markdown
| Database | Platform/provider | Exact query | Date searched | Limits/sort | Total found | Retrieved | Reviewed | Access/issues |
|---|---|---|---|---|---:|---:|---:|---|
| PubMed | PubMed direct | ... | YYYY-MM-DD | none | 123 | 123 | 123 | complete records; full-text access logged separately |
```

Also record:

- inclusion and exclusion criteria;
- duplicate-removal method;
- screening counts and reasons for full-text exclusion;
- unavailable full texts;
- hand-searching and citation-chasing steps;
- deviations from the original plan.

For publication-quality reviews, preserve a PRISMA flow and follow the current PRISMA-S reporting guidance.

## 8. Screen without moving the goalposts

- Apply criteria defined before seeing the results.
- Separate title/abstract screening from full-text eligibility.
- Do not exclude a paper merely because its result conflicts with the emerging conclusion.
- Link companion papers and avoid double-counting the same participant cohort.
- Translate non-English records when feasible rather than silently discarding them.
- Mark unresolved eligibility decisions and their potential impact.
- For a formal systematic review, use at least two independent qualified human reviewers for final full-text eligibility, with a predefined disagreement-resolution process. AI may assist triage/extraction; two AI agents do not replace independent human reviewers. If this is unavailable, deliver a review draft and flag the unmet requirement. See [Cochrane Handbook chapter 4](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04).
