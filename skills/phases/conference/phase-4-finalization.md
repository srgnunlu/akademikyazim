---
title: "Phase 4 — Format & Submit"
title_tr: "Aşama 4 — Biçimlendirme ve Gönderim"
node_type: phase
phase_number: 4
document_type: conference
phase_gate_in: "phase-3-writing.md"
phase_gate_out: null
description: "Enforce the page limit, check anonymization for double-blind review, verify reference format, and complete the final submission checklist. This phase ends with a submitted paper."
description_tr: "Sayfa limitini zorla, çift-kör inceleme için anonimleştirmeyi kontrol et, referans formatını doğrula ve son gönderim kontrol listesini tamamla. Bu aşama gönderilmiş bir bildiriyle sona erer."
tags: [phase, conference, formatting, submission, anonymization]
outputs:
  - "submission/paper_final.pdf"
  - "submission/submission_checklist_completed.md"
links_to:
  - skills/core/iron-rules.md
  - skills/core/source-policy.md
language: bilingual
version: "1.0"
---

# Phase 4 — Format & Submit / Biçimlendirme ve Gönderim

## Purpose / Amaç

The content is written. This phase is about compliance — ensuring the paper meets every technical requirement of the conference before submission. Formatting failures cause desk rejections. Anonymization failures in double-blind submissions cause immediate disqualification. These are avoidable errors.

İçerik yazılmış. Bu aşama uyumla ilgilidir — bildirinin göndermeden önce konferansın her teknik gereksinimini karşıladığını sağlamak. Biçimlendirme hataları masa başı redlerine yol açar. Çift-kör gönderimlerde anonimleştirme hataları anında diskalifikasyona neden olur. Bunlar önlenebilir hatalardır.

---

## Step 1 — Page Limit Enforcement / Sayfa Limiti Yaptırımı

Check the conference page limit against your draft. Typical limits:

Taslağınıza karşı konferans sayfa limitini kontrol et. Tipik limitler:

- 4-page short paper: no overflow allowed
- 6-page paper: often allows 1 extra page for references only
- 8-page paper: often allows 1-2 extra pages for references only
- 10-page paper: check if references are included or excluded from the limit

- 4 sayfalık kısa bildiri: taşma izin verilmez
- 6 sayfalık bildiri: genellikle yalnızca referanslar için 1 ekstra sayfa izin verilir
- 8 sayfalık bildiri: genellikle yalnızca referanslar için 1-2 ekstra sayfa izin verilir
- 10 sayfalık bildiri: referansların limite dahil mi hariç mi olduğunu kontrol et

If the paper is over the page limit, apply cuts in this order:

Bildiri sayfa limitinin üzerindeyse, bu sırayla kes:

1. **Remove padding** — Introductory phrases ("It is widely known that..."), redundant sentences, over-long transitions
2. **Compress Related Work** — Each paragraph to 2-3 sentences; citation density over prose
3. **Compress Discussion** — Focus on the two most important interpretations only
4. **Reduce figure/table whitespace** — Reformat rather than remove content
5. **As a last resort** — Remove the least important finding or a secondary limitation

1. **Dolguyu kaldır** — Giriş ifadeleri ("Yaygın olarak bilinmektedir ki..."), gereksiz cümleler, aşırı uzun geçişler
2. **İlgili Çalışmaları sıkıştır** — Her paragraf 2-3 cümleye; düzyazı yerine atıf yoğunluğu
3. **Tartışmayı sıkıştır** — Yalnızca en önemli iki yoruma odaklan
4. **Şekil/tablo beyaz alanını azalt** — İçeriği kaldırmak yerine yeniden biçimlendir
5. **Son çare olarak** — En önemsiz bulguyu veya ikincil bir sınırlılığı kaldır

Do not cut the Methods or Results sections to meet the page limit unless absolutely necessary — these sections contain the substance of the contribution.

Sayfa limitini karşılamak için, kesinlikle gerekli olmadıkça Yöntemler veya Sonuçlar bölümlerini kesme — bu bölümler katkının özünü içerir.

---

## Step 2 — Anonymization Check / Anonimleştirme Kontrolü

First, confirm: is this conference using double-blind review?

