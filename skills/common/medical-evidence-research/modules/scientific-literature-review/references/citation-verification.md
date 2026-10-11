# Citation verification

Verify each reference before delivery.

## Verification order

1. Resolve DOI through `https://doi.org/<doi>` or Crossref.
2. Verify PMID/PMCID in PubMed/PMC for biomedical records.
3. Match title, authors, journal, year, volume/issue/pages or article number.
4. Confirm the cited claim is supported by the accessible abstract/full text/supplement.
5. Check for correction, retraction, expression of concern, updated version, or preprint-to-journal transition.

## Stable identifier rules

- Prefer DOI plus PMID/PMCID where applicable.
- Preserve dataset accession and software/version identifiers separately from paper citations.
- Do not use a search-result URL as the sole citation when a stable record exists.
- Do not guess missing metadata. Mark it unresolved.

## Claim-citation audit

For each material sentence ask:

- Does this citation support this exact claim?
- Is it the primary source or merely repeating another source?
- Is the population/model/assay the same as the claim?
- Is the evidence causal, associative, mechanistic, or speculative?
- Are numerical values and units copied accurately?

If verification fails, remove or qualify the claim rather than preserving a plausible-looking citation.

For systematic or scoping reviews, use the current [PRISMA 2020 resources](https://www.prisma-statement.org/home) as reporting guidance and preserve a flow record; PRISMA is not itself a risk-of-bias tool.
