# NotebookLM Artifact Prompt Templates

Use these templates as building blocks. Adapt them to the user's course, artifact type, and source set.

## 1. Chat / direct answer

```text
Seçili kaynaklara dayanarak sorumu cevapla: [SORU]

Cevap formatı:
- Önce 3–5 maddelik net sonuç.
- Sonra konu başlıklarına ayrılmış detaylı açıklama.
- Gereken yerde tablo kullan.
- En sonda "Kaynaklarda belirsiz/kısıtlı kalan noktalar" bölümü oluştur.

Kurallar:
- Yalnızca seçili kaynaklara dayan.
- Kaynaklarda olmayan bilgiyi ekleme.
- Önemli iddialara citation ekle.
- Gereksiz giriş, sonuç, motivasyon ve kişisel yorum yazma.
```

## 2. Dense study note / lecture note

```text
Seçili kaynaklardan sınava yönelik yoğun ders notu çıkar.

Hedef: [ders adı] / [sınav tipi] için hızlı ama eksiksiz çalışma notu.
Seviye: [öğrenci seviyesi]

Çıktı:
1. Yüksek verimli konu iskeleti
2. Temel kavramlar ve kısa tanımlar tablosu
3. Mekanizma / neden-sonuç akışı
4. Klinik veya pratik bağlantılar
5. Sınıflamalar, farklar, kontrendikasyonlar ve istisnalar
6. Sınavda karışabilecek yerler: "X ≠ Y" formatında
7. 20 aktif hatırlama sorusu + kısa cevap
8. Kaynaklarda eksik/belirsiz kalan noktalar

Kurallar:
- Türkçe yaz.
- Her madde bilgi taşısın; boş cümle kullanma.
- Uzun paragraf yerine başlık, tablo ve kısa maddeler kullan.
- Citation ekle.
- Kaynakta olmayan bilgiyi dışarıdan tamamlama.
```

## 3. Report / custom report / briefing doc

```text
Seçili kaynaklardan özel rapor oluştur.

Rapor tipi: [study guide / briefing doc / glossary / clinical summary / comparison report]
Amaç: [amaç]
Hedef okuyucu: [seviye]

Rapor yapısı:
1. Yönetici özeti: en fazla 8 madde
2. Ana konu haritası
3. Detaylı bölümler
4. Karşılaştırma tabloları
5. Önemli kaynak alıntıları/citationlar
6. Uygulama veya sınav bağlantısı
7. Açık kalan sorular ve kaynak boşlukları

Kurallar: kaynak dışı bilgi ekleme, tekrarları birleştir, gereksiz giriş/sonuç kullanma, yoğun ve taranabilir yaz.
```

## 4. Flashcards

```text
Seçili kaynaklardan kapsamlı flashcard seti oluştur.

Hedef: [ders/konu] için aktif hatırlama.
Zorluk: [kolay/orta/zor/karma]
Kart sayısı: [sayı veya "olabildiğince kapsamlı"]

Kart türleri:
- Tanım kartları
- Mekanizma kartları
- Karşılaştırma kartları
- Klinik/senaryo kartları
- Tuzak/istisna kartları

Format:
Tablo halinde ver:
| Ön yüz | Arka yüz | Kaynak/citation | Zorluk | Etiket |

Kurallar:
- Her kart tek bilgi çekirdeğini test etsin.
- Çok uzun arka yüz yazma; gerektiğinde 2–4 maddeye böl.
- Kaynakta olmayan bilgiyi ekleme.
- Ezber değil, ayırt etme ve kavrama odaklı kartlar da ekle.
```

## 5. Quiz / MCQ / clinical vignette

```text
Seçili kaynaklardan sınav tarzı quiz oluştur.

Soru sayısı: [sayı]
Soru tipi: [çoktan seçmeli / kısa cevap / vaka / karışık]
Zorluk: [orta-zor]
Odak: [tanım, mekanizma, klinik, ayırıcı fark, kontrendikasyon, tablo bilgisi]

Format:
1. Soru
2. Şıklar veya beklenen cevap
3. Doğru cevap
4. Neden doğru?
5. Yanlış şıklar neden yanlış?
6. Kaynak/citation

Kurallar:
- Ezber sorusu kadar ayırt ettirici soru da üret.
- Hoca tuzağı olabilecek yakın kavramları özellikle sor.
- Kaynak dışı bilgi kullanma.
```

## 6. Audio Overview