Önce onayla: bu konferans çift-kör inceleme kullanıyor mu?

Check the conference website or Call for Papers. If double-blind: perform the full anonymization check below. If single-blind or open review: skip this step.

Konferans web sitesini veya Bildiri Çağrısını kontrol et. Çift-kör ise: aşağıdaki tam anonimleştirme kontrolünü gerçekleştir. Tek-kör veya açık inceleme ise: bu adımı atla.

**Double-blind anonymization checklist:**

**Çift-kör anonimleştirme kontrol listesi:**

- [ ] Author names removed from title page
- [ ] Author affiliations removed from title page
- [ ] Acknowledgments section removed or replaced with "Acknowledgments omitted for review"
- [ ] Self-citations do not reveal identity ("In our previous work [12]..." → "In prior work [12]..." or citation removed)
- [ ] Funding acknowledgments that identify the authors removed
- [ ] File metadata checked: author name not embedded in PDF document properties (check File → Properties in your PDF viewer)
- [ ] Supplementary materials (if any) are also anonymized
- [ ] GitHub or dataset links that identify the authors are anonymized or replaced with anonymous repositories (e.g., anonymous.4open.science)

- [ ] Yazar adları başlık sayfasından kaldırıldı
- [ ] Yazar affiliasyonları başlık sayfasından kaldırıldı
- [ ] Teşekkürler bölümü kaldırıldı veya "Teşekkürler inceleme için çıkarıldı" ile değiştirildi
- [ ] Öz-atıflar kimliği açığa çıkarmıyor ("Önceki çalışmamızda [12]..." → "Önceki çalışmada [12]...")
- [ ] Yazarları tanımlayan finansman teşekkürleri kaldırıldı
- [ ] Dosya meta verileri kontrol edildi: yazar adı PDF belge özelliklerine gömülü değil
- [ ] Tamamlayıcı materyaller (varsa) de anonimleştirildi
- [ ] Yazarları tanımlayan GitHub veya veri seti bağlantıları anonimleştirildi

---

## Step 3 — Reference Format Verification / Referans Format Doğrulaması

Check the conference's required reference format. The four most common:

Konferansın gerekli referans formatını kontrol et. En yaygın dört format:

**ACM format** — Used for CHI, CSCW, UIST, and most ACM venues. Uses numbered references [1], [2]. ACM provides a BibTeX style file.

**ACM formatı** — CHI, CSCW, UIST ve çoğu ACM mekanı için kullanılır. Numaralı referanslar [1], [2] kullanır.

**IEEE format** — Used for most IEEE conferences. Also numbered [1], [2]. Author initials before surname. IEEE provides a BibTeX style file.

**IEEE formatı** — Çoğu IEEE konferansı için kullanılır. Aynı zamanda numaralı [1], [2]. Soyad öncesinde yazar baş harfleri.

**APA format** — Less common in CS/engineering conferences; more common in social science and education venues. Author-date: (Author, Year).

**APA formatı** — CS/mühendislik konferanslarında daha az yaygın; sosyal bilim ve eğitim mekanlarında daha yaygın.

**Chicago / venue-specific** — Check the CfP for any non-standard format.

**Chicago / mekana özgü** — Standart olmayan format için BÇ'yi kontrol et.

For each reference in your list, verify:
- [ ] Author names formatted correctly for the style
- [ ] Year placement correct
- [ ] Journal/proceedings name complete (not abbreviated unless the style requires it)
- [ ] Volume, issue, page numbers present (for journal citations)
- [ ] DOI or URL present where required
- [ ] Conference name properly formatted (ACM/IEEE proceedings have specific formats)

Listenizde her referans için doğrula:
- [ ] Yazar adları stil için doğru biçimlendirilmiş
- [ ] Yıl yerleşimi doğru
- [ ] Dergi/bildiri kitabı adı eksiksiz
- [ ] Cilt, sayı, sayfa numaraları mevcut
- [ ] Gerekli yerde DOI veya URL mevcut
- [ ] Konferans adı doğru biçimlendirilmiş

---

## Step 4 — Complete the Submission Checklist / Gönderim Kontrol Listesini Tamamla

