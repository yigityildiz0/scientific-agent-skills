# Research Sources Used While Designing This Skill

This skill was designed around the following source-backed principles:

- the assistant Skills are directories containing a `SKILL.md` file with YAML frontmatter, including required `name` and `description` fields.
- Skills work through progressive disclosure: metadata first, `SKILL.md` when relevant, and supporting reference files only as needed.
- Custom Skills can be uploaded to Claude.ai as ZIP files through Settings > Features when available for the user plan.
- NotebookLM prompts should explicitly specify source scope, artifact type, output language, audience, style, focus, and evidence rules.
- NotebookLM source behavior matters: sources are always used from the selected/all source set, notes are used only when selected, and conversation history can influence responses.
- NotebookLM Studio artifacts such as slide decks, flashcards, quizzes, audio/video overviews, and infographics support customization prompts and settings.
- Google prompt design guidance emphasizes clear instructions, context, examples, structured output, task decomposition, and iteration.

Primary sources reviewed:

- Anthropic Agent Skills overview and engineering article.
- Anthropic public Skills repository and skill-creator example.
- Google AI/Gemini prompt design strategies.
- Google Cloud Gemini prompt design strategies.
- Google NotebookLM Help pages for sources, notes, output language, flashcards/quizzes, audio/video overviews, infographics, slide decks, and FAQs.
- Google blog updates on NotebookLM learning features.
- NotebookLM community/Reddit discussions for practical study patterns; used only as secondary signal, not as authoritative documentation.
