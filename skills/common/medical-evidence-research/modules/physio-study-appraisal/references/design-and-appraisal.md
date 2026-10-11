# Design-specific appraisal map

> Method status checked 2026-07-22. Verify the official tool version during each appraisal.

## Choose by actual design and target result

| Design/document | Risk-of-bias or methodological assessment | Reporting guidance |
|---|---|---|
| Parallel RCT | RoB 2 | CONSORT 2025 |
| Cluster/crossover RCT | Relevant RoB 2 variant | Relevant CONSORT extension |
| Non-randomized intervention effect | ROBINS-I | STROBE |
| Diagnostic accuracy estimate | QUADAS-3 | STARD |
| Prognostic factor | QUIPS | STROBE |
| Diagnostic/prognostic prediction model | PROBAST+AI (current official version) | TRIPOD+AI |
| Measurement-property study | COSMIN Risk of Bias | Relevant COSMIN reporting guidance |
| Systematic review of intervention effects | AMSTAR 2 for methods; ROBIS for review-level bias | PRISMA 2020 + PRISMA-S |
| Systematic review of prognostic-factor studies | AMSTAR-PF; use a compatible review-level bias method | PRISMA 2020 + appropriate extension |
| Other systematic review | ROBIS and a purpose/design-specific method; do not apply AMSTAR 2 automatically | PRISMA 2020 + appropriate extension |
| Clinical practice guideline | AGREE II; consider AGREE-REX for recommendations | RIGHT |
| Qualitative study | Appropriate JBI/CASP or epistemologically aligned method | Relevant EQUATOR guidance |

Do not force a near-looking tool onto an incompatible design. ROBINS-I is for non-randomized intervention-effect estimates, not every cohort.

## Live version safeguards

- [RoB 2](https://www.riskofbias.info/welcome/rob-2-0-tool/current-version-of-rob-2) evaluates a specified result, not a whole paper in the abstract.
- [ROBINS-I](https://methods.cochrane.org/bias/risk-bias-non-randomized-studies-interventions): the 2016 version remains the established tool while ROBINS-I V2 is explicitly described by Cochrane as a **first draft** as of 2026-07-22. Label draft use.
- [QUADAS-3](https://www.bristol.ac.uk/population-health-sciences/projects/quadas/) supersedes QUADAS-2 for primary diagnostic test-accuracy estimates; the 2026 tool evaluates Participants, Index Test, Target Condition, and Analysis at the relevant estimate level.
- [CONSORT 2025](https://www.consort-spirit.org/published-statements) replaces CONSORT 2010 for randomized-trial reporting.
- [PROBAST+AI and Cochrane prognosis tools](https://methods.cochrane.org/prognosis/tools) replace the earlier PROBAST framework for prediction-model bias/applicability; [TRIPOD+AI](https://www.tripod-statement.org/scope/) replaces TRIPOD 2015 for prediction-model reporting, including regression and machine-learning methods.
- [AMSTAR 2](https://www.bmj.com/content/358/bmj.j4008) is for systematic reviews of randomized and/or non-randomized **healthcare intervention** studies; it should not be converted into a summed score. Use [AMSTAR-PF](https://methods.cochrane.org/prognosis/tools) for systematic reviews of prognostic-factor studies and choose a purpose-specific method for other review types.
- [ROBIS](https://www.bristol.ac.uk/population-health-sciences/projects/robis/) assesses bias in systematic reviews across broad question types; fit still depends on the review question and target conclusion.
- [AGREE II](https://www.agreetrust.org/resource-centre/agree-ii/) evaluates guideline development quality, not whether every recommendation is correct.
- [EQUATOR](https://www.equator-network.org/reporting-guidelines/) is the reporting-guideline registry.

## PEDro use

The [PEDro scale](https://pedro.org.au/wp-content/uploads/PEDro_scale.pdf) supports rapid trial screening in physiotherapy. Eligibility is not counted in the total. The score does not measure external validity, effect size, intervention reporting, or clinical benefit. Interpret items and use RoB 2 for a comprehensive RCT result-level bias assessment.

## Rehabilitation-specific bias checks

- Therapist and participant blinding may be impossible; do not assign automatic high risk. Judge deviations and outcome-measurement bias for the specified result.
- Extract provider expertise, equipment, supervision, adherence, progression rules, co-intervention, home-program content, and intervention fidelity.
- Check whether the control is no treatment, attention control, usual care, sham, or a credible active intervention.
- Identify treatment preference, expectation, contamination, and unequal contact time.
- Use CERT and TIDieR to assess intervention-description completeness, not efficacy or risk of bias.

## Statistical audit

- Match effect measure to question and data; interpret the 95% interval's direction and width.
- Compare groups with the prespecified between-group effect/CI or appropriate group-by-time contrast. A significant pre/post change in one group and a non-significant change in the other do not establish treatment superiority.
- Separate within-person change thresholds from between-group clinical importance; do not apply MIC/MCID without checking population, scale, time and intended use.
- Report NNT/NNH only with a defensible baseline risk and time horizon.
- Preserve MD/SMD scale direction; do not treat SMD as a natural clinical unit.
- Inspect multiplicity across outcomes, time points, and subgroups; require an interaction test for subgroup differences.
- Examine missingness assumptions, complete-case bias, clustering, repeated measures, baseline adjustment, regression to the mean, early stopping, and model overfitting.
- For non-inferiority/equivalence, verify margin, analysis populations, constancy/assay-sensitivity assumptions, and interval interpretation.

## Systematic-review audit

First classify the review question: intervention effect, diagnostic accuracy, prognostic factor, prediction model, prevalence, etiology, qualitative synthesis, measurement, or another purpose. Then choose the compatible review-level and included-study tools. AMSTAR 2 is not a universal systematic-review tool.

Check protocol, eligible designs, comprehensive reproducible search, duplicate selection/extraction, excluded-study list, study-level bias, effect metric, heterogeneity, synthesis model, missing results, small-study effects, funding/conflicts, and outcome-level certainty. A random-effects model does not solve heterogeneity.
