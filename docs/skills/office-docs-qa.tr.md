# office-docs-qa

[English](office-docs-qa.en.md) · [Türkçe](office-docs-qa.tr.md) · [Library](../../README.tr.md)

**Belge yapısı, içerik ve görünümü açık doğrulama sınırlarıyla kontrol eder.**

## Örnek istek

> Bu çalışma kitabını denetle; gerçekten yapılan kontrolleri bildir.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Quality-first handling of office files and diagrams: Word DOCX, PDF (extract, merge, split, OCR, forms, redaction), Excel/CSV workbooks, reading PowerPoint files (building or redesigning a deck goes to presentation-studio), large or unknown files, workflow diagrams (Mermaid, SVG, HTML) and Markdown knowledge bases, preserving structure and verifying the output. Turkish triggers: Word dosyası, PDF birleştir/böl, Excel düzenle, PPTX kontrol, dosyayı oku, diyagram çiz, akış şeması, not arşivi düzenle. More triggers: bilgi tabanı kur, indeks ve bağlantılar, iş akışını görselleştir, süreç veya sistem haritası, Mermaid.

</details>

## Çalışma mantığı

Biçim ve araçları belirler; yapıyı/içeriği inceler; mümkünse görünümü kontrol eder; üretimle native uygulama doğrulamasını ayırır.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/office-docs-qa/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Modül | Kaynak kapsamı |
|---|---|
| [docx-workflow](../../skills/common/office-docs-qa/modules/docx-workflow/MODULE.md) | Apply a preservation-first workflow to read, create, edit, and validate Word DOCX documents while protecting structure, styles, relationships, accessibility, and existing user cont |
| [file-reading-workflow](../../skills/common/office-docs-qa/modules/file-reading-workflow/MODULE.md) | Apply a safe, bounded workflow for inspecting local or uploaded files without flooding context or treating binary data as text. Use when the user requests this workflow or when an  |
| [knowledge-base](../../skills/common/office-docs-qa/modules/knowledge-base/MODULE.md) | Create, organize, audit, or maintain a durable Markdown knowledge base with an index, atomic notes, stable identifiers, links, tags, and maintenance checks. Use for a personal or t |
| [pdf-workflow](../../skills/common/office-docs-qa/modules/pdf-workflow/MODULE.md) | Apply a provenance-first PDF workflow for inspecting, extracting, creating, combining, splitting, rotating, redacting, OCR, or form filling. Use when the user asks for this workflo |
| [workflow-visualizer](../../skills/common/office-docs-qa/modules/workflow-visualizer/MODULE.md) | Create an accessible, self-contained workflow diagram as HTML, Mermaid, or SVG from a process description. Use to map systems, data flows, decisions, ownership, handoffs, or timeli |
| [xlsx-workflow](../../skills/common/office-docs-qa/modules/xlsx-workflow/MODULE.md) | Apply a preservation-first workflow to read, create, edit, clean, calculate, chart, and validate XLSX/XLSM workbooks. Use when the user asks for this workflow or needs an additiona |
