---
title: "Quality Control — Section and Thesis-Wide Checklists"
title_tr: "Kalite Kontrol — Bölüm ve Tez Geneli Kontrol Listeleri"
node_type: foundation
description: "Two checklists: per-section quality check (run after every written section) and thesis-wide consistency check (run in Phase 7 before finalization)."
description_tr: "İki kontrol listesi: her yazılı bölüm sonrası çalıştırılan bölüm kalite kontrolü ve Faz 7'de bitirilmeden önce çalıştırılan tez geneli tutarlılık kontrolü."
tags: [quality-control, checklist, verification, foundation, always-active]
links_to:
  - skills/core/source-policy.md
  - skills/core/context-management.md
  - skills/core/anti-hallucination.md
  - skills/core/operating-modes.md
  - skills/phases/thesis/phase-6-writing.md
  - skills/phases/thesis/phase-7-finalization.md
  - skills/techniques/argument-evaluation.md
  - skills/techniques/paragraph-coherence.md
  - skills/techniques/natural-voice.md
used_by:
  - skills/moc/MOC-core.md
  - skills/phases/thesis/phase-6-writing.md
  - skills/phases/thesis/phase-7-finalization.md
language: bilingual
version: "4.0"
---

# Kalite Kontrol / Quality Control

## Her Bölüm Sonrası Kontrol Listesi

Her alt bölüm yazıldıktan sonra çalıştır. Geçemeyen madde varsa tamamlandı deme.

- [ ] Her paragrafta en az 1 kaynaklı atıf var mı?
- [ ] Tüm atıflar `/sources/` klasöründeki PDF'lerden mi?
- [ ] Doğrudan alıntılar tırnak içinde ve sayfa numaralı mı?
- [ ] Parafrazlar orijinalden yeterince farklı mı?
- [ ] Orijinallik oranı %50+ mı?
- [ ] Terminoloji `TERMINOLOJI.md` ile tutarlı mı?
- [ ] Akademik dil tutarlı mı?
- [ ] Tez dilinin karakter kuralları doğru mu? (Türkçe: ş/ç/ğ/ı/ö/ü)
- [ ] Mevcut içerik kaybolmamış mı?
- [ ] Paragraf yapısı doğru mu? (konu → argüman → kaynak → geçiş)
- [ ] Önceki bölümle geçiş doğal mı?

**Paragraf Tutarlılığı** (detay: [[paragraph-coherence]]):
- [ ] Her paragraf Bağlam Kartı (PBK) ile üretildi mi? (ilk paragraf hariç)
- [ ] Argüman İzleyici'deki tüm alt iddialar ele alındı mı?
- [ ] Ardışık paragraflarda terim tekrarı yok mu? (TERMINOLOJI sabit terimleri hariç)
- [ ] Ardışık paragraflarda yapısal monotonluk yok mu? (aynı İ-K-G kalıbı arka arkaya)
- [ ] Her paragraf bölümün tezini bir adım ilerletiyor mu?

**Doğal Ses Kontrolü** (detay: [[natural-voice]]):
- [ ] Kara liste kelimesi paragraf başında veya geçiş olarak kullanılmamış mı?
- [ ] Cümle uzunluk varyasyonu yeterli mi? (paragrafta en az 3 bant: kısa/orta/uzun)
- [ ] Ardışık paragraflar farklı yapıyla mı açılıyor?
- [ ] Madde listesi oranı bölümdeki toplam metnin %15'inden az mı?
- [ ] `YAZIM_PROFILI.md` ile uyumlu mu? (profil varsa)

**Argüman mantıksal kalitesi** (detay: [[argument-evaluation]]):
- [ ] Her argümanın zinciri tam mı? (varsayım → kanıt → sonuç)
- [ ] Kullandığım kanıt iddiamı gerçekten destekliyor mu, yoksa sadece ilgili mi?
- [ ] Kaynaklar arası çelişki var mı ve açıklandı mı?
- [ ] Bu bölümdeki en güçlü karşı argümanı ele aldım mı?

**Metodoloji Tavsiyeleri — Anti-Halüsinasyon** (detay: [[anti-hallucination]]):
- [ ] AI'nın verdiği tüm metodoloji tavsiyeleri kaynaklı mı? (Demir Kural M)
- [ ] AI hiçbir istatistik/n/p değeri uydurmadı mı?
- [ ] Raporlama standartları gerçek rehbere atıfla verildi mi? (CONSORT, APA, PRISMA vb.)
- [ ] `[Source: Unverified]` işaretli maddeler kullanıcıya bildirildi mi?

## Tez Geneli Tutarlılık Kontrolü (Faz 7)

Faz 7'de, tüm bölümler yazıldıktan sonra çalıştır. [[phase-7-finalization]] bu kontrolü tetikler.

- [ ] Girişteki araştırma soruları sonuçta cevaplanmış mı?
- [ ] "Bölüm X'te ele alınacak" ifadeler gerçekten ele alınmış mı?
- [ ] Çapraz referanslar doğru mu?
- [ ] Tablo/şekil numaraları ardışık mı?
- [ ] Dipnotlarda "a.g.e." / "Ibid." — bir önceki dipnot gerçekten aynı kaynak mı?
- [ ] Terminoloji baştan sona tutarlı mı? (`TERMINOLOJI.md` ile karşılaştır)
- [ ] Kaynakçadaki her eser en az 1 dipnotta geçiyor mu?
- [ ] Dipnotlardaki her eser kaynakçada var mı?
- [ ] Kısaltmalar ilk kullanımda açıklanmış mı?
- [ ] `[KAYNAK BEKLENİYOR]` etiketi kalmadı mı?

Bütünlük kontrolü için `TUTARLILIK_KONTROLU.md` dosyası oluşturulur — şablonu [[tpl-status-summary]]'nin varyantı olarak kullan.
