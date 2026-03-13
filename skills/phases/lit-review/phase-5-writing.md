---
title: "Phase 5 — Writing & PRISMA Reporting"
title_tr: "Aşama 5 — Yazım ve PRISMA Raporlama"
node_type: phase
phase_number: 5
document_type: lit-review
phase_gate_in: "phase-4-synthesis.md"
phase_gate_out: null
description: "Write the systematic review manuscript in the prescribed order: Methods → Results → Discussion → Introduction → Abstract. Ensure PRISMA checklist compliance and include an explicit limitations section."
description_tr: "Sistematik inceleme makalesini belirtilen sırayla yazın: Yöntemler → Sonuçlar → Tartışma → Giriş → Özet. PRISMA kontrol listesi uyumunu sağlayın ve açık bir sınırlılıklar bölümü ekleyin."
tags: [phase, lit-review, writing, PRISMA, manuscript, submission]
outputs:
  - "manuscript_draft.md"
  - "PRISMA_checklist_completed.md"
links_to:
  - skills/core/iron-rules.md
  - skills/core/agent-orchestration.md
  - skills/phases/lit-review/phase-4-synthesis.md
  - skills/techniques/paragraph-coherence.md
  - skills/techniques/natural-voice.md
  - skills/core/guided-writing-mode.md
language: bilingual
version: "1.0"
---

# Phase 5 — Writing & PRISMA Reporting
# Aşama 5 — Yazım ve PRISMA Raporlama

## Gate Rule / Geçiş Kuralı

**EN:** Do not begin writing until synthesis_map.md and evidence_table.md are finalized. Writing without a complete synthesis map leads to structure-by-sources rather than argument-by-evidence.

**TR:** synthesis_map.md ve evidence_table.md kesinleştirilmeden yazmaya başlamayın. Tam bir sentez haritası olmadan yazmak, kanıta dayalı argüman yerine sourcesa dayalı yapıya yol açar.

---

## Guided Writing Mode / Rehberli Yazım Modu

Bu fazda `skills/core/guided-writing-mode.md` protokolü aktiftir:
- Her bölüm/paragraf için A/B seçenekleri üretilir
- Her seçenek kaynak kanıtlarıyla desteklenir (📚)
- Akademik Yazım Notu yapıyı ve normu açıklar (📖)
- Kullanıcı seçer, birleştirir veya yeniden yönlendirir
- Demir Kural 1: Kaynak olmadan yazım YOK

In this phase, the `skills/core/guided-writing-mode.md` protocol is active:
- A/B draft options are generated for each section/paragraph
- Each option is backed by source evidence (📚)
- Academic Writing Note explains structure and norms (📖)
- User selects, merges, or redirects
- Iron Rule 1: No writing without source

---

## 1. Writing Order / Yazım Sırası

**EN:** Write sections in this order. The logic: Methods and Results contain facts you already have. Discussion interprets them. Introduction contextualizes after you know what you found. Abstract last because it summarizes all sections.

**TR:** Bölümleri bu sırayla yazın. Mantık: Yöntemler ve Sonuçlar zaten sahip olduğunuz gerçekleri içerir. Tartışma bunları yorumlar. Giriş, ne bulduğunuzu bildikten sonra bağlamı verir. Özet en son çünkü tüm bölümleri özetler.

```
1. Methods / Yöntemler
2. Results / Sonuçlar
3. Discussion / Tartışma
4. Introduction / Giriş
5. Abstract / Özet
```

---

## 2. Methods Section / Yöntemler Bölümü

**EN:** Report everything from the protocol. A reader must be able to replicate your search using only this section. Include:
- Review registration (PROSPERO ID if registered)
- Eligibility criteria
- Information sources (databases, search dates)
- Search strategy (one complete example string in full)
- Study selection process (screening stages, who screened, disagreement resolution)
- Data extraction process
- Quality assessment tool and scoring

**TR:** Protokoldeki her şeyi raporlayın. Bir okuyucu yalnızca bu bölümü kullanarak aramanızı kopyalayabilmelidir. Şunları ekleyin:
- İnceleme kaydı (kayıtlıysa PROSPERO kimliği)
- Uygunluk kriterleri
- Bilgi sourcesı (veritabanları, arama tarihleri)
- Arama stratejisi (tam olarak bir eksiksiz örnek dize)
- Çalışma seçim süreci (tarama aşamaları, kim taradı, anlaşmazlık çözümü)
- Veri çıkarma süreci
- Kalite değerlendirme aracı ve puanlama

---

## 3. Results Section / Sonuçlar Bölümü

**EN:** Structure directly from synthesis_map.md. One subsection per theme. For each:
- Name the theme
- Report how many studies address it and their quality range
- Present findings without interpretation (interpretation goes in Discussion)
- Include PRISMA flow diagram (numbers from Phases 1–2)

