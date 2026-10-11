# research-analyst

[English](research-analyst.en.md) · [Türkçe](research-analyst.tr.md) · [Library](../../README.md)

**Coordinate quick or deep research, claim verification, synthesis and timestamped video analysis.**

## Try it

> Research this claim deeply, separate promotion from evidence and explain uncertainty.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Research hub: quick/deep web research, multi-item comparison, trends, source/photo/video verification, report synthesis, legal and consumer questions. TR/EN: araştır / research; derin araştır / deep research; doğru mu / fact-check; kaynak var mı; raporları birleştir; iade/şikayet. Independent items may use authorized agents; this does not select the paid Parallel service.

</details>

## How it works

Frame the decision; choose the lightest sufficient module; open original sources and counterevidence; synthesize with citations and coverage limits.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

Video: the local FFmpeg/ffprobe helper produces sampled frames and timestamps. Visual interpretation needs host image capability; transcription needs a recognizer. Sampling is not complete coverage.

## Modules and source

[SKILL.md](../../skills/common/research-analyst/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [competitive-brief](../../skills/common/research-analyst/modules/competitive-brief/MODULE.md) | Research and write a decision-focused competitive brief using current, source-backed evidence. Use for competitor analysis, competitive brief, market comparison, feature comparison |
| [consumer-resolution](../../skills/common/research-analyst/modules/consumer-resolution/MODULE.md) | Resolve a consumer complaint, return, refund, cancellation, warranty, defective/missing order, subscription, chargeback, or seller/platform dispute with evidence and current jurisd |
| [decision-council](../../skills/common/research-analyst/modules/decision-council/MODULE.md) | Stress-test an important decision by running a structured council of expert perspectives, surfacing tensions, and ending with a synthesized recommendation and next steps. |
| [deep-reading-analyst](../../skills/common/research-analyst/modules/deep-reading-analyst/MODULE.md) | Deeply analyze user-supplied articles, papers, reports, transcripts, URLs, or other long-form content using structural reading, critical thinking, inversion, first principles, ment |
| [deep-research](../../skills/common/research-analyst/modules/deep-research/MODULE.md) | Automatically plan and execute deep, evidence-backed, multi-source research when the user says "derin/çok detaylı araştır", "bütün siteleri/kaynakları tara", "yüzeysel olma", "güze |
| [deep-research-compilation](../../skills/common/research-analyst/modules/deep-research-compilation/MODULE.md) | Compile multiple research reports (.docx/.md/.pdf/.pptx/.html/.txt/URLs) into one unified document (.docx, .pdf, or .md) with deduplicated inline [N] citations linking to a Referen |
| [evidence-integrity-guard](../../skills/common/research-analyst/modules/evidence-integrity-guard/MODULE.md) | Automatically audit evidence whenever a request depends on factual accuracy, current web information, research, comparison, a consequential decision, or doubt such as "araştır", "d |
| [fact-check-workflow](../../skills/common/research-analyst/modules/fact-check-workflow/MODULE.md) | Structured fact-checking workflow. Use when verifying claims for publication, rating claims, or setting pre-publication checks. |
| [firecrawl](../../skills/common/research-analyst/modules/firecrawl/MODULE.md) | Use an already configured Firecrawl client or API for authorized web search, scraping, mapping, crawling, and structured extraction with bounded scope, current official syntax, pro |
| [firecrawl-search](../../skills/common/research-analyst/modules/firecrawl-search/MODULE.md) | Search the web through an already configured Firecrawl capability, then open and verify primary sources with dates and provenance. Use when Firecrawl search is available and the us |
| [legal-research](../../skills/common/research-analyst/modules/legal-research/MODULE.md) | Research a legal question with jurisdiction, date, procedural posture, current primary law, authoritative guidance, deadlines, evidence needs, uncertainty, and escalation clearly s |
| [quick-research](../../skills/common/research-analyst/modules/quick-research/MODULE.md) | Automatically perform a fast, reliable web lookup when the user conversationally says "araştırır mısın", "bir bak", "bakabilir misin", "güncel mi", "fiyatı ne", "hangisi", "doğru m |
| [research-synthesis](../../skills/common/research-analyst/modules/research-synthesis/MODULE.md) | Synthesize qualitative research, feedback, interviews, observations, support tickets, or study notes into traceable themes, evidence, uncertainty, and actionable opportunities. Use |
| [source-driven-development](../../skills/common/research-analyst/modules/source-driven-development/MODULE.md) | Grounds every implementation decision in official documentation. Use when you want authoritative, source-cited code free from outdated patterns. Use when building with any framewor |
| [source-verification](../../skills/common/research-analyst/modules/source-verification/MODULE.md) | Verify sources, claims, images, video, documents, interviews, and synthetic media with SIFT and a durable evidence trail. Use before relying on uncertain material. |
| [trend-research](../../skills/common/research-analyst/modules/trend-research/MODULE.md) | Research any topic across Reddit, X (Twitter), and the web to identify recent trends (last 30 days) and generate production-ready prompts or recommendations |
| [vendor-review](../../skills/common/research-analyst/modules/vendor-review/MODULE.md) | Compare vendors, tools, agencies, platforms, or service providers using requirements, evidence, cost, integration, risk, support, and exit criteria. Use for vendor review, supplier |
| [video-understanding](../../skills/common/research-analyst/modules/video-understanding/MODULE.md) | video understanding |
| [web-archiving](../../skills/common/research-analyst/modules/web-archiving/MODULE.md) | Web archiving and retrieval via Wayback Machine and Archive.today. Use to preserve content, reach dead pages, or save evidence. |
| [weizhena-research](../../skills/common/research-analyst/modules/weizhena-research/MODULE.md) | Conduct preliminary research on a topic and generate research outline. For academic research, benchmark research, technology selection, etc. Use for a structured multi-item researc |
| [weizhena-research-add-fields](../../skills/common/research-analyst/modules/weizhena-research-add-fields/MODULE.md) | Add field definitions to existing research outline. Use with an existing /research outline. Turkish triggers: araştırmaya alan ekle, yeni kriter ekle. |
| [weizhena-research-add-items](../../skills/common/research-analyst/modules/weizhena-research-add-items/MODULE.md) | Add items (research objects) to existing research outline. Use with an existing /research outline. Turkish triggers: araştırmaya madde ekle, listeye yeni öğe ekle. |
| [weizhena-research-deep](../../skills/common/research-analyst/modules/weizhena-research-deep/MODULE.md) | Read research outline, launch independent agent for each item for deep research. Disable task output. Use after a /research outline exists or for /research-deep. Turkish triggers:  |
| [weizhena-research-report](../../skills/common/research-analyst/modules/weizhena-research-report/MODULE.md) | Summarize deep research results into markdown report, cover all fields, skip uncertain values. Use after /research-deep results exist or for /research-report. Turkish triggers: ara |