Open `submission_checklist.md` created in Phase 0. Go through every item.

Aşama 0'da oluşturulan `submission_checklist.md` dosyasını aç. Her öğeyi gözden geçir.

Common items that are missed at the last moment:

Son anda kaçırılan yaygın öğeler:

- [ ] Paper is in the required file format (PDF is standard; check if source files also required)
- [ ] PDF is within file size limit (some systems reject files over 10MB or 20MB)
- [ ] Author metadata is complete in the submission system (name, affiliation, email, ORCID for all authors)
- [ ] Paper title in submission system matches title on the paper exactly
- [ ] Abstract in submission system matches abstract on the paper exactly (some systems require re-entry)
- [ ] Keywords entered in the submission system
- [ ] Subject area / topic area selected correctly
- [ ] Conflict of interest declared (most systems require this)
- [ ] Co-authors confirmed and acknowledged in the submission system

- [ ] Bildiri gerekli dosya formatında (PDF standarttır; kaynak dosyaların da gerekli olup olmadığını kontrol et)
- [ ] PDF dosya boyutu limitinin dahilinde
- [ ] Gönderim sistemindeki yazar meta verisi eksiksiz
- [ ] Gönderim sistemindeki bildiri başlığı bildiri üzerindeki başlıkla tam eşleşiyor
- [ ] Gönderim sistemindeki özet bildiri üzerindeki özet ile tam eşleşiyor
- [ ] Gönderim sistemine anahtar kelimeler girildi
- [ ] Konu alanı / tema alanı doğru seçildi
- [ ] Çıkar çatışması beyan edildi
- [ ] Ortak yazarlar gönderim sisteminde onaylanmış ve kabul edilmiş

---

## Step 5 — Final Proofread / Son Düzeltme Okuma

Read the final PDF — not the source file — once from beginning to end. PDFs sometimes have rendering issues that are invisible in the source.

Son PDF dosyasını — kaynak dosyayı değil — başından sonuna bir kez oku. PDF'ler bazen kaynak dosyada görünmez olan oluşturma sorunları içerebilir.

Check: figures readable at print size, tables not overflowing margins, no hyphenation errors in headings, no broken references ([?] or [Author?]).

Kontrol et: şekiller baskı boyutunda okunabilir, tablolar kenar boşluklarını aşmıyor, başlıklarda kötü heceleme hatası yok, bozuk referans yok ([?] veya [Yazar?]).

---

## Step 6 — Submit / Gönder

Submit through the conference system before the deadline. Do not wait until the last hour — submission systems slow under load and sometimes go down.

Son tarihten önce konferans sistemi aracılığıyla gönder. Son saate kadar bekleme — gönderim sistemleri yük altında yavaşlar ve bazen çöker.

After submission:
- Download the confirmation email and save it
- Save the submission ID number
- Record the expected notification date

Gönderdikten sonra:
- Onay e-postasını indir ve kaydet
- Gönderim ID numarasını kaydet
- Beklenen bildirim tarihini kaydet

---

## Completion Criteria / Tamamlanma Kriterleri

- [ ] Paper is within the page limit.
- [ ] Anonymization check completed (double-blind) or confirmed not required.
- [ ] All references formatted correctly for the conference style.
- [ ] `submission_checklist.md` from Phase 0 is fully completed.
- [ ] Final PDF proofread and verified.
- [ ] Paper submitted through the conference system.
- [ ] Submission confirmation saved.

- [ ] Bildiri sayfa limiti dahilinde.
- [ ] Anonimleştirme kontrolü tamamlandı (çift-kör) veya gerekli olmadığı onaylandı.
- [ ] Tüm referanslar konferans stili için doğru biçimlendirildi.
- [ ] Aşama 0'dan `submission_checklist.md` tamamen tamamlandı.
- [ ] Son PDF düzeltme okundu ve doğrulandı.
- [ ] Bildiri konferans sistemi aracılığıyla gönderildi.
- [ ] Gönderim onayı kaydedildi.

When the submission confirmation is in hand, Phase 4 is complete. The paper is submitted.

Gönderim onayı elde tutulduğunda, Aşama 4 tamamdır. Bildiri gönderilmiştir.
