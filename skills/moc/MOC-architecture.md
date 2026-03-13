---
title: "MOC — Architecture Cluster"
title_tr: "MOC — Mimari Küme"
node_type: moc
cluster: architecture
description: "Navigation hub for system-wide architectural AI features (Guardian, Oracle, FIRE, Provenance)."
description_tr: "Sistem çapındaki mimari yapay zeka özellikleri (Guardian, Oracle, FIRE, Provenance) için navigasyon merkezi."
tags: [moc, architecture, ai-features, system, navigation]
cluster_nodes:
  - skills/architecture/methodological-oracle.md
  - skills/architecture/proactive-methodological-guardian.md
  - skills/architecture/feedback-integration-engine.md
  - skills/architecture/ai-provenance-layer.md
used_by:
  - skills/INDEX.md
language: bilingual
version: "1.0"
---

# MOC — Mimari Küme / Architecture Cluster

Bu küme, TezAtlas'ın çekirdek zekasını (core intelligence) barındırır. Standart Markdown faz dosyalarının ötesinde, sistemin bir metni *nasıl okuyacağı*, *nasıl sorgulayacağı* ve *nasıl denetleyeceği* ile ilgili temel AI davranış kurallarını içerir.

## Node'lar

| Node | Açıklama | Wikilink |
|------|----------|----------|
| Metodolojik Kahin | Yöntem/Soru uyumunu denetler (Faz 0/1/2) | [[architecture/methodological-oracle]] |
| Proaktif Gardiyan | Arka planda çalışır, kesin ifadeleri ve kaynaksızlıkları yakalar (Faz 5/6) | [[architecture/proactive-methodological-guardian]] |
| FIRE | Karmaşık geri bildirimleri tek bir yanıt şablonuna çevirir | [[architecture/feedback-integration-engine]] |
| Kaynak Katmanı | AI'ın kendi ürettiği taslakların (`Draft Generator` modu) kaynakçasını görünmez etiketlerle izler | [[architecture/ai-provenance-layer]] |
| Tekrarlanabilirlik Katmanı | Veri temizleme ve yazılım sürümlerini kaydederek 'Replikasyon Paketi' oluşturur | [[architecture/reproducibility-layer]] |
| İşbirlikçi Çalışma Alanı | Çoklu yazar desteği, not çakışması çözümü ve yazar katkı günlüğü (CRediT) | [[architecture/collaborative-workspace]] |
| Uyarlanabilir Çıktı | Tamamlanmış metinlerden basın bülteni veya özet (policy brief) üretir | [[architecture/adaptive-output]] |
| Otonom Telemetri | Kullanıcı zorlanmalarını tespit edip gizlilik odaklı geri bildirim JSON'u oluşturur | [[architecture/autonomous-telemetry]] |