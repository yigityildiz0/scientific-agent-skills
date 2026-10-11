# medical-evidence-research

[English](medical-evidence-research.en.md) · [Türkçe](medical-evidence-research.tr.md) · [Library](../../README.tr.md)

**Rehabilitasyon ve Türkiye uygulanabilirliği dahil tıbbi kanıtı arar, değerlendirir ve sentezler.**

## Örnek istek

> Kronik bel ağrısında egzersizleri karşılaştır; Türkiye’ye uygulanabilirliğini değerlendir.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Searches/appraises biomedical, clinical and rehab evidence in PubMed, PEDro and Cochrane. Use for effectiveness, dose, harms, diagnosis, prognosis, statistics/MCID, GRADE, reviews/meta-analysis, legal full texts, journals and evidence updates. Literatür tara, makaleyi değerlendir, etkili mi, bilimsel gelişmeler. Short TR/EN requests: literatür / literatur / literature; makale / paper. Literatür tara; search literature; makaleyi değerlendir; appraise paper.

</details>

## Çalışma mantığı

Soruyu çerçeveler; uluslararası ve yerel bağlam kaynaklarını tarar; tasarım/yanlılığı inceler; etki, zarar ve uygulanabilirliği sentezler.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/medical-evidence-research/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [content-access](../../skills/common/medical-evidence-research/modules/content-access/MODULE.md) | Legal methods for paywalled and geo-blocked content. Use for paywalls, academic papers, or open access via Unpaywall. |
| [physio-evidence-search](../../skills/common/medical-evidence-research/modules/physio-evidence-search/MODULE.md) | Search, synthesize, and clinically translate current physiotherapy and rehabilitation evidence. Use for effectiveness, comparative interventions, harms, dose/frequency, guidelines, |
| [physio-study-appraisal](../../skills/common/medical-evidence-research/modules/physio-study-appraisal/MODULE.md) | Critically appraise a named or supplied physiotherapy, rehabilitation, or clinical study with design-appropriate methods. Use for a PDF, DOI/PMID, RCT, cohort, diagnostic/prognosti |
| [scientific-literature-review](../../skills/common/medical-evidence-research/modules/scientific-literature-review/MODULE.md) | Produces traceable biomedical and life-science literature searches, evidence maps, narrative reviews, scoping reviews, and systematic-review drafts with verified citations. Use for |
