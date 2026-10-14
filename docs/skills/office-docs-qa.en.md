# office-docs-qa

[English](office-docs-qa.en.md) · [Türkçe](office-docs-qa.tr.md) · [Library](../../README.md)

**Check document structure, content and presentation with explicit verification boundaries.**

## Try it

> Audit this workbook and report which checks actually ran.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Quality-first handling of office files and diagrams: Word DOCX, PDF (extract, merge, split, OCR, forms, redaction), Excel/CSV workbooks, reading PowerPoint files (building or redesigning a deck goes to presentation-studio), large or unknown files, workflow diagrams (Mermaid, SVG, HTML) and Markdown knowledge bases, preserving structure and verifying the output. Turkish triggers: Word dosyası, PDF birleştir/böl, Excel düzenle, PPTX kontrol, dosyayı oku, diyagram çiz, akış şeması, not arşivi düzenle. More triggers: bilgi tabanı kur, indeks ve bağlantılar, iş akışını görselleştir, süreç veya sistem haritası, Mermaid.

</details>

## How it works

Identify format and available tooling; inspect structure/content; check rendering when possible; separate file creation from native-app verification.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/office-docs-qa/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [docx-workflow](../../skills/common/office-docs-qa/modules/docx-workflow/MODULE.md) | Apply a preservation-first workflow to read, create, edit, and validate Word DOCX documents while protecting structure, styles, relationships, accessibility, and existing user cont |
| [file-reading-workflow](../../skills/common/office-docs-qa/modules/file-reading-workflow/MODULE.md) | Apply a safe, bounded workflow for inspecting local or uploaded files without flooding context or treating binary data as text. Use when the user requests this workflow or when an  |
| [knowledge-base](../../skills/common/office-docs-qa/modules/knowledge-base/MODULE.md) | Create, organize, audit, or maintain a durable Markdown knowledge base with an index, atomic notes, stable identifiers, links, tags, and maintenance checks. Use for a personal or t |
| [pdf-workflow](../../skills/common/office-docs-qa/modules/pdf-workflow/MODULE.md) | Apply a provenance-first PDF workflow for inspecting, extracting, creating, combining, splitting, rotating, redacting, OCR, or form filling. Use when the user asks for this workflo |
| [workflow-visualizer](../../skills/common/office-docs-qa/modules/workflow-visualizer/MODULE.md) | Create an accessible, self-contained workflow diagram as HTML, Mermaid, or SVG from a process description. Use to map systems, data flows, decisions, ownership, handoffs, or timeli |
| [xlsx-workflow](../../skills/common/office-docs-qa/modules/xlsx-workflow/MODULE.md) | Apply a preservation-first workflow to read, create, edit, clean, calculate, chart, and validate XLSX/XLSM workbooks. Use when the user asks for this workflow or needs an additiona |
