# Domain routing for complete research

Use this map when a deep-research request crosses domains or explicitly asks
for the necessary, related, compatible, or all relevant skills. Select only
roles that contribute distinct work.

| Request evidence | Owning specialist(s) to add | Verification or challenge |
|---|---|---|
| Human clinical effect, diagnosis, treatment, rehabilitation, scientific literature | `research-medical-evidence`; add `physio-clinical-copilot` for an individual FTR case or `physio-study-coach` for course/exam material | `evidence-integrity-guard` |
| Health product, supplement, cream, brace, wearable, device, regulatory or reimbursement claim | `health-product-evidence-check`; add `research-medical-evidence` for effectiveness and `market-pricing-analysis` only when price/value is requested | `evidence-integrity-guard` |
| Stock, fund, ETF, warrant, VİOP, crypto, portfolio action, target, or forecast | `investment-copilot` plus the relevant market/instrument specialist; add `probabilistic-market-forecast` for future ranges | `finance-evidence-guard`; add `investment-red-team` for “emin misin?”, concentrated/high-risk action, or a fresh second opinion |
| Device, OS, mobile/desktop app, peripheral, smart home, compatibility, remote access, or troubleshooting | `personal-tech-copilot`; add `market-pricing-analysis` only for a purchase/value decision | `evidence-integrity-guard` for current specifications, security, or consequential recommendations |
| Product/service price, package, subscription, total cost, or value | `market-pricing-analysis`; add the health or technical specialist when claims cross those domains | `evidence-integrity-guard` |
| A supplied article, report, paper, transcript, long URL, or document that must also be checked against the open web | `deep-reading-analyst` for the supplied content and `deep-research` for external discovery | `evidence-integrity-guard`; add the owning domain specialist |
| Current route, ETA, transit, traffic, opening-hours, or multi-stop travel within a day | `plan-smart-routes` | Current-source verification; add weather or place research only when it changes the route decision |
| Publishable, sourced long-form article or report | `content-research-writer` after research ownership is established | `evidence-integrity-guard` before factual claims enter the draft |
| Company, market, competitor, income opportunity, or commercial trend | Use the narrow installed business/research specialist when one exists; otherwise retain `deep-research` as owner | `evidence-integrity-guard`; treat seller, sponsor, affiliate, and platform claims as interested evidence |

## Conflict rules

- Use `quick-research` or `deep-research` as the research-depth owner, not both,
  unless a bounded quick lookup is a named subtask inside a broader deep review.
- Do not use `bio-research` for human clinical effectiveness merely because a
  mechanism, gene, or protein is mentioned; add it only when molecular or
  cellular biology is itself a distinct question.
- Do not use `market-pricing-analysis` for securities or investment targets.
- Do not use `content-research-writer` for a short email or message.
- Do not use `physio-study-coach` for patient-specific treatment planning.
- A short requested answer changes presentation length, not research depth or
  the required safety checks.

## Handoff record

For a multi-skill research task, keep a compact internal handoff:

| Role | Skill | Distinct question | Required output |
|---|---|---|---|

If two selected skills would answer the same distinct question, keep the more
specific owner and remove the redundant one.
