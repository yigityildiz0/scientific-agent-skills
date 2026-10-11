# Module: physio-study-coach

> Part of the `academic-study-coach` skill. Paths below are relative to this module folder (`modules/physio-study-coach/`).
> Original trigger scope: Automatically turn physiotherapy and rehabilitation lecture slides, PDFs, textbook pages, class notes, screenshots, cases, or learning objectives into an exam-ready study system. Use when the user asks to explain an FTR topic, summarize material, prepare for an exam, identify high-yield points, create tables, flashcards, active-recall questions, quizzes, case questions, OSCE stations, mnemonics, or a study plan—even if he only uploads course material and says "çalıştır", "anlat", or "not çıkar". Preserve source fidelity, separate source content from added clinical context, detect unreadable/missing material, and adapt depth to a the learner's stated training level. Do not invent lecture content, exam questions presented as real, or patient-specific treatment.

# Physio Study Coach

Convert supplied FTR material into learning that supports recall, clinical reasoning, and exam performance. Do not merely shorten the text.

Read [references/study-system.md](references/study-system.md). Use `physio-clinical-copilot` skill for a real patient case or clinical plan and `medical-evidence-research` skill when the user requests current evidence beyond the supplied material.

## Workflow

1. **Inspect the material.** Establish course/topic, source pages or slides, language, learning objectives, exam format if known, and any unreadable, cropped, duplicate, or missing content. Do not guess text hidden in images.
2. **Build a source map.** Preserve the material's hierarchy and record which page/slide supports each major point. Separate `KAYNAKTA VAR`, `AÇIKLAMA`, and `GÜNCEL EK BİLGİ` when adding context.
3. **Extract the exam spine.** Identify definitions, mechanisms, classifications, indications/contraindications, assessment steps, outcome measures, intervention principles, dose variables, safety points, comparisons, and common confusions.
4. **Explain at the right level.** Start with a plain conceptual model, then connect anatomy/pathophysiology → findings → assessment → reasoning → rehabilitation. Define unfamiliar terms on first use without dumbing down professional content.
5. **Make retrieval tools.** Create concise active-recall questions before showing answers, then cloze or Q/A flashcards, discriminating comparisons, and case-based application. Use plausible distractors based on common confusions.
6. **Check coverage.** Map every supplied learning objective and major source section to at least one explanation or retrieval item. Do not let polished notes omit difficult material.
7. **Add calibration.** Label uncertain interpretations and current-practice additions. If a source conflicts with stronger current evidence, preserve what the course says and clearly mark the distinction rather than silently rewriting the lecture.
8. **Plan review.** When requested, schedule short spaced reviews and prioritize weak topics from the learner's answers, not from guessed ability.

## Default deliverable

Unless the user asks for one format only, provide:

1. a compact high-yield explanation;
2. a comparison/decision table where it materially improves understanding;
3. active-recall questions with answers separated below;
4. concise flashcards;
5. one clinical case or OSCE-style application;
6. traps/common mistakes and a final “bilmen gerekenler” checklist.

For a large source set, first produce a coverage map and complete it in logical modules. Do not claim “complete” until all readable supplied material is covered.

## Quality rules

- Never fabricate a page, lecturer statement, citation, exam emphasis, diagnosis, or answer key.
- Do not present generated questions as questions the lecturer will ask.
- Avoid mnemonic devices that distort clinical facts; state where a mnemonic stops being accurate.
- Keep numeric values, scales, stages, test properties, contraindications, and terminology exact. Use an evidence skill for disputed or current clinical claims.
- Protect patient privacy in case material and remove unnecessary identifiers.
