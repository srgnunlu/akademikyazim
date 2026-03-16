# Turkish Medical Workflows / Türkçe Tıbbi İş Akışları

Bu doküman, TezAtlas fork'unun sık kullanılacak üç çekirdek kullanımını özetler:
- Türkçe tıp tezi
- akademik özgün araştırma makalesi
- olgu sunumu (case report)

## 1) Türkçe Tıp Tezi

Önerilen başlangıç:

```bash
tezatlas new --type thesis --lang tr --field medicine --title "[Tez başlığı]"
```

Beklenen çekirdek dosyalar:
- `STATUS.md`
- `READING_REPORT.md`
- `ARGUMENTS.md`
- `METODOLOJI.md`
- `THESIS_MASTER_PLAN.md`
- `REPORTING_CHECKLIST.md`
- `JOURNAL_TARGETS.md`
- `AJEM_QUICK_GUIDE.md`

Odak noktaları:
- araştırma sorusu ve birincil sonlanımın erken netleşmesi
- etik kurul ve anonimleştirme planı
- istatistik / güç analizi
- Vancouver veya hedef dergi stilinin baştan seçilmesi

## 2) Akademik Makale / Original Article

Önerilen başlangıç:

```bash
tezatlas new --type original-article --lang en --field medicine --title "[Article title]"
```

Ek dosyalar:
- `MANUSCRIPT.md`
- `SUBMISSION_PACKAGE.md`
- `REPORTING_CHECKLIST.md`
- `JOURNAL_TARGETS.md`
- `AJEM_QUICK_GUIDE.md`

Makale yazım iskeleti:
- Title page
- Structured abstract
- Introduction
- Methods
- Results
- Discussion
- Conclusion
- Funding / conflicts / data statement
- References

## 3) Case Report

Önerilen başlangıç:

```bash
tezatlas new --type case-report --lang en --field medicine --title "[Case title]"
```

Ek dosyalar:
- `MANUSCRIPT.md`
- `SUBMISSION_PACKAGE.md`
- `TITLE_PAGE.md`
- `COVER_LETTER.md`
- `AUTHOR_CONTRIBUTIONS.md`
- `ETHICS_AND_DISCLOSURES.md`
- `AJEM_SUBMISSION_CHECKLIST.md`
- `REPORTING_CHECKLIST.md`
- `AJEM_QUICK_GUIDE.md`

Olgu sunumunda kritik hatırlatmalar:
- hasta kimliği tamamen korunmalı
- onam durumu açık yazılmalı
- olgunun acil servis bağlamındaki özgün katkısı net olmalı
- tartışma kısa ama literatüre bağlı olmalı

## 4) AJEM Kısa Kullanım Notu

AJEM özellikle şu tür işler için mantıklı aday olabilir:
- acil servis gözlemleri
- retrospektif / prospektif klinik çalışmalar
- toksikoloji, travma, kritik bakım, resüsitasyon, pediatrik ve erişkin acil tıp çalışmaları
- acil serviste yönetilmiş anlamlı olgu sunumları

Pratik filtre:
- acil tıpla doğrudan ilişkili mi?
- veri güncel mi?
- klinik mesaj açık mı?
- makale tipi doğru seçildi mi?
