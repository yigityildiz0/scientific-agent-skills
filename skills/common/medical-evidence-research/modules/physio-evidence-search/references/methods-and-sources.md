# Evidence-search methods and source map

> Method status checked 2026-07-22. Verify live versions and publication status during every current search.

## Question structures

- **Intervention:** population, intervention, comparator, outcomes; add time, setting, and study design when decision-relevant.
- **Diagnostic accuracy:** population, index test, reference standard, target condition, intended role, threshold, and setting.
- **Prognosis:** population, prognostic factor/model, outcomes, time horizon, and setting.
- **Etiology/exposure:** population, exposure, comparator, outcomes, time.
- **Measurement:** construct, population, intended use, setting, language/version, and measurement property.

The review question, each synthesis question, and the actual PICO of included studies may differ. Make the differences visible.

## Source hierarchy by purpose

### Guidelines and health-system recommendations

- WHO, NICE, national health ministries, VA/DoD, and relevant regulator or public-health agency.
- World Physiotherapy and professional-society clinical practice guidelines.
- Guideline International Network for discovery; open the issuing organization's source.
- Use AGREE II for development quality when needed. A guideline recommendation is not automatically correct or locally applicable.

### Intervention effectiveness and dose

- Cochrane Database of Systematic Reviews and current systematic reviews in PubMed/MEDLINE.
- PEDro, CENTRAL, and PubMed/MEDLINE for trials.
- Embase, CINAHL, SPORTDiscus, PsycINFO, and Scopus/Web of Science when available and relevant.
- ClinicalTrials.gov and WHO ICTRP for ongoing, unpublished, or selectively reported work.

### Prognosis, harms, and real-world implementation

- Cohort, registry, surveillance, qualitative, and implementation studies as the question requires.
- Do not exclude non-randomized evidence for rare or long-term harms merely because RCTs exist.
- `No adverse events reported` does not mean safe. Check definitions, active/passive ascertainment, denominator, follow-up, severity, withdrawals, and exclusion of high-risk people.

### Measurement and diagnosis

- COSMIN tools/database and COMET core outcome set database.
- PubMed/MEDLINE and, when available, Embase/CINAHL.
- Rehabilitation Measures Database only for discovery; verify numbers in original studies and official instrument materials.

## Authoritative method links

- [PubMed help and syntax](https://pubmed.ncbi.nlm.nih.gov/help/)
- [PEDro](https://pedro.org.au/)
- [Cochrane Library](https://www.cochrane.org/products-and-services/cochrane-library)
- [Cochrane Handbook, current version](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current)
- [GRADE Book](https://book.gradepro.org/)
- [ClinicalTrials.gov](https://clinicaltrials.gov/)
- [WHO ICTRP](https://trialsearch.who.int/)
- [NICE guidance](https://www.nice.org.uk/guidance)
- [APTA clinical practice guidelines](https://www.apta.org/patient-care/evidence-based-practice-resources/cpgs)
- [VA/DoD rehabilitation guidelines](https://www.healthquality.va.gov/HEALTHQUALITY/guidelines/Rehab/index.asp)
- [WHO Package of Interventions for Rehabilitation](https://www.who.int/publications/i/item/9789240067097)

Search engines, Google Scholar, citation maps, and AI summaries may support discovery; they are not final evidence sources.

## Search construction

Build concept blocks with controlled vocabulary and free text:

```text
(population terms) AND (intervention/index terms) AND (outcome/design terms only when useful)
```

Avoid unnecessary outcome terms when they reduce recall. Document every filter. Expand a failed query stepwise and record what changed.

For PEDro, use English Abstract & Title terms with optional advanced fields. Do not type Boolean words or MeSH tags into text fields: words in one field use implicit AND, and the Match all/Match any control combines fields. Mixed AND/OR is unavailable; execute separate synonym queries and merge. Quoted phrases cannot contain wildcards. Verify [PEDro search help](https://pedro.org.au/english/learn/search-help/) and test sentinel records before treating a query as complete.

Record database and actual retrieval provider separately; a PubMed-linked OpenAlex search is not a direct PubMed search. Distinguish total matches, retrieved records and reviewed records; follow the pages and clipped-text continuations required by the declared scope. State caps and inaccessible sources explicitly.

## Certainty and effect rules

- Assess certainty for each critical outcome: risk of bias, inconsistency, indirectness, imprecision, and missing/publication bias; use upgrading domains only when justified.
- Do not equate certainty with recommendation strength. Benefits, harms, values, burden, resources, equity, acceptability, and feasibility also matter.
- For binary outcomes, report baseline risk, relative effect, absolute difference, and time horizon.
- For continuous outcomes, use MD for the same scale and SMD when scales differ; explain direction and, when defensible, a natural-unit or important-change interpretation.
- Do not convert a group mean difference into the percentage of individual responders without valid responder data.
- Do not use I² alone as a heterogeneity decision rule. Consider clinical/methodological diversity, τ², direction, and prediction interval when available.
- Funnel asymmetry is not proof of publication bias; small-study tests are usually uninformative with few studies.

## Recency and publication status

- Find the last search date of every synthesis, not only its publication date.
- Search forward for newer primary studies and label them as an update layer.
- Verify DOI/PMID, version, correction, retraction, expression of concern, and preprint status.
- Use [NLM errata/retraction policy](https://www.nlm.nih.gov/bsd/policy/errata.html) and [Crossmark](https://www.crossref.org/services/crossmark/) when appropriate.

## Clinical translation fields

For every actionable intervention, extract:

`problem → intervention → target outcome → evidence → patient match → dose provenance → progression/regression → stop rules → monitoring → harms → burden/resources`

If a component is not reported, write **not reported**. Never fill the gap with a guessed number.

