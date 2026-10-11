# NotebookLM prompt patterns

## Universal source-grounded frame

Include these elements in a natural single prompt:

1. **Role and audience:** who the output serves and their current level.
2. **Goal:** what the user should understand, remember, decide, or create.
3. **Source scope:** selected sources and any exclusions.
4. **Coverage contract:** required topics/sections and how to report omissions.
5. **Grounding contract:** citations/locators, no unsupported facts, conflict handling, missing-evidence language.
6. **Output structure:** headings, tables, questions, duration, number of items, or media sequence.
7. **Quality check:** coverage map, duplicate removal, terminology consistency, and uncertainty labels.

## Study guide

Request: conceptual map; high-yield explanation; definitions and mechanisms; comparison tables only where useful; clinical/application examples labeled as generated; common confusions; active-recall questions with answers separated; flashcards; final source-coverage matrix.

## Quiz and flashcards

Specify item count and mix, difficulty distribution, one idea per flashcard, plausible distractors, explanations, source locator for the correct answer, and no claim that generated questions predict the real exam.

## Audio Overview

Specify audience, language, approximate duration, two-speaker or suitable conversational structure if the feature supports it, learning arc, pronunciation of technical terms, mandatory topics, where sources disagree, recap, and three retrieval questions. Ask speakers not to add anecdotes or claims unsupported by the notebook.

## Video Overview or slides

Specify narrative/slide sequence, what each visual must explain, on-screen terminology, source locator in notes/caption, accessibility needs, and prohibition on invented charts, patient images, statistics, or quotations. Prefer diagrams and comparisons that can be derived from the sources.

## Infographic

Define one central message, audience, hierarchy, exact sections, comparison axes, labels/units, color or accessibility constraints, source footer, and a rule that unsupported numbers or icons implying magnitude must not be introduced.

## Research synthesis

Request a question/claim matrix, source-by-source contribution, agreements, conflicts, methodological limits, missing evidence, and conclusion confidence. Require that several sources tracing to one origin are not treated as independent confirmation.

## Coverage check

End substantial prompts with a requirement to provide a table containing each selected source, sections used, major contributions, and any unreadable or unused portion with a reason. This makes “all sources used” auditable instead of rhetorical.
