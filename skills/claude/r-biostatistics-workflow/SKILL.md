---
name: r-biostatistics-workflow
description: "Plan, fit, diagnose, interpret, and report statistical analyses in R for laboratory, genetics, and bioscience data. Use when choosing among linear, generalized-linear, mixed-effects,."
license: MIT
metadata:
  source: original synthesis from R Core statistics documentation, lme4 guidance, and reviewed bioscience workflows
  reviewed: '2026-07-10'
---

# R Biostatistics Workflow

Use R to answer the stated scientific question with the simplest defensible model. A small p-value cannot repair a confounded design, pseudoreplication, outcome switching, selective exclusion, or an incorrect experimental unit.

## Route specialized analyses

- Randomization, blocking, controls, and prospective design: `experimental-design`.
- Bulk RNA-seq counts: `bio-differential-expression-deseq2-basics`.
- Single-cell models: `single-cell-rna-qc` and `scvi-tools`.
- Data cleaning/joins: `r-bioscience-data-wrangling`.
- Figures: `bio-data-visualization-ggplot2-fundamentals`.
- Reproducible execution and package state: `rstudio-reproducible-analysis`.

Do not replace a domain-specific count, survival, longitudinal, or omics method with a generic `t.test()` or `lm()` for convenience.

## Define the estimand before code

Write down:

1. experimental unit and unit of inference;
2. outcome, scale, units, and measurement process;
3. exposure/treatment and exact comparison or contrast;
4. biological versus technical replication;
5. pairing, repeated measures, nesting, blocking, batches, plates, runs, centers, donors, and families;
6. covariates selected before seeing results and why;
7. primary versus exploratory outcomes;
8. missing-data, exclusion, outlier, and multiplicity plan;
9. effect measure and uncertainty to report;
10. assumptions that are scientific, not merely mathematical.

If these cannot be resolved, produce an analysis-readiness report rather than inventing a model.

## Model routing

| Data/question | Starting model | Critical checks |
|---|---|---|
| Continuous outcome, independent units | `lm()` | linearity, residual pattern, influential observations, heteroskedasticity, estimability |
| Binary outcome | `glm(..., family = binomial())` | event counts, separation, link scale, calibration, predicted probabilities |
| Counts/rates | Poisson or negative-binomial GLM | exposure/offset, overdispersion, zero process, independent units |
| Paired two-condition data | paired contrast/model | pairing IDs, within-unit correlation, missing pairs |
| Repeated/nested data | mixed model or marginal model | random-effect structure, enough groups, singular fits, time structure |
| Ordered/multicategory outcome | appropriate ordinal/multinomial model | proportional-odds or category assumptions, sparse cells |
| Time-to-event | survival model | time origin, censoring, competing risks, proportional hazards |
| Many genes/features | domain method + FDR | feature universe, normalization, dependence, contrast, effect size |
| Very small or assumption-poor sample | exact/permutation/robust sensitivity analysis | exchangeability, discreteness, low power; avoid exaggerated certainty |

Nonparametric does not mean assumption-free. A permutation test still requires an exchangeability structure that respects pairing, blocks, or clusters.

## Build the model explicitly

Use a data argument and explicit factor levels. Inspect the model matrix and intended contrasts before fitting.

```r
analysis$condition <- relevel(factor(analysis$condition), ref = "control")
analysis$batch <- factor(analysis$batch)

fit <- lm(response ~ batch + condition, data = analysis, na.action = na.exclude)
model.matrix(fit) |> head()
summary(fit)
confint(fit)
```

For binary outcomes:

```r
fit <- glm(
  response_binary ~ batch + condition,
  family = binomial(),
  data = analysis,
  na.action = na.exclude
)

odds_ratio <- exp(coef(fit))
odds_ratio_ci <- exp(confint(fit))
```

State whether an effect is on the response, log-odds, log-count, hazard, or transformed scale. Convert it only when the conversion is valid and show the scale used.

For repeated measures, use a reviewed mixed-model workflow only when the required package is installed and the grouping structure is supported by the data:

