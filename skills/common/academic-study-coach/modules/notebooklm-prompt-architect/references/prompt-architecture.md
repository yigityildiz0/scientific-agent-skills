# Prompt Architecture for NotebookLM

## Design principle

NotebookLM works best when the prompt controls **scope, task, output, evidence, and density**. A good prompt is not "long"; it is modular. It tells NotebookLM what to use, what to produce, what not to add, and how to handle uncertainty.

## The NLM-PROMPT framework

Use this framework for most prompts:

1. **N — Notebook scope**
   - All sources / selected sources / named sources.
   - Ask for source names when narrowing matters.
   - Include "yalnızca seçili kaynaklara dayan."

2. **L — Learning objective**
   - Exam, lecture comprehension, clinical reasoning, active recall, presentation, revision.
   - State the user's academic level.

3. **M — Mode/artifact**
   - Chat answer, study note, briefing doc, report, flashcards, quiz, audio overview, video overview, slide deck, infographic, mind map.

4. **P — Persona/function**
   - Not vague "uzman gibi anlat." Use a functional role:
   - "FTR öğrencisine sınav odaklı ders notu çıkaran akademik asistan."
   - "Klinik mantık ve mekanizma bağını kuran öğretici."

5. **R — Required structure**
   - Exact headings, tables, bullet levels, number of questions, slide count, CSV format, etc.

6. **O — Output economy**
   - Dense, no filler, no intro/outro, short definitions, high-information tables.
   - Use compact markers: `Tanım`, `Mekanizma`, `Klinik`, `Sınav`, `Karışır`.

7. **M — Mistake control**
   - No unsupported external info.
   - Source citations for major claims.
   - Mark contradictions and missing source data.

8. **P — Priority signal**
   - Tell NotebookLM what to emphasize: highlighted text, red notes, teacher emphasis, tables, figures, repeated concepts, objectives.

9. **T — Test layer**
   - Add active recall, MCQ, short-answer, case question, flashcards, or "kendimi yoklama" section.

## Prompt modules

### Source module

```text
KAPSAM: Yalnızca seçili kaynakları kullan. Kaynaklarda açıkça geçmeyen bilgiyi dışarıdan tamamlama. Bir bilgi kaynaklarda yoksa "kaynaklarda açık bilgi yok" diye belirt. Kaynaklar arasında çelişki varsa ayrı işaretle.
```

### Density module

```text
YAZIM STİLİ: Çok yoğun bilgi aktar; gereksiz giriş, sonuç, yorum, motivasyon, genel tavsiye ve tekrar kullanma. Kısa ama eksik olmayan cümleler kur. Başlıkları taranabilir yap. Sayfa alanını verimli kullan.
```

### Evidence module

```text
KANIT: Önemli her iddiadan sonra mümkün olduğunca kaynak/citation ekle. Citation verilemiyorsa o iddianın kaynakta açık olup olmadığını belirt.
```

### Exam module

```text
SINAV ODAĞI: Tanım, mekanizma, sınıflama, ayırıcı fark, klinik bulgu, kontrendikasyon, istisna ve hocanın sorabileceği tuzak noktaları ayrı ayrı çıkar.
```

### Compression module

```text
FORMAT EKONOMİSİ: Uzun paragraf kullanma. Gereken yerde tablo kullan. Her madde bilgi taşısın. Boş açıklama, "önemlidir", "dikkat edilmelidir" gibi içi boş cümleleri çıkar; bunun yerine neden önemli olduğunu yaz.
```

## Few-shot mini-patterns

### Weak prompt

```text
Bu slaytı detaylı anlat.
```

### Strong prompt

```text
Seçili slayt/PDF kaynaklarını temel alarak FTR 3. sınıf final sınavına yönelik yoğun ders notu çıkar.

Çıktı sırası:
1. Konunun 10 satırlık yüksek verimli iskeleti
2. Terimler ve kısa tanımlar tablosu
3. Mekanizma/klinik bağlantı akışı
4. Sınavda sorulabilecek ayrımlar ve tuzaklar
5. Hoca vurgusu olabilecek tablolar, şekiller, kırmızı/işaretli yerler
6. 15 kısa aktif hatırlama sorusu + cevap

Kurallar: Yalnızca kaynaklara dayan, citation ekle, gereksiz giriş/sonuç yazma, kaynakta olmayan bilgiyi uydurma.
```

## Anti-patterns

Avoid prompts that:

- say only "özetle," "detaylı anlat," "bana çalıştır," "sunum hazırla";
- request detail without output structure;
- fail to specify source scope;
- ask for "sınavda çıkacak" as certainty instead of "sınavda sorulma ihtimali yüksek";
- ask for chain-of-thought or hidden reasoning;
- mix incompatible goals, e.g. "çok kısa ama eksiksiz tüm detaylar" without prioritization;
- request external medical claims while pretending they come from sources.
