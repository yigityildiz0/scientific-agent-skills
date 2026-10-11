# Claim and evidence protocol

## Claim ledger

For each decision-relevant claim, preserve these fields internally:

| Field | Requirement |
| --- | --- |
| `claim` | One atomic proposition, including population/item, condition, outcome, and time when relevant |
| `type` | `FACT`, `CALCULATION`, `INFERENCE`, `FORECAST`, or `UNKNOWN` |
| `importance` | `DECISIVE`, `MATERIAL`, or `BACKGROUND` |
| `source` | Publisher, title, URL or stable identifier, and exact locator |
| `date` | Publication/update date and access date; data cutoff if different |
| `identity` | Exact person, product, instrument, version, population, jurisdiction, units, and currency |
| `origin` | Primary evidence, independent synthesis, issuer/seller claim, or copied/syndicated material |
| `incentive` | Funding, sponsor, affiliate, seller, issuer, advocacy, or unknown conflict |
| `entailment` | `DIRECT`, `PARTIAL`, `CONTEXT_ONLY`, or `NONE` |
| `status` | `VERIFIED`, `SUPPORTED`, `MIXED`, `WEAK`, `UNVERIFIED`, or `CONTRADICTED` |

## Status meanings

- `VERIFIED`: exact identity and claim are directly supported by suitable primary or authoritative evidence and any required arithmetic was reproduced.
- `SUPPORTED`: strong evidence supports the claim, but some context, independence, or completeness limitation remains.
- `MIXED`: credible evidence points in different directions or effects vary materially by population, method, time, or scenario.
- `WEAK`: evidence is indirect, small, biased, outdated, or dominated by interested sources.
- `UNVERIFIED`: the necessary source or identity could not be checked.
- `CONTRADICTED`: better evidence conflicts with the claim.

Only `VERIFIED` or appropriately qualified `SUPPORTED` claims may carry high confidence. A source can be real while its use is still wrong.

## Entailment test

For every citation ask:

1. Does it concern the exact entity, version, population, and jurisdiction?
2. Does it report the asserted outcome, rather than a surrogate or related measure?
3. Does it support association or causation at the strength used in the answer?
4. Does it support the magnitude, direction, timeframe, and certainty stated?
5. Is the cited location actually present in the inspected source?

If any answer is no, narrow the claim or change the evidence status.

## Independence test

Trace claims back to their origin. Ten pages copying the same press release are one source. A news report quoting a study and the study itself are not independent evidence for the result. Use independent confirmation only when the second source gathered or analyzed evidence separately.

## Contradiction pass

Before finalizing a consequential answer, search for:

- official corrections, retractions, withdrawals, recalls, or enforcement;
- later or larger primary studies and systematic reviews;
- adverse outcomes and null results;
- incompatible dates, versions, units, or definitions;
- base-rate explanations and selection or survivorship bias;
- the strongest reasonable case against the preferred conclusion.

State whether contradictions change the conclusion, reduce confidence, or merely bound applicability.

## Stop conditions

Do not issue a reliance-grade conclusion when exact identity is unresolved, decisive current evidence cannot be accessed, calculations cannot be reproduced, or a material contradiction remains unexplained. Give the best conditional result and the exact verification needed next.
