---
title: "Phase 5 — Peer Review Simulation"
title_tr: "Aşama 5 — Hakem İncelemesi Simülasyonu"
node_type: phase
phase_number: 5
document_type: article
phase_gate_in: "phase-4-writing.md"
phase_gate_out: null
description: "Simulate internal peer review before submission. Check argument clarity, source sufficiency, journal formatting requirements, and abstract quality. Produce a submission-ready manuscript."
description_tr: "Göndermeden önce dahili hakem incelemesi simüle et. Argüman netliğini, kaynak yeterliliğini, dergi biçimlendirme gereksinimlerini ve özet kalitesini kontrol et. Göndermeye hazır bir el yazması üret."
tags: [phase, article, revision, peer-review, submission]
outputs:
  - "submission/manuscript_final.md (or .docx/.tex)"
  - "submission/cover_letter.md"
  - "submission/submission_checklist.md"
links_to:
  - skills/core/iron-rules.md
  - skills/core/source-policy.md
language: bilingual
version: "1.0"
---

# Phase 5 — Peer Review Simulation / Hakem İncelemesi Simülasyonu

## Purpose / Amaç

Before submission, read the manuscript as a skeptical peer reviewer would. This phase applies three layers of review: argument quality, source integrity, and journal compliance. Each layer catches different failure types. Do not skip any layer.

Göndermeden önce, el yazmasını şüpheci bir hakem olarak oku. Bu aşama üç inceleme katmanı uygular: argüman kalitesi, kaynak bütünlüğü ve dergi uyumu. Her katman farklı hata türlerini yakalar. Hiçbir katmanı atlama.

---

## Layer 1 — Argument Quality Review / Argüman Kalite İncelemesi

Read the complete draft from beginning to end as if you are seeing it for the first time.

Tamamlanmış taslağı sanki ilk kez görüyormuşsun gibi başından sonuna kadar oku.

Check each of the following — note any failures:

Aşağıdakilerin her birini kontrol et — başarısızlıkları not et:

**Claim clarity / İddia netliği:**
- Can you identify the contribution claim within the first two paragraphs of the Introduction?
- Is the claim stated in the Abstract?
- Is the claim restated (not merely implied) in the Conclusion?

- Katkı iddiasını Giriş'in ilk iki paragrafı içinde belirleyebiliyor musun?
- İddia Özet'te belirtilmiş mi?
- İddia Sonuç'ta (yalnızca ima edilmeden) yeniden ifade edilmiş mi?

**Argument flow / Argüman akışı:**
- Does each section connect logically to the next?
- Does the Discussion interpret Results — or does it introduce new claims not supported by Results?
- Are all counter-arguments from `argument_map.md` addressed?

- Her bölüm mantıksal olarak bir sonrakine bağlanıyor mu?
- Tartışma Sonuçları mı yorumluyor — yoksa Sonuçlar tarafından desteklenmeyen yeni iddialar mı sunuyor?
- `argument_map.md` dosyasındaki tüm karşı-argümanlar ele alındı mı?

**Scope discipline / Kapsam disiplini:**
- Are there paragraphs or sections that do not serve the central claim? Mark them for removal or reduction.
- Is the Discussion longer than the Results? If so, investigate why.

- Merkezi iddiaya hizmet etmeyen paragraf veya bölümler var mı? Kaldırma veya azaltma için işaretle.
- Tartışma, Sonuçlardan daha uzun mu? Eğer öyleyse, nedenini araştır.

---

## Layer 2 — Source Integrity Review / Kaynak Bütünlüğü İncelemesi

This layer applies Iron Rules. Work through the manuscript citation by citation.

Bu katman Demir Kurallar uygular. El yazmasını atıf atıf gözden geçir.

For every in-text citation, verify:
- The source exists in `OKUMA_RAPORU.md`
- The claim being supported matches what the cited source actually says
- Page numbers are present where specific claims are made (for AKTİF sources)
- No citation is present for a source labeled ATLANDI

Her metin içi atıf için doğrula:
- Kaynak `OKUMA_RAPORU.md` dosyasında mevcut
- Desteklenen iddia, atıf yapılan kaynağın gerçekte söylediğiyle örtüşüyor
- Belirli iddialar yapılırken sayfa numaraları mevcut (AKTİF sources için)
- ATLANDI olarak etiketlenmiş bir kaynak için atıf yok

Check the reference list:
- Every in-text citation has a corresponding reference list entry
- Every reference list entry is cited in the text (no orphan references)
- All references are formatted correctly for the target journal

Referans listesini kontrol et:
- Her metin içi atıfın karşılık gelen bir referans listesi girişi var
- Her referans listesi girişi metinde atıf alıyor (yetim referans yok)
- Tüm referanslar hedef dergi için doğru biçimlendirilmiş

---

## Layer 3 — Journal Compliance Review / Dergi Uyum İncelemesi

Retrieve the author guidelines for the target journal. Review them now against the manuscript.

Hedef dergi için yazar kılavuzlarını al. Şimdi el yazmasına karşı incele.

