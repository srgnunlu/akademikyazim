---
title: "Pre-Submission Review — Simulating Peer Review Before Submission"
title_tr: "Gönderi Öncesi İnceleme — Hakem Simülasyonu"
node_type: technique
description: "Protocol for stress-testing a manuscript before submission by simulating harsh peer review. Forces the researcher to find and fix critical weaknesses before a real reviewer does. Fires at the final phase of every document type."
description_tr: "Gerçek hakem bulmadan önce kritik zayıflıkları tespit etmek için gönderi öncesi sert hakem simülasyonu protokolü. Her belge türünün son fazında zorunlu olarak tetiklenir."
tags: [pre-submission, peer-review, quality-control, self-review, publication-readiness, final-check]
links_to:
  - skills/core/quality-control.md
  - skills/techniques/feedback-integration.md
  - skills/techniques/journal-selection.md
  - skills/techniques/citation-formatting.md
used_by:
  - skills/phases/article/phase-5-revision.md
  - skills/phases/thesis/phase-7-finalization.md
  - skills/phases/conference/phase-4-finalization.md
  - skills/phases/grant-proposal/phase-5-review-submit.md
  - skills/phases/lit-review/phase-5-writing.md
language: bilingual
version: "1.0"
---

# Gönderi Öncesi İnceleme / Pre-Submission Review

Gerçek bir hakem reddetmeden önce sen reddet. Sonra düzelt.

---

## Ne Zaman Tetiklenir

Her belge türünün **son fazında**, gönderi kararından önce zorunludur:

| Belge Türü | Tetikleme Noktası |
|-----------|------------------|
| Dergi Makalesi | Faz 5 başında (revision cycle öncesi) |
| Tez | Faz 7 başında (nihai düzeltmeler öncesi) |
| Konferans Bildirisi | Faz 4 başında (finalizasyon öncesi) |
| Hibe Teklifi | Faz 5 başında (gönderi öncesi) |
| Literatür Derlemesi | Faz 5 başında (yazım tamamlandıktan sonra) |

---

## Ana Protokol: 5 Red Gerekçesi Bul

Claude'a bu prompt'u ver — kelimesi kelimesine:

```
Sen bu [makale/tez/bildiri]nin en sert ve en titiz hakemisin.
Reddetmek için 5 güçlü, spesifik gerekçe bul.

Her gerekçe için:
1. Sorunun tam olarak nerede olduğunu göster (bölüm, paragraf, sayfa)
2. Neden bu bir red sebebidir
3. Nasıl düzeltilebilir

Kibar olma. Gerçek bir hakem gibi davran.
```

**Kritik kural:** Claude'un bulduğu her red gerekçesine itiraz etme — önce düzelt, sonra itiraz et.

---

## Belge Türüne Göre Yaygın Red Gerekçeleri

### Dergi Makalesi
- Katkı iddiası (contribution claim) belirsiz veya önemsiz: *"Bu zaten biliniyordu"*
- Literatür taraması eksik veya güncel değil: kritik eserler atlanmış
- Metodoloji açıklaması yetersiz: tekrar edilebilirlik mümkün değil
- Bulgular tartışmada yeterince yorumlanmamış: sadece özet, analiz yok
- Sonuçlar iddiaları aşıyor (overclaiming): veriler sonuçları desteklemiyor
- Özet (abstract) ile makale arasında uyumsuzluk

### Tez
- Araştırma sorusu çok geniş veya çok dar
- Karşı argümanlar ele alınmamış (savunma zırhı eksik — bkz. Iron Rule 8)
- Metodoloji meşrulaştırılmamış: neden bu yöntemi seçtin?
- Özgün katkı açıkça ifade edilmemiş
- Kaynakça eksik veya son 5 yıllık literatür yok

### Konferans Bildirisi
- Abstract ile tam metin arasında içerik uyumsuzluğu
- Sayfa / kelime sınırı aşılmış
- Özgün katkı belirsiz: *"Bu neden bu konferansta sunulmalı?"*
- Sunum materyali (slayt) ile bildiri arasındaki bağ kurulmamış

### Hibe Teklifi
- Bütçe gerekçelendirmesi zayıf: rakamlar nereden geliyor?
- Etki (impact) bölümü muğlak: kim yararlanır, nasıl ölçülür?
- Fon çağrısı (RFP) kriterlerini doğrudan karşılamayan bölümler
- Ekip yeterliliği kanıtlanmamış

---

## Gönderi Öncesi Kontrol Listesi

Her maddeyi işaretle: ✅ Tamam | ⚠️ Gözden geçir | ❌ Eksik

**İçerik:**
- [ ] Katkı iddiası tek cümlede net olarak ifade edilmiş
- [ ] Araştırma sorusu/hipotez açık ve ölçülebilir
- [ ] Literatür taraması kapsamlı; son 5 yıl dahil
- [ ] Metodoloji tekrar edilebilir biçimde açıklanmış
- [ ] Bulgular ve tartışma bölümleri birbirinden ayrışıyor
- [ ] Sonuçlar yalnızca verinin desteklediği iddiaları içeriyor
- [ ] Karşı argümanlar ele alınmış ve yanıtlanmış

**Teknik:**
- [ ] Atıf formatı baştan sona tutarlı (bkz. [[citation-formatting]])
- [ ] Tüm atıflar `/sources/` klasöründeki dosyalarla eşleşiyor (Iron Rule 4)
- [ ] Şekil ve tablo başlıkları eksiksiz ve tutarlı
- [ ] Kelime / sayfa sınırı kontrol edildi
- [ ] Abstract dergi/konferansın gerektirdiği uzunlukta

**Etik ve Uyum:**
- [ ] Çıkar çatışması (conflict of interest) beyanı var mı?
- [ ] Fon kaynağı beyanı var mı?
- [ ] İnsan/hayvan deneyi varsa etik kurul onayı belirtilmiş mi?
- [ ] Veri paylaşım beyanı (data availability statement) var mı?
- [ ] Yazar katkıları belirtilmiş mi? (çok yazarlıysa)

**Son Kontrol:**
- [ ] Dergi seçimi tamamlandı — kapsam uyumu doğrulandı (bkz. [[journal-selection]])
- [ ] Gönderim kılavuzu (author guidelines) okundu ve uyuldu
- [ ] Dil ve yazım kalitesi gözden geçirildi

---

## Gönderi Kararı

```
0 ❌  → Göndermeye hazır. Git commit yap, gönder.
1–2 ❌ → Revizyon yap, kontrol listesini tekrar çalıştır.
3+ ❌  → Gönderme. Daha fazla çalışma gerekli.
```

Her düzeltme turu bir git commit'i: `revision(pre-sub): address 3 self-review issues`
