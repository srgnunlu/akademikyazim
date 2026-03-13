---
title: "Phase 0 — Abstract & Claim First"
title_tr: "Aşama 0 — Önce Özet ve İddia"
node_type: phase
phase_number: 0
document_type: conference
phase_gate_in: null
phase_gate_out: "phase-1-literature.md"
description: "Conference papers begin with the abstract submission. Write the abstract first, identify the target conference, and submit before expanding into a full paper."
description_tr: "Konferans bildirileri özet gönderimiyle başlar. Önce özeti yaz, hedef konferansı belirle ve tam bildiriye genişletmeden önce gönder."
tags: [phase, conference, abstract, claim, submission]
outputs:
  - "abstract_v1.md"
  - "submission_checklist.md"
links_to:
  - skills/core/iron-rules.md
  - skills/core/source-policy.md
language: bilingual
version: "1.0"
---

# Phase 0 — Abstract & Claim First / Önce Özet ve İddia

## Purpose / Amaç

Conference papers invert the normal writing sequence: you write and submit the abstract before the full paper exists. The abstract is not a summary of finished work — it is a precise commitment to what you will demonstrate. This phase forces that commitment into writing before any other work proceeds.

Konferans bildirileri normal yazım sırasını tersine çevirir: tam bildiri var olmadan önce özeti yazar ve gönderirsin. Özet, bitmiş çalışmanın özeti değildir — ne göstereceğine dair kesin bir taahhüttür. Bu aşama, başka herhangi bir çalışma ilerlemeden önce o taahhüdü yazıya zorla döker.

---

## Step 1 — Write the Abstract First / Önce Özeti Yaz

The abstract must be 250-500 words (check target conference for exact limit). It must contain four elements — even if the research is preliminary:

Özet 250-500 kelime olmalı (tam limit için hedef konferansı kontrol et). Araştırma ön aşamada olsa bile dört öğe içermeli:

**1. Problem** — What is the problem or question this paper addresses?
Be specific. "AI in education" is not a problem statement. "The lack of real-time feedback mechanisms in automated essay scoring systems limits adoption in under-resourced classrooms" is a problem statement.

**1. Problem** — Bu bildiri hangi problemi veya soruyu ele alıyor?
Spesifik ol. "Eğitimde yapay zeka" bir problem ifadesi değildir.

**2. Approach** — What method, framework, or analysis did you use?
State the approach even if results are preliminary. Reviewers evaluate whether the approach is sound, not only whether results are complete.

**2. Yaklaşım** — Hangi yöntemi, çerçeveyi veya analizi kullandın?
Sonuçlar ön aşamada olsa bile yaklaşımı belirt. Hakemler yaklaşımın sağlam olup olmadığını değerlendirir, sadece sonuçların tamamlanıp tamamlanmadığını değil.

**3. Contribution** — What does this paper establish, show, or argue?
This is the claim. It must be falsifiable and specific. If you cannot state the contribution in one sentence, the work is not ready for abstract submission.

**3. Katkı** — Bu bildiri ne ortaya koyuyor, gösteriyor veya savunuyor?
Bu, iddiadır. Yanlışlanabilir ve spesifik olmalı. Katkıyı bir cümlede ifade edemiyorsan, çalışma özet gönderimi için hazır değil.

**4. Result** — What is the main finding or expected finding?
If the work is complete: state the result. If preliminary: state the expected result and the evidence basis for expecting it. Do not fabricate results.

**4. Sonuç** — Ana bulgu veya beklenen bulgu nedir?
Çalışma tamamsa: sonucu belirt. Ön aşamadaysa: beklenen sonucu ve bunu beklemenin kanıt temelini belirt. Sonuç uydurmayın.

---

## Step 2 — Select Target Conference / Hedef Konferansı Seç

For each candidate conference, record:

Her aday konferans için kaydet:

- Conference name, acronym, and organizing body (ACM, IEEE, etc.)
- Submission deadline (abstract deadline vs. full paper deadline — these differ)
- Acceptance rate (last 2 years) — this calibrates expected quality bar
- Typical audience and scope — does your contribution fit?
- Page limit for full paper (typically 4, 6, 8, or 10 pages)
- Reference format (ACM, IEEE, APA, Chicago)
- Double-blind review? (affects anonymization requirements)
- Proceedings: will the paper be indexed (DBLP, ACM DL, IEEE Xplore, Scopus)?

- Konferans adı, kısaltması ve düzenleyici kuruluş (ACM, IEEE, vb.)
- Gönderim son tarihi (özet son tarihi vs. tam bildiri son tarihi — bunlar farklı)
- Kabul oranı (son 2 yıl) — beklenen kalite barını kalibre eder
- Tipik izleyici kitlesi ve kapsam — katkındır uyuyor mu?
- Tam bildiri sayfa limiti (tipik olarak 4, 6, 8 veya 10 sayfa)
- Referans formatı (ACM, IEEE, APA, Chicago)
- Çift-kör inceleme? (anonimleştirme gereksinimlerini etkiler)
- Bildiriler: makale endekslenecek mi (DBLP, ACM DL, IEEE Xplore, Scopus)?

---

## Step 3 — Build Submission Checklist / Gönderim Kontrol Listesini Oluştur

Create `submission_checklist.md` now, before the paper is written. Fill in the requirements from the conference Call for Papers.

Bildiri yazılmadan önce şimdi `submission_checklist.md` oluştur. Konferans Bildiri Çağrısından gereksinimleri doldur.

This checklist will be used in Phase 4 (Finalization). Creating it now means requirements are not discovered at the last moment.

Bu kontrol listesi Aşama 4'te (Sonlandırma) kullanılacak. Şimdi oluşturmak, gereksinimlerin son anda keşfedilmemesi anlamına gelir.

---

## Step 4 — Submit the Abstract / Özeti Gönder

Submit through the conference submission system (EasyChair, HotCRP, CMT, or similar).

Konferans gönderim sistemi aracılığıyla gönder (EasyChair, HotCRP, CMT veya benzeri).

Keep a local copy of exactly what was submitted — the accepted abstract is a contractual commitment to the reviewers and the program committee. The full paper must deliver what the abstract promises.

Gönderilenlerin tam bir yerel kopyasını sakla — kabul edilen özet, hakemlere ve program komitesine karşı sözleşmesel bir taahhüttür. Tam bildiri, özetin vaat ettiklerini teslim etmelidir.

---

## Output / Çıktı

**abstract_v1.md** — The submitted abstract, exactly as submitted, with:
- Submission date and conference name recorded at the top
- All four elements (problem, approach, contribution, result) present
- Word count within the conference limit

**submission_checklist.md** — All formatting and submission requirements from the conference CfP, organized as a checklist for use in Phase 4.

---

## Completion Criteria / Tamamlanma Kriterleri

- [ ] Abstract contains all four elements: problem, approach, contribution, result.
- [ ] Contribution is stated in one falsifiable sentence.
- [ ] Target conference is selected with deadline and formatting requirements recorded.
- [ ] `abstract_v1.md` saved with submission date.
- [ ] `submission_checklist.md` created from conference CfP.
- [ ] Abstract is submitted to the conference system (OR a clear submission date is set).

- [ ] Özet dört öğenin tamamını içeriyor: problem, yaklaşım, katkı, sonuç.
- [ ] Katkı bir yanlışlanabilir cümlede ifade edilmiş.
- [ ] Hedef konferans, son tarih ve biçimlendirme gereksinimleri kaydedilmiş olarak seçilmiş.
- [ ] `abstract_v1.md` gönderim tarihiyle kaydedilmiş.
- [ ] `submission_checklist.md` konferans BÇ'den oluşturulmuş.
- [ ] Özet konferans sistemine gönderilmiş (VEYA net bir gönderim tarihi belirlenmiş).

Do not proceed to Phase 1 until the abstract is submitted or a firm submission date is set.

Özet gönderilmeden veya kesin bir gönderim tarihi belirlenmeden Aşama 1'e geçme.
