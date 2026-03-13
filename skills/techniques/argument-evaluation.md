---
title: "Argument Evaluation — Argüman Mantıksal Kalitesi"
title_tr: "Argüman Mantıksal Kalitesi Değerlendirmesi"
node_type: technique
description: "Method for evaluating the logical quality of thesis arguments: detecting logical fallacies, analyzing hidden assumptions, spotting cross-chapter contradictions, and testing synthesis quality. Applied in Phase 4 structure design and Phase 6 writing quality checks."
description_tr: "Tez argümanlarının mantıksal kalitesini değerlendirme yöntemi: mantık hatalarını tespit etme, gizli varsayımları analiz etme, bölümler arası çelişkileri yakalama ve sentez kalitesini test etme. Faz 4 yapı tasarımında ve Faz 6 yazım kalite kontrolünde uygulanır."
tags: [technique, argument-evaluation, logical-fallacies, assumption-analysis, synthesis, phase-4, phase-6]
links_to:
  - skills/techniques/critical-reading.md
  - skills/techniques/argument-mapping.md
  - skills/core/quality-control.md
  - skills/phases/thesis/phase-4-structure.md
used_by:
  - skills/phases/thesis/phase-4-structure.md
  - skills/phases/thesis/phase-6-writing.md
  - skills/core/quality-control.md
language: bilingual
version: "1.0"
---

# Argüman Mantıksal Kalitesi / Argument Evaluation

Bir tez argümanının **doğru sourcesa dayanması** ile **mantıksal olarak tutarlı olması** farklı şeylerdir.

İyi sourcesdan kötü argüman çıkabilir. Yüksek kaliteli akademik yazım ikisini birden gerektirir.

---

## Adım 1 — Argüman Zinciri Testi

Her ana argüman için şu üç halkayı kontrol et:

```
VARSAYIM → KANIT → SONUÇ

Varsayım: "Bu argüman neyi baştan kabul ediyor?"
Kanıt:    "Bunu destekleyen empirik/teorik veri nedir?"
Sonuç:    "Buradan çıkan yargı mantıksal olarak zorunlu mu?"
```

**Test:** Sonuç, kanıt olmadan da geçerli olur muydu? Eğer evet ise, kanıt gereksiz — argümanı yeniden kur.
**Test:** Varsayım yanlış olsaydı, sonuç çöker miydi? Eğer evet ise, varsayımı savunmak zorundasın.

---

## Adım 2 — Yaygın Mantık Hataları Listesi

Kendi yazımını şu listeyle karşılaştır:

| Hata Türü | Tanım | Tespit Sorusu |
|-----------|-------|---------------|
| **Hasımca temsil (Straw man)** | Karşı argümanı zayıf biçimde sunup çürütmek | "Karşı tarafın en güçlü versiyonunu mı eleştirdim?" |
| **Otoriteye başvuru (Appeal to authority)** | "X ünlü yazar söyledi, o zaman doğrudur" | "Yetkili kişinin kanıtı var mı, yoksa sadece prestiji mi?" |
| **Kısır döngü (Circular reasoning)** | Sonucu kanıt olarak kullanmak | "Sonucumu varsayım olarak kullandım mı?" |
| **Yanlış ikilem (False dichotomy)** | "Ya A ya B" — başka seçenek yok gibi sunmak | "Aslında C, D seçenekleri de var mı?" |
| **Korelasyonu nedensellik saymak** | İki şey birlikte değişiyor = biri diğerine neden oluyor | "Ters nedenselliği veya üçüncü değişkeni elledim mi?" |
| **Acele genelleme (Hasty generalization)** | Az örnekten geniş sonuç | "Örneklem temsil gücüne sahip mi?" |
| **Kayma (Slippery slope)** | "A olursa B olur, B olursa C olur..." zincirleri | "Her adım gerçekten zorunlu mu?" |
| **Çifte standart** | Aynı kriteri farklı taraflara farklı uygulamak | "Rakip teoriye de aynı standardı uyguladım mı?" |

---

## Adım 3 — Gizli Varsayım Analizi

Her bölümün giriş paragrafına bak. Şu soruyu sor:

"Bu bölümün çalışabilmesi için neyi doğru kabul ediyorum ama bunu okuyucuya söylemiyorum?"

**Örnekler:**
- "Merkez bankası bağımsızlığı enflasyonu düşürür" argümanı şunu varsayar: Para politikası enflasyonun birincil belirleyicisidir. — Bu tartışmalı bir varsayım.
- "Sözleşme özgürlüğü toplumsal refahı artırır" şunu varsayar: Taraflar eşit müzakere gücüne sahiptir. — Bu hukuk doktrininde sık tartışılan bir varsayım.

Gizli varsayımı bul → Tezde açıkça kabul et → Savun veya kısıtlılık olarak belirt.

---

## Adım 4 — Bölümler Arası Çelişki Tespiti

Yazım ilerledikçe kontrol et:

```
Soru: "Bölüm X'te savunduğum şey, Bölüm Y'de iddia ettiğimle çelişiyor mu?"
```

Bunu yakalamak için:
1. Her bölümün 1 cümlelik ana iddiasını çıkar
2. Bu cümleleri yan yana koy
3. Birbirine mantıksal olarak tutarlı mı?

**Çelişki bulunursa:**
- [ ] Birini revize et (hangisi daha güçlü kanıta sahip?)
- [ ] Gerilimi kabul et ve açıkla ("Bu ikilem disiplinde tartışmalıdır: X vs. Y")
- [ ] Kapsamı sınırla ("Bu argüman yalnızca Z koşulunda geçerlidir")

---

## Adım 5 — Sentez Kalitesi Testi

Thesis-Antithesis-Synthesis şeması:

```
Thesis (T):    "X doğrudur çünkü [kanıt A + B]"
Antithesis (A): "X yanlıştır çünkü [kanıt C + D]"
Synthesis (S):  "X, [bağlam/koşul] altında doğrudur;
                 ancak [A'nın işaret ettiği sınırlılık] geçerlidir."
```

**Kötü sentez:** T'yi tekrar et, A'yı yoksay.
**İyi sentez:** T ve A'nın her ikisinde de gerçek olan bir şeyi ortaya çıkar.

---

## Uygulama: Faz 4 Yapı Kontrolü

Yapı taslağı hazırlandığında şu soruları sor:

1. Her bölüm bir araştırma sorusunu yanıtlıyor mu? (Bölüm-RQ eşlemesi)
2. Bölümler mantıksal bir gerekçelendirme zinciri oluşturuyor mu?
   - Bölüm 1 → Bölüm 2 için zemin hazırlıyor mu?
   - Sonuç, girişteki soruyu gerçekten yanıtlıyor mu?
3. En güçlü karşı argüman nerede ele alınıyor?
   - Hiç ele alınmıyorsa → yapıya dahil et

## Uygulama: Faz 6 Yazım Kontrolü

Her bölüm tamamlandığında `quality-control.md`'deki listeye ek olarak:

- [ ] Bu bölümün merkezi argümanı tek cümleyle ifade edilebiliyor mu?
- [ ] Bu bölümde en az bir potansiyel karşı argüman ele alındı mı?
- [ ] Kullandığım kanıt, iddiamı destekliyor mu yoksa sadece ilgili mi?
- [ ] Bu bölümün varsayımları açıklandı mı?