```r
if (requireNamespace("lme4", quietly = TRUE)) {
  fit <- lme4::lmer(response ~ condition * time + (1 | subject_id), data = analysis)
  lme4::isSingular(fit)
}
```

Do not add a maximal random-effects structure blindly, and do not remove random effects merely to obtain significance. Report singularity, group counts, and sensitivity to defensible structures.

## Diagnostics are model-specific

Check the assumptions that affect the chosen estimate and inference:

- residuals versus fitted values and covariates;
- influence and leverage, with biological context;
- distribution/dispersion appropriate to the outcome;
- linearity on the link scale where required;
- calibration or predictive checks when relevant;
- random-effect singularity and enough independent groups;
- sparse cells, complete/quasi separation, and estimability;
- batch-treatment confounding and extrapolation;
- independence at the experimental-unit level.

Do not use a normality test as an automatic switch between parametric and nonparametric tests. With small samples it has low power; with large samples it flags harmless deviations. Use design, residual diagnostics, effect robustness, and sensitivity analyses together.

Do not delete an outlier only because it changes the p-value. Verify data integrity, document the biological/technical reason, report analyses with and without any defensible exclusion, and preserve the original data.

## Missing data

1. Quantify missingness by variable, group, batch, and time.
2. Distinguish not measured, failed QC, below detection, structural missingness, dropout, and unknown.
3. State what complete-case analysis assumes and how many experimental units it removes.
4. Use imputation only with a method that matches the analysis, includes relevant predictors, and propagates uncertainty.
5. Run sensitivity analysis when missing-not-at-random mechanisms are plausible.

Never replace missing biological measurements with zero by default.

## Multiplicity and selective analysis

- Define the family of hypotheses and primary endpoints before correction.
- Use FDR for high-dimensional exploratory feature sets when appropriate; use family-wise procedures for confirmatory families when required.
- Report the unadjusted estimate, uncertainty, adjusted measure, and tested family.
- Do not try many reasonable analyses and present only the smallest p-value.
- Label subgroup, post-hoc, and data-driven analyses as exploratory and test interactions rather than comparing “significant here, not significant there.”

## Effect-first reporting

For every primary result report:

- sample size and independent unit count per group;
- exclusions/missingness and reasons;
- exact model/formula, contrast, link, and reference levels;
- effect estimate with units/scale;
- confidence or credible interval;
- test statistic, degrees of freedom when applicable, and adjusted p-value/FDR;
- diagnostics and sensitivity analyses;
- software/package versions;
- limitations, especially confounding, small group counts, model dependence, and generalizability.

Use model-derived plots and raw-data displays together. Do not draw causal conclusions from observational associations without a defensible causal design.

## Completion gates

- Scientific question, estimand, and experimental unit agree.
- Model matches outcome and dependence structure.
- Formula, factor levels, and contrast were inspected.
- Diagnostics and sensitivity analyses were run and retained.
- Multiplicity and missingness are explicit.
- Code reruns in a clean project environment.
- Results emphasize effect size and uncertainty, not only significance.
- A qualified statistician reviews consequential, regulatory, clinical, or borderline analyses.

## Example prompts

- “Use $r-biostatistics-workflow to choose and justify an R model for this experiment. Start from the experimental unit, pairing, batches and outcome type; do not choose a test from p-values.”
- “Bu tekrarlı ölçüm deneyinde subject, batch ve time yapısını kontrol et; R formülünü, kontrastı, diagnostics ve sensitivity analizini açıkla.”
- “Audit this R analysis for pseudoreplication, missing-data bias, multiplicity, factor-level errors, selective exclusions, and effect-size reporting.”

## Primary references

- R `lm`: https://stat.ethz.ch/R-manual/R-devel/library/stats/html/lm.html
- R `glm`: https://stat.ethz.ch/R-manual/R-devel/library/stats/html/glm.html
- R model formulas: https://stat.ethz.ch/R-manual/R-devel/library/stats/html/formula.html
- R model diagnostics/accessors: https://stat.ethz.ch/R-manual/R-devel/library/stats/html/lm.summaries.html
- lme4 vignettes: https://lme4.github.io/lme4/articles/
