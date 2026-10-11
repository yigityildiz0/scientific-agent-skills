# Source Strategy for NotebookLM Prompts

## Key assumptions to build into prompts

- NotebookLM answers are grounded in uploaded/selected sources.
- Sources can be all sources or a selected subset.
- Notes are used only when selected.
- Conversation history can influence responses.
- For precise answers, mention source names or select the exact sources in the source panel.
- If using many PDFs/slides, ask NotebookLM to report which source supports each major claim.

## Source selection prompt add-ons

### Narrow to selected sources

```text
Yalnızca şu anda seçili olan kaynakları kullan. Seçili olmayan kaynaklardan bilgi çekme.
```

### Named-source priority

```text
Öncelik sırası: 1) [kaynak adı], 2) [kaynak adı], 3) diğer seçili kaynaklar. Çelişki varsa önce kaynak adını ver, sonra farkı açıkla.
```

### Multi-source synthesis

```text
Kaynakları ayrı ayrı özetleme; önce ortak ana fikirleri sentezle, sonra kaynaklar arasındaki farkları/çelişkileri tabloyla göster.
```

### Poor scan / OCR / image-heavy PDF

```text
PDF/slayt görsellerinde tablo, şekil, başlık, kırmızı yazı, altı çizili ve işaretli alanları özellikle dikkate al. Okunmayan veya belirsiz alanları uydurma; "okunmuyor/belirsiz" diye işaretle.
```

### YouTube / audio transcript

```text
Video/ses transkriptinden gelen bilgileri konu başlıklarına göre düzenle. Konuşma tekrarlarını, dolgu kelimeleri ve örnek tekrarlarını temizle; ama yeni bilgi ekleme. Önemli zaman akışı veya adım sırası varsa koru.
```

## Source-grounding guardrail

Use this guardrail in nearly every prompt:

```text
Kaynaklarda açıkça bulunmayan hiçbir bilgiyi kesin bilgi gibi yazma. Eğer dış bilgi kullanman gerekirse ayrı "Kaynak dışı genel bilgi olabilir" etiketiyle belirt; aksi halde ekleme.
```

For strict exam work, prefer the stricter version:

```text
Dış bilgi kullanma. Kaynakta yoksa "kaynaklarda açık bilgi yok" yaz.
```

## Citation discipline

Ask NotebookLM for citations after major claims, definitions, numeric values, classifications, contraindications, and tables.

```text
Tanım, sınıflama, sayı/parametre, klinik bulgu, kontrendikasyon ve tablo bilgilerinde citation ver. Citation olmayan önemli bilgiyi "citation yok" diye işaretle.
```

## Slide deck revision caveat

When revising generated slide decks, source grounding may be weaker than initial generation. If the user wants a revision, include source-backed content in the revision text itself or ask for a fresh deck rather than relying on the previous source context.

```text
Bu revizyonda kaynaklara dönülmeyebileceği için, değiştirilmesini istediğim içerik aşağıdadır. Bu metindeki bilgiyi koru, dışarıdan yeni bilgi ekleme: [metin]
```

## Large notebook strategy

If sources are numerous or very long, generate prompts in stages:

1. **Index prompt** — ask NotebookLM to map topics and source coverage.
2. **Deep prompt** — pick the highest-priority chapter/topic.
3. **Exam prompt** — convert deep notes into questions.
4. **Weakness prompt** — ask for gaps, contradictions, low-confidence areas.

Index prompt:

```text
Tüm seçili kaynaklardan konu haritası çıkar. Her ana konu için hangi kaynaklarda geçtiğini, kaynak yoğunluğunu ve sınav açısından önceliğini tabloyla ver. Detaylı açıklama yapma; sadece çalışma rotası çıkar.
```
