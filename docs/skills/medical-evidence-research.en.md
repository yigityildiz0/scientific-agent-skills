# medical-evidence-research

[English](medical-evidence-research.en.md) · [Türkçe](medical-evidence-research.tr.md) · [Library](../../README.md)

**Search, appraise and synthesize medical evidence, including rehabilitation and Türkiye applicability.**

## Try it

> Compare exercise interventions for chronic low-back pain and assess applicability in Türkiye.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Searches/appraises biomedical, clinical and rehab evidence in PubMed, PEDro and Cochrane. Use for effectiveness, dose, harms, diagnosis, prognosis, statistics/MCID, GRADE, reviews/meta-analysis, legal full texts, journals and evidence updates. Literatür tara, makaleyi değerlendir, etkili mi, bilimsel gelişmeler. Short TR/EN requests: literatür / literatur / literature; makale / paper. Literatür tara; search literature; makaleyi değerlendir; appraise paper.

</details>

## How it works

Frame the question; search international and local-context sources; appraise design/bias; synthesize effects, harms, certainty and applicability.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/medical-evidence-research/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [content-access](../../skills/common/medical-evidence-research/modules/content-access/MODULE.md) | Legal methods for paywalled and geo-blocked content. Use for paywalls, academic papers, or open access via Unpaywall. |
| [physio-evidence-search](../../skills/common/medical-evidence-research/modules/physio-evidence-search/MODULE.md) | Search, synthesize, and clinically translate current physiotherapy and rehabilitation evidence. Use for effectiveness, comparative interventions, harms, dose/frequency, guidelines, |
| [physio-study-appraisal](../../skills/common/medical-evidence-research/modules/physio-study-appraisal/MODULE.md) | Critically appraise a named or supplied physiotherapy, rehabilitation, or clinical study with design-appropriate methods. Use for a PDF, DOI/PMID, RCT, cohort, diagnostic/prognosti |
| [scientific-literature-review](../../skills/common/medical-evidence-research/modules/scientific-literature-review/MODULE.md) | Produces traceable biomedical and life-science literature searches, evidence maps, narrative reviews, scoping reviews, and systematic-review drafts with verified citations. Use for |
