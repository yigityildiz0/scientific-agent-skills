# Biomedical database search

## PubMed baseline

Build concept blocks and combine synonyms with `OR`, then blocks with `AND`.

```text
("gene alias"[tiab] OR "protein name"[tiab] OR "MeSH term"[mh])
AND
(disease[tiab] OR disease[mh])
AND
(assay[tiab] OR technique[mh])
```

Use field tags deliberately. Field tags disable or constrain automatic term mapping, so inspect PubMed **Search Details** and save the translated query. Useful tags include `[tiab]`, `[mh]`, `[majr]`, `[pt]`, `[dp]`, `[au]`, `[ad]`, and `[pmid]`.

Official reference: [PubMed User Guide](https://pubmed.ncbi.nlm.nih.gov/help/).

## Complementary databases

Select by question, not convenience:

- PubMed/MEDLINE: biomedical literature and MeSH.
- Europe PMC: biomedical papers, preprints, grants, and open full text.
- Web of Science or Scopus: citation-indexed breadth when institutionally available.
- Embase: drug/clinical and conference coverage when licensed.
- bioRxiv/medRxiv: preprints; always label as non-peer-reviewed.
- ClinicalTrials.gov: registered interventional/observational studies; registration is not proof of result.
- GEO/SRA/ENA: public functional-genomics datasets; record accession and retrieval date.
- Crossref: bibliographic metadata and DOI resolution, not scientific quality appraisal.

## Search log fields

Record one row per query:

| Database | Interface/API | Exact query | Filters | Search date | Result count | Export format | Notes |
|---|---|---|---|---|---:|---|---|

When using NCBI E-utilities, identify the tool and email, respect current rate limits, keep credentials in environment variables, and follow the current [NCBI E-utilities documentation](https://www.ncbi.nlm.nih.gov/books/NBK25497/).

## Search expansion and stopping

Use backward references, forward citations, related-article search, author searches, and registry/accession links to expand. Stop only when the predefined protocol is satisfied or when additional searches no longer add eligible concepts/studies; document the stopping rule.
