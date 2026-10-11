# academic-study-coach

[English](academic-study-coach.en.md) · [Türkçe](academic-study-coach.tr.md) · [Library](../../README.tr.md)

**Ders içeriğini çalışma planına, aktif hatırlamaya ve literatür okuma pratiğine dönüştürür.**

## Örnek istek

> Rehabilitasyon araştırma yöntemleri için iki haftalık tekrar planı hazırla.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Academic study coach, FTR-focused: turns slides, PDFs, notes and screenshots into exam-ready summaries, tables, flashcards, active-recall and case/OSCE questions and study plans; teaches English physiotherapy and medical texts and terminology; writes NotebookLM prompts; builds thesis and conference presentations; handles scholarly writing compliance (CRediT, preregistration, ORCID, LLM-use disclosure, preprints); routes research-idea generation to the AI research library. Turkish triggers: sınava hazırla, slaytı özetle, soru çıkar, flashcard, İngilizce makaleyi çevir/anlat, terim ne demek, NotebookLM'e ne yazayım, tez sunumu, akademik sunum, tez konusu fikri. More triggers: konferans konuşması, seminer sunumu, ders notu çıkar, sınav soruları.

</details>

## Çalışma mantığı

Öğrenme hedefini belirler; eksikleri bulur; örnek çözer; hatırlamayı sınayıp planı günceller.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/academic-study-coach/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Modül | Kaynak kapsamı |
|---|---|
| [academic-presentations](../../skills/common/academic-study-coach/modules/academic-presentations/MODULE.md) | Plan, write, review, or improve academic presentations for thesis defenses, conferences, seminars, lab meetings, grant briefings, and research talks. Use when evidence, argument fl |
| [academic-writing](../../skills/common/academic-study-coach/modules/academic-writing/MODULE.md) | Scholarly writing and research compliance. Use for CRediT, preregistration, Plan S, Nelson Memo, preprints, ORCID, LLM disclosure. |
| [notebooklm-prompt-architect](../../skills/common/academic-study-coach/modules/notebooklm-prompt-architect/MODULE.md) | Automatically design high-quality, source-grounded prompts for Google NotebookLM when the user wants to study, research, summarize, compare, question, or create outputs from upload |
| [physio-clinical-english](../../skills/common/academic-study-coach/modules/physio-clinical-english/MODULE.md) | Read, translate, and deeply teach English physiotherapy and rehabilitation language without losing scientific detail. Use for an English article, abstract, guideline, report, table |
| [physio-study-coach](../../skills/common/academic-study-coach/modules/physio-study-coach/MODULE.md) | Automatically turn physiotherapy and rehabilitation lecture slides, PDFs, textbook pages, class notes, screenshots, cases, or learning objectives into an exam-ready study system. U |
