# Appraisal and Synthesis

## Contents

- [Match the tool to the design](#match-the-tool-to-the-design)
- [Extract what changes interpretation](#extract-what-changes-interpretation)
- [Rehabilitation-specific checks](#rehabilitation-specific-checks)
- [Synthesize without vote counting](#synthesize-without-vote-counting)
- [Grade certainty](#grade-certainty)
- [Use precise evidence language](#use-precise-evidence-language)
- [Evidence table](#evidence-table)
- [Synthesis order](#synthesis-order)

## Match the tool to the design

| Evidence type | Suitable appraisal approach |
|---|---|
| Randomized trial | Cochrane RoB 2; PEDro scale as an additional physiotherapy-oriented indicator |
| Non-randomized intervention | ROBINS-I |
| Systematic review of healthcare intervention effects | AMSTAR 2 for methods; ROBIS for review-level risk of bias |
| Other systematic review | Purpose/design-specific methods and compatible ROBIS guidance; do not apply AMSTAR 2 automatically |
| Diagnostic accuracy | QUADAS-3 (current official version; verify the live version and guidance before formal use) |
| Prediction model | PROBAST+AI for prediction models using regression or AI methods; use TRIPOD+AI for reporting, not as a risk-of-bias substitute |
| Prognostic-factor study | QUIPS |
| Qualitative study | CASP or JBI design-specific checklist |
| Prevalence/cross-sectional/cohort/case-control | JBI or another design-specific critical-appraisal tool |
| Clinical guideline | AGREE II |

Use the current official version and domain guidance. For diagnostic accuracy, verify against the [QUADAS official site](https://www.bristol.ac.uk/population-health-sciences/projects/quadas/); for prediction models, verify against the [PROBAST official site](https://www.probast.org/). Reporting standards such as CONSORT, STROBE, PRISMA, CARE, and TRIPOD+AI improve reporting but are not substitutes for risk-of-bias assessment.

## Extract what changes interpretation

For each study, capture:

- citation, DOI/PMID/registry ID, publication and peer-review status;
- design, setting, recruitment dates, sample size, eligibility, baseline differences;
- intervention or exposure details, dose, frequency, duration, adherence, co-interventions;
- comparator and treatment fidelity;
- prespecified primary and secondary outcomes and time points;
- effect estimate, unit, denominator, confidence interval, p-value when relevant;
- absolute as well as relative effects when possible;
- missing data, attrition, crossovers, protocol deviations, multiplicity;
- harms, adverse events, withdrawals, and follow-up duration;
- funding, author conflicts, protocol/registration, and deviations;
- applicability to the user's population and setting.

Do not extract only the abstract's conclusion.

### Compare groups, not separate p-values

- Extract the prespecified between-group effect (or appropriate group-by-time contrast), its confidence interval, time point and adjustment. A significant pre/post improvement in one group and a non-significant improvement in another do not establish a significant between-group difference.
- Within-group change may reflect natural recovery, regression to the mean, expectation or co-interventions. Do not use it alone to claim treatment superiority.
- Interpret clinical importance against an appropriate population/scale threshold; an individual-change MIC/MCID is not automatically a between-group threshold. Keep reporting completeness, bias, effect size, certainty and patient applicability separate.

Use [AMSTAR 2's official guidance](https://amstar.ca/Amstar-2.php) for intervention reviews; judge critical domains rather than summing a quality score.

### Interpret null and equivalence claims correctly

- Failure to reject the null hypothesis is not proof of equivalence or absence of harm.
- For a “no difference” conclusion, check whether non-inferiority or equivalence was prespecified, whether the margin was clinically justified, and whether the confidence interval excludes important benefit and harm.
- Check the sample-size calculation, event count, attrition, adherence, follow-up, and expected effect size.
- Describe an underpowered negative trial as **no clear signal detected within this study's limits**, not as proof of no effect.

## Rehabilitation-specific checks

- Determine whether the intervention is described well enough to reproduce using TIDieR, CERT, or a current rehabilitation-specific reporting guide.
- Examine therapist training, expertise, treatment individualization, progression rules, adherence, home-program monitoring, and contamination.
- Interpret blinding in context: participant or therapist blinding may be impossible, but blinded outcome assessment and allocation concealment may still matter.
- Check comparator intensity. “Usual care” can vary greatly.
- Compare outcomes with the minimal clinically important difference when a credible population-specific threshold exists.
- Separate short-term impairment change from activity, participation, quality of life, durability, and adverse effects.

## Synthesize without vote counting

Weigh:

1. risk of bias;
2. directness to the target population, intervention, comparator, and outcome;
3. consistency of effect direction and magnitude;
4. precision and information size;
5. selective reporting and publication bias;
6. dose, adherence, follow-up, and clinical importance.

Explain heterogeneity through populations, interventions, comparators, outcomes, follow-up, methods, and bias. Do not average fundamentally incompatible studies merely to produce a number.

## Grade certainty

Use GRADE for outcome-level certainty when the task warrants it:

- high;
- moderate;
- low;
- very low.

Explain each downgrade or upgrade. Do not assign certainty from study design alone. If a formal GRADE assessment is not feasible, use plain-language confidence and state why.

## Use precise evidence language

| Evidence state | Preferred wording |
|---|---|
| Consistent direct evidence with adequate certainty | “Evidence indicates…” |
| Limited, imprecise, or biased evidence | “Evidence suggests, but confidence is limited…” |
| Conflicting evidence | “Results are inconsistent…” |
| Only mechanistic, animal, or surrogate evidence | “This is biologically plausible but not established clinically…” |
| Search found no eligible direct studies | “No direct eligible evidence was found in the searched sources…” |
| Adequate evidence shows little or no important effect | “Evidence indicates little or no clinically important effect…” |

Never turn “not statistically significant” into “no effect,” or “no evidence found” into proof of safety.

## Evidence table

```markdown
| Study | Design/sample | Exposure or intervention | Comparator | Key effect (95% CI) | Follow-up | Main bias/limit | Relevance |
|---|---|---|---|---|---|---|---|
```

## Synthesis order

1. Give the practical bottom line.
2. State confidence/certainty.
3. Summarize the few studies driving the conclusion.
4. Explain contradictions, indirectness, harms, and applicability.
5. State what is unknown and what new evidence would change the answer.
6. Attach exact citations and the search boundary.