```text
Bu Audio Overview'i [hedef dinleyici] için hazırla.

Amaç: [konuyu hızlı anlamak / sınav öncesi tekrar / karşıt görüşleri tartışmak / eleştirel inceleme]
Odak: [3–6 ana odak]
Ton: Akademik ama sade; gereksiz sohbet, espri ve uzatma olmasın.
Uzunluk: [kısa / orta / uzun]

İçerik kuralları:
- Kaynakların ana fikirlerini önceliklendir.
- Sınavda karışabilecek noktaları açıkça vurgula.
- Terimleri kısa tanımla, mekanizmaları neden-sonuç olarak anlat.
- Kaynaklarda belirsiz olan yerleri belirsiz diye söyle.
- Gereksiz podcast muhabbeti, dramatik giriş ve kişisel yorum ekleme.
```

## 7. Video Overview

```text
Bu Video Overview'i [hedef] için oluştur.

Amaç: Görsel olarak anlaşılır, sınav odaklı konu özeti.
Görsel stil: [sade akademik / profesyonel / şema ağırlıklı]
Odak: [ana başlıklar]

İstenen akış:
1. Konu haritası
2. Temel tanımlar
3. Mekanizma/akış şeması
4. Klinik veya pratik bağlantı
5. Sınav tuzakları ve karıştırılan kavramlar
6. Kısa tekrar

Kurallar:
- Kaynak dışı bilgi ekleme.
- Slayt/ekran başına az ama yoğun bilgi koy.
- Şema, ok, karşılaştırma ve tablo mantığını kullan.
- Dekoratif ama bilgi taşımayan görsel isteme.
```

## 8. Slide Deck

```text
Seçili kaynaklardan [hedef kitle] için slide deck oluştur.

Amaç: [ders anlatımı / sınav tekrarı / konu özeti / klinik sunum]
Uzunluk: [kısa/default/uzun veya slayt sayısı]
Dil: Türkçe
Stil: Minimal, modern, akademik; yüksek kontrastlı, okunaklı.

Slayt yapısı:
1. Başlık + öğrenme hedefleri
2. Konu haritası
3. Temel kavramlar
4. Mekanizma/akış şeması
5. Tablolar ve karşılaştırmalar
6. Klinik/pratik bağlantılar
7. Sınavda karışan noktalar
8. Özet + aktif hatırlama soruları

Kurallar:
- Her slaytta bilgi yoğun ama okunabilir olsun.
- Uzun paragraflar yerine kısa maddeler, tablo ve şema kullan.
- Kaynaklarda olmayan bilgiyi ekleme.
- Görsel/faktüel hata riskini azaltmak için her slaytta sadece kaynak destekli içerik kullan.
- Kırmızı/işaretli/vurgulu kaynak alanları varsa önceliklendir.
```

## 9. Infographic

```text
Seçili kaynaklardan tek sayfalık infografik oluştur.

Amaç: [konunun hızlı görsel özeti]
Dil: Türkçe
Detay düzeyi: Detailed
Yön: [Portrait / Landscape / Square]
Stil: Profesyonel, temiz, akademik; fazla dekoratif değil.

İçerik:
- Ana başlık
- 4–6 ana bilgi bloğu
- En önemli mekanizma/akış
- Kritik karşılaştırma tablosu
- Sınav tuzakları mini kutusu
- Kaynakta belirsiz kalan nokta varsa küçük not

Kurallar:
- Bilgi yoğun ama okunabilir olsun.
- Dekoratif öğe yerine şema, ok, tablo, ikon ve hiyerarşi kullan.
- Kaynak dışı bilgi ekleme.
```

## 10. Mind map

```text
Seçili kaynaklardan konu haritası/mind map üret.

Merkez konu: [konu]
Amaç: Konunun dallarını, alt başlıklarını ve ilişkilerini görmek.

Kurallar:
- Ana dallar: tanım, sınıflama, mekanizma, klinik, değerlendirme, tedavi/uygulama, sınav tuzakları.
- Her dalda kısa ama bilgi taşıyan ifadeler kullan.
- Yakın kavramları bağla ve farklarını belirt.
- Kaynak dışı bilgi ekleme.
```

## 11. Chat customization / Learning Guide mode

```text
Bu notebook'taki sohbeti şu öğrenme moduna göre yürüt:

Rol: Beni [ders/konu] için çalıştıran, kaynaklara sıkı bağlı, sınav odaklı öğretici.
Tarz: Önce kısa net cevap, sonra gerekiyorsa detay. Gereksiz yorum yok.
Öğretme yöntemi:
- Önce kavram iskeleti kur.
- Sonra mekanizma ve neden-sonuç ilişkisini açıkla.
- Ardından bana 3–5 aktif hatırlama sorusu sor.
- Yanlış cevap verirsem kısa düzeltme + kaynak dayanağı ver.
- Kaynakta olmayan bilgi için "kaynaklarda açık bilgi yok" de.

Çıktı kuralları:
- Türkçe.
- Tabloları aktif kullan.
- Sınav tuzaklarını ayrıca işaretle.
- Citation kullan.
```
