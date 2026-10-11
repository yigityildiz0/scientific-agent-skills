# Quality Checklist

Before finalizing a NotebookLM prompt, check:

## Core clarity

- [ ] Target artifact is clear: chat, study note, report, quiz, flashcards, audio, video, slide deck, infographic, mind map.
- [ ] Source scope is explicit: selected sources / named sources / all sources.
- [ ] Audience and goal are stated.
- [ ] Output language is stated.
- [ ] Output structure is specified.
- [ ] Density/length rule is specified.

## Source accuracy

- [ ] Prompt says not to use unsupported external info.
- [ ] Prompt asks for citations/source references for important claims.
- [ ] Prompt tells NotebookLM what to do when sources are missing or contradictory.
- [ ] For slides/images/PDFs, prompt protects tables, figures, labels, highlights.

## Study value

- [ ] Includes high-yield summary.
- [ ] Includes mechanisms or why/how, not only definitions.
- [ ] Includes comparison/contrast for confusing concepts.
- [ ] Includes active recall: questions, cards, quiz, or self-test.
- [ ] Includes exam traps or likely question angles.

## Output economy

- [ ] Removes filler: intro, outro, generic advice, motivational talk, AI self-commentary.
- [ ] Uses tables where dense comparison is better than prose.
- [ ] Long paragraph risk is reduced.
- [ ] Every section has a job.

## Red flags

Revise if the prompt:

- says "detaylı anlat" without defining structure;
- requests "eksiksiz" without coverage checks;
- asks for certainty about exam predictions;
- mixes too many artifact types in one run;
- asks for external information but also says "only sources";
- is so long that the actual task becomes hard to see.

## Final micro-check prompt add-on

Add this to complex prompts:

```text
SON KALİTE KONTROLÜ: Cevabı bitirmeden önce kaynak kapsamını kontrol et. Atlanan ana başlık, citation verilmeyen kritik bilgi, kaynak çelişkisi veya belirsizliği varsa en sonda kısa listele.
```
