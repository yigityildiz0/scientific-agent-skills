# academic-study-coach

[English](academic-study-coach.en.md) · [Türkçe](academic-study-coach.tr.md) · [Library](../../README.md)

**Turn course material into a study plan, active recall and literature-reading practice.**

## Try it

> Build a two-week revision plan for rehabilitation research methods.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Academic study coach, FTR-focused: turns slides, PDFs, notes and screenshots into exam-ready summaries, tables, flashcards, active-recall and case/OSCE questions and study plans; teaches English physiotherapy and medical texts and terminology; writes NotebookLM prompts; plans the scholarly argument of thesis and conference talks (deck building, PPTX and speaker notes go to presentation-studio); handles scholarly writing compliance (CRediT, preregistration, ORCID, LLM-use disclosure, preprints); routes research-idea generation to the AI research library. Turkish triggers: sınava hazırla, slaytı özetle, soru çıkar, flashcard, İngilizce makaleyi çevir/anlat, terim ne demek, NotebookLM'e ne yazayım, tez sunumu, akademik sunum, tez konusu fikri. More triggers: konferans konuşması, seminer sunumu, ders notu çıkar, sınav soruları.

</details>

## How it works

Set the learning goal; identify gaps; give a worked example; test recall and adjust the plan.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/academic-study-coach/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [academic-presentations](../../skills/common/academic-study-coach/modules/academic-presentations/MODULE.md) | Plan, write, review, or improve academic presentations for thesis defenses, conferences, seminars, lab meetings, grant briefings, and research talks. Use when evidence, argument fl |
| [academic-writing](../../skills/common/academic-study-coach/modules/academic-writing/MODULE.md) | Scholarly writing and research compliance. Use for CRediT, preregistration, Plan S, Nelson Memo, preprints, ORCID, LLM disclosure. |
| [notebooklm-prompt-architect](../../skills/common/academic-study-coach/modules/notebooklm-prompt-architect/MODULE.md) | Automatically design high-quality, source-grounded prompts for Google NotebookLM when the user wants to study, research, summarize, compare, question, or create outputs from upload |
| [physio-clinical-english](../../skills/common/academic-study-coach/modules/physio-clinical-english/MODULE.md) | Read, translate, and deeply teach English physiotherapy and rehabilitation language without losing scientific detail. Use for an English article, abstract, guideline, report, table |
| [physio-study-coach](../../skills/common/academic-study-coach/modules/physio-study-coach/MODULE.md) | Automatically turn physiotherapy and rehabilitation lecture slides, PDFs, textbook pages, class notes, screenshots, cases, or learning objectives into an exam-ready study system. U |