**TR:** Doğrudan synthesis_map.md'den yapılandırın. Tema başına bir alt bölüm. Her biri için:
- Temayı adlandırın
- Kaç çalışmanın onu ele aldığını ve kalite aralıklarını raporlayın
- Bulgular yorumsuz sunun (yorum Tartışma'ya gider)
- PRISMA akış diyagramını ekleyin (Aşama 1–2'deki sayılar)

---

## 4. Discussion Section / Tartışma Bölümü

**EN:** Interpret the synthesis. Required elements:
- Answer the research question stated in Phase 0 — directly and explicitly
- Explain what the findings mean in context of existing theory
- Address contradictions found in synthesis
- State evidence gaps from synthesis_map.md as directions for future research
- Explicit limitations section (see below)

**TR:** Sentezi yorumlayın. Gerekli unsurlar:
- Aşama 0'da belirtilen araştırma sorusunu — doğrudan ve açıkça — yanıtlayın
- Bulguların mevcut teori bağlamında ne anlama geldiğini açıklayın
- Sentezde bulunan çelişkileri ele alın
- synthesis_map.md'deki kanıt boşluklarını gelecekteki araştırma yönleri olarak belirtin
- Açık sınırlılıklar bölümü (aşağıya bakın)

---

## 5. Limitations Section (Mandatory) / Sınırlılıklar Bölümü (Zorunlu)

**EN:** Every systematic review must include an honest limitations section. Common ones to address:
- Language bias (searches in English only?)
- Publication bias (grey literature excluded?)
- Database coverage (not all databases indexed equally)
- Heterogeneity of included studies
- Quality of included studies
- Date range restrictions

**TR:** Her sistematik inceleme dürüst bir sınırlılıklar bölümü içermelidir. Ele alınacak yaygın olanlar:
- Dil önyargısı (yalnızca İngilizce aramalar mı?)
- Yayın önyargısı (gri literatür dışlandı mı?)
- Veritabanı kapsamı (tüm veritabanları eşit biçimde dizinlenmemiş)
- Dahil edilen çalışmaların heterojenliği
- Dahil edilen çalışmaların kalitesi
- Tarih aralığı kısıtlamaları

---

## 6. PRISMA Checklist / PRISMA Kontrol Listesi

**EN:** Complete the PRISMA checklist before submission. Mark each item with the page/section number where it is addressed.

**TR:** Göndermeden önce PRISMA kontrol listesini tamamlayın. Her öğeyi ele alındığı sayfa/bölüm numarasıyla işaretleyin.

Key items / Temel öğeler:
- [ ] Title identifies review as systematic / Başlık incelemeyi sistematik olarak tanımlıyor
- [ ] Structured abstract with all required components / Tüm gerekli bileşenlerle yapılandırılmış özet
- [ ] PROSPERO registration reported / PROSPERO kaydı raporlandı
- [ ] Eligibility criteria reported / Uygunluk kriterleri raporlandı
- [ ] All databases with search dates reported / Tüm veritabanları arama tarihleriyle raporlandı
- [ ] Full search string for at least one database / En az bir veritabanı için tam arama dizesi
- [ ] PRISMA flow diagram included / PRISMA akış diyagramı dahil
- [ ] Characteristics of included studies table / Dahil edilen çalışmaların özellikleri tablosu
- [ ] Risk of bias / quality assessment reported / Risk of bias / kalite değerlendirmesi raporlandı
- [ ] Limitations section present / Sınırlılıklar bölümü mevcut

---

## AI Hakem İncelemesi / AI Reviewer Gate

Yazım fazı tamamlandığında, sonraki faza geçmeden önce `/ai-review` komutu çalıştırılmalıdır.
Bkz: `skills/core/reviewer-mode.md`

Before advancing to the next phase, run `/ai-review` to trigger AI Peer Review.
See: `skills/core/reviewer-mode.md`

---

## Completion Checklist / Tamamlama Kontrol Listesi

- [ ] All sections written in prescribed order / Tüm bölümler belirtilen sırayla yazıldı
- [ ] Research question from Phase 0 explicitly answered / Aşama 0'dan araştırma sorusu açıkça yanıtlandı
- [ ] PRISMA checklist completed / PRISMA kontrol listesi tamamlandı
- [ ] Limitations section included / Sınırlılıklar bölümü dahil
- [ ] PRISMA flow diagram matches Phase 1–2 numbers / PRISMA akış diyagramı Aşama 1–2 sayılarıyla eşleşiyor
- [ ] Manuscript ready for submission / Makale göndermeye hazır

**Gate in:** phase-4-synthesis.md
**Gate out:** submission
