---
title: "Phase 1 — Evidence Gathering"
title_tr: "Aşama 1 — Kanıt Toplama"
node_type: phase
phase_number: 1
document_type: report
phase_gate_in: "phase-0-brief.md"
phase_gate_out: "phase-2-reading.md"
description: "Identify and collect relevant policy documents, datasets, previous reports, and academic literature. Determine whether primary data collection is needed. Maintain a provenance record — government statistics and official sources are preferred over secondary summaries."
description_tr: "İlgili politika belgelerini, veri kümelerini, önceki raporları ve akademik literatürü belirleyip toplayın. Birincil veri toplama gerekip gerekmediğini belirleyin. Bir kaynak kaydı tutun — hükümet istatistikleri ve resmi sources ikincil özetlere tercih edilir."
tags: [phase, report, evidence, data, policy, provenance]
outputs:
  - "evidence_inventory.md"
links_to:
  - skills/core/iron-rules.md
  - skills/core/agent-orchestration.md
  - skills/phases/report/phase-0-brief.md
language: bilingual
version: "1.0"
---

# Phase 1 — Evidence Gathering
# Aşama 1 — Kanıt Toplama

## Gate Rule / Geçiş Kuralı

**EN:** Gather only evidence that is relevant to the scope defined in brief.md. Do not collect interesting material that falls outside scope. If scope seems too narrow after gathering, return to Phase 0 and revise with commissioner approval.

**TR:** Yalnızca brief.md'de tanımlanan kapsamla ilgili kanıtları toplayın. Kapsam dışında kalan ilginç materyali toplamayın. Toplama sonrasında kapsam çok dar görünüyorsa Aşama 0'a dönün ve komisyoncu onayıyla revize edin.

---

## 1. Evidence Types / Kanıt Türleri

**EN:** Reports draw from four evidence tiers. Prefer higher tiers where available.

**TR:** Raporlar dört kanıt katmanından yararlanır. Mevcut olduğunda daha yüksek katmanları tercih edin.

| Tier / Katman | Type / Tür | Examples / Örnekler |
|--------------|-----------|---------------------|
| 1 — Primary official / Birincil resmi | Government statistics, official reports, legal documents / Hükümet istatistikleri, resmi raporlar, yasal belgeler | TÜİK, Eurostat, UN, OECD |
| 2 — Institutional / Kurumsal | Major NGO reports, intergovernmental reports / Büyük STK raporları, hükümetlerarası raporlar | World Bank, WHO, ILO |
| 3 — Academic / Akademik | Peer-reviewed research / Hakemli araştırma | Journal articles, systematic reviews |
| 4 — Secondary / İkincil | News, commentary, think-tank briefs / Haberler, yorumlar, düşünce kuruluşu brifingleri | Use only to identify primary sources |

---

## 2. Source Categories Relevant to This Report / Bu Rapora İlgili Kaynak Kategorileri

**EN:** Check each category for relevant material. Not all will apply to every report.

**TR:** Her kategoriyi ilgili materyal için kontrol edin. Her rapor için hepsi geçerli olmayacaktır.

- [ ] Policy documents and legislation / Politika belgeleri ve mevzuat
- [ ] Official statistical datasets / Resmi istatistiksel veri kümeleri
- [ ] Previous reports on the same topic / Aynı konudaki önceki raporlar
- [ ] Academic literature (targeted, not systematic) / Akademik literatür (hedefli, sistematik değil)
- [ ] Interviews / expert consultations needed? / Görüşmeler / uzman danışmaları gerekli mi?
- [ ] Survey data needed? / Anket verileri gerekli mi?
- [ ] Case studies / comparative examples / Vaka çalışmaları / karşılaştırmalı örnekler

---

## 3. Primary Data Assessment / Birincil Veri Değerlendirmesi

**EN:** Determine whether secondary sources are sufficient or whether primary data collection is required. Primary data (interviews, surveys, field observations) is costly in time and must be decided here, not mid-report.

**TR:** İkincil sourcesın yeterli olup olmadığını veya birincil veri toplamanın gerekip gerekmediğini belirleyin. Birincil veriler (görüşmeler, anketler, saha gözlemleri) zaman açısından maliyetlidir ve rapor ortasında değil, burada karar verilmelidir.

```
Are secondary sources sufficient? / İkincil sources yeterli mi? [Yes / No]
If No — primary data method needed / Hayırsa — gerekli birincil veri yöntemi:
  [ ] Expert interviews / Uzman görüşmeleri — N = ___
  [ ] Survey / Anket — N = ___
  [ ] Freedom of Information requests / Bilgi edinme başvuruları
  [ ] Field observation / Saha gözlemi
Estimated time for primary collection / Birincil toplama için tahmini süre:
```

---

## 4. Evidence Inventory / Kanıt Envanteri

**EN:** Record every collected source. This becomes evidence_inventory.md. Include provenance — where the data came from, when accessed, and reliability assessment.

**TR:** Toplanan her kaynağı kaydedin. Bu, evidence_inventory.md olur. Provenance'ı ekleyin — verilerin nereden geldiği, ne zaman erişildiği ve güvenilirlik değerlendirmesi.

```markdown
## Evidence Inventory / Kanıt Envanteri

| ID | Title | Source | Type/Tier | Date | Access Date | Relevance | Notes |
|----|-------|--------|-----------|------|-------------|-----------|-------|
| E01 | | | Tier 1 | | | High/Med/Low | |
| E02 | | | Tier 2 | | | | |
```

---

## 5. Gaps Identified / Belirlenen Boşluklar

**EN:** Note what evidence you expected to find but could not locate. Report these gaps in the Methods/Limitations section. Do not pretend evidence is stronger than it is.

**TR:** Bulmayı beklediğiniz ancak bulamadığınız kanıtları not edin. Bu boşlukları Yöntemler/Sınırlılıklar bölümünde raporlayın. Kanıtın olduğundan daha güçlü olduğunu iddia etmeyin.

```
Evidence gap 1 / Kanıt boşluğu 1:
Evidence gap 2 / Kanıt boşluğu 2:
```

---

## Completion Checklist / Tamamlama Kontrol Listesi

- [ ] All relevant source categories checked / Tüm ilgili kaynak kategorileri kontrol edildi
- [ ] Primary data decision made and documented / Birincil veri kararı verildi ve belgelendi
- [ ] evidence_inventory.md completed with provenance / evidence_inventory.md provenance ile tamamlandı
- [ ] Evidence gaps documented / Kanıt boşlukları belgelendi
- [ ] exec_summary updated with any scope implications / exec_summary kapsam etkileriyle güncellendi

**Gate in:** phase-0-brief.md
**Gate out:** → phase-2-reading.md