**Structural requirements / Yapısal gereksinimler:**
- [ ] Word count within stated limit (including or excluding references — check which)
- [ ] Abstract within stated word limit
- [ ] Section headings match journal style
- [ ] Required sections present (e.g., some journals require a Data Availability statement, Ethics statement, Funding statement)

- [ ] Kelime sayısı belirtilen limit dahilinde (referanslar dahil mi hariç mi — hangisi olduğunu kontrol et)
- [ ] Özet belirtilen kelime limiti dahilinde
- [ ] Bölüm başlıkları dergi stiliyle eşleşiyor
- [ ] Gerekli bölümler mevcut (örn. bazı dergiler Veri Erişilebilirliği, Etik beyanı, Finansman beyanı gerektirir)

**Formatting requirements / Biçimlendirme gereksinimleri:**
- [ ] Reference format matches journal style guide exactly
- [ ] Figure and table captions formatted correctly
- [ ] Font, spacing, margin requirements met (if submitting formatted file)
- [ ] File format correct (PDF, DOCX, LaTeX — check journal requirement)

- [ ] Referans formatı dergi stil kılavuzuyla tam eşleşiyor
- [ ] Şekil ve tablo başlıkları doğru biçimlendirilmiş
- [ ] Font, aralık, kenar boşluğu gereksinimleri karşılandı (biçimlendirilmiş dosya gönderiliyorsa)
- [ ] Dosya formatı doğru (PDF, DOCX, LaTeX — dergi gereksinimini kontrol et)

**Author and submission requirements / Yazar ve gönderim gereksinimleri:**
- [ ] Author information prepared (affiliations, ORCID, corresponding author)
- [ ] Conflict of interest statement prepared
- [ ] Keywords selected from journal's approved list (if required)
- [ ] Cover letter drafted

- [ ] Yazar bilgisi hazırlandı (affiliasyonlar, ORCID, sorumlu yazar)
- [ ] Çıkar çatışması beyanı hazırlandı
- [ ] Anahtar kelimeler derginin onaylı listesinden seçildi (gerekirse)
- [ ] Ön yazı taslaklandırıldı

---

## Abstract Quality Check / Özet Kalite Kontrolü

The Abstract must stand alone. A reader who reads only the Abstract must understand:
- What problem was addressed
- What method or approach was used
- What the main finding is
- Why it matters

Özet bağımsız durabilmelidir. Yalnızca Özeti okuyan bir okuyucu şunları anlamalı:
- Hangi problem ele alındı
- Hangi yöntem veya yaklaşım kullanıldı
- Ana bulgunun ne olduğu
- Neden önemli olduğu

Test: give the Abstract to a colleague unfamiliar with your work and ask them to state what the article argues. If they cannot, the Abstract is insufficient.

Test: Özeti, çalışmanı tanımayan bir meslektaşına ver ve makalenin ne savunduğunu söylemesini iste. Söyleyemiyorlarsa, Özet yetersizdir.

---

## Automated Style Check / Otomatik Stil Kontrolü

Before Layer 1 review, run the style linter on the draft manuscript:

```bash
python3 tools/style_linter.py manuscript_draft.md --lang <tr|en> --json
```

Thresholds:
- `passive_density > 0.25` → flag passive sentences for active-voice revision
- `overhedge_count > 0` → show over-hedging chains to the user for tightening
- `overclaim_count > 0` → flag overstatements ("definitively proves", "kesinlikle kanıtlar")

Address flagged issues before proceeding to Layer 1.

---

## Output / Çıktı

**submission/manuscript_final** — The complete, formatted, submission-ready manuscript.

**submission/cover_letter.md** — A cover letter addressed to the editor containing:
- Title of the manuscript
- Statement that it is not under review elsewhere
- One paragraph stating the contribution and why it fits the journal
- List of 3-5 suggested reviewers (name, institution, email, rationale) — optional but recommended

**submission/submission_checklist.md** — The completed checklists from Layers 1-3 above, marked with pass/fail for each item.

---

## Completion Criteria / Tamamlanma Kriterleri

- [ ] All Layer 1 argument quality checks passed or issues addressed.
- [ ] All Layer 2 source integrity checks passed — no Iron Rule violations.
- [ ] All Layer 3 journal compliance checks passed.
- [ ] Abstract stands alone and delivers all four required elements.
- [ ] `submission/manuscript_final` is in the required file format.
- [ ] `submission/cover_letter.md` is complete.
- [ ] `submission/submission_checklist.md` is complete with all items checked.

- [ ] Tüm Katman 1 argüman kalite kontrolleri geçildi veya sorunlar ele alındı.
- [ ] Tüm Katman 2 kaynak bütünlüğü kontrolleri geçildi — Demir Kural ihlali yok.
- [ ] Tüm Katman 3 dergi uyum kontrolleri geçildi.
- [ ] Özet bağımsız duruyor ve dört gerekli öğenin tamamını sunuyor.
- [ ] `submission/manuscript_final` gerekli dosya formatında.
- [ ] `submission/cover_letter.md` tamamlanmış.
- [ ] `submission/submission_checklist.md` tüm öğeler işaretlenmiş olarak tamamlanmış.

When all criteria are checked, the manuscript is ready for submission.

Tüm kriterler işaretlendiğinde, el yazması göndermeye hazırdır.
