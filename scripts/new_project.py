#!/usr/bin/env python3
"""
new_project.py — TezAtlas Template Scaffolding Command

One-command project bootstrap:
  python3 scripts/new_project.py --type article --lang tr --field law --title "My Paper"

Creates a minimal but practical project scaffold for thesis/article workflows.
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


DOCUMENT_TYPES = {
    "thesis": ("Tez", "Thesis"),
    "article": ("Makale", "Article"),
    "original-article": ("Özgün Araştırma Makalesi", "Original Article"),
    "case-report": ("Olgu Sunumu", "Case Report"),
    "conference": ("Konferans Bildirisi", "Conference Paper"),
    "lit-review": ("Literatür Derlemesi", "Literature Review"),
    "report": ("Araştırma Raporu", "Research Report"),
    "book-chapter": ("Kitap Bölümü", "Book Chapter"),
    "grant-proposal": ("Hibe Başvurusu", "Grant Proposal"),
    "research-proposal": ("Araştırma Önerisi", "Research Proposal"),
}

FIELDS = [
    "economics", "law", "education", "psychology", "sociology", "history",
    "engineering", "medicine", "management", "political-science", "linguistics",
    "philosophy", "literature", "computer-science", "environmental-science",
    "other",
]

TODAY = date.today().isoformat()
MEDICAL_DOC_TYPES = {"thesis", "article", "original-article", "case-report", "lit-review"}


def build_status(doc_type: str, lang: str, field: str, title: str) -> str:
    lang_label = {"tr": "Türkçe", "en": "English", "both": "Bilingual"}.get(lang, lang)
    return f"""# STATUS.md — TezAtlas Proje Durumu

## Proje Kimliği

```yaml
title: "{title}"
document_type: {doc_type}
field: {field}
language: {lang_label}
created: "{TODAY}"
last_updated: "{TODAY}"
current_phase: 0
```

## Faz İlerlemesi

| Faz | Ad | Durum | Tamamlanma |
|-----|----|-------|------------|
| 0 | Başlangıç / Onboarding | ✅ Tamamlandı | {TODAY} |
| 1 | Araştırma Sorusu | ⏳ Devam ediyor | — |
| 2 | Metodoloji (ampirik ise) | ⏸ Bekliyor | — |
| 3 | Okuma | ⏸ Bekliyor | — |
| 4 | Yapı / Outline | ⏸ Bekliyor | — |
| 5 | Yazım | ⏸ Bekliyor | — |
| 6 | Revizyon | ⏸ Bekliyor | — |
| 7 | Finalizasyon | ⏸ Bekliyor | — |

## Kaynak Havuzu

```yaml
sources:
  total_collected: 0
  read: 0
  active: 0
  deferred: 0
  saturation_reached: false
```

## Yazım Takibi

```yaml
writing_schedule:
  current_streak: 0
  longest_streak: 0
  last_session_date: null
  total_sessions: 0

wellbeing:
  last_session_date: "{TODAY}"
  days_inactive: 0
  goals_missed_consecutive: 0
  last_advisor_checkpoint: null
  attrition_risk: low

motivation:
  why_statement: null
  recorded_at: null
```

## Notlar

<!-- Danışman geri bildirimleri, kararlar, önemli notlar -->
"""


def build_reading_report(title: str) -> str:
    return f"""# READING_REPORT.md — Okuma Raporu

**Proje:** {title}
**Başlangıç:** {TODAY}

## Kaynak Envanteri

| # | Yazar(lar) | Yıl | Başlık | Durum | Alaka | Notlar |
|---|-----------|-----|--------|-------|-------|--------|
| 1 | | | | 🔵 Havuzda | | |

**Durum kodları:** 🔵 Havuzda → 🟡 Okunuyor → 🟢 Tamamlandı → 🔴 Elendi

## Doygunluk Takibi

| Tur | Yeni Kaynak | Önceden Bilinen | Doygunluk % |
|-----|-------------|-----------------|-------------|
| 1 | | | |

**Doygunluk hedefi:** Yeni kaynakların ≥ %80'i önceden bilinen → okuma tamamdır.

## Özet Notlar

<!-- Okuma süreci notları -->
"""


def build_arguments(title: str) -> str:
    return f"""# ARGUMENTS.md — Argüman İzleyici

**Proje:** {title}
**Son güncelleme:** {TODAY}

## Aktif İddialar

| # | İddia | Kaynak | Kanıt Gücü | Durum |
|---|-------|--------|-----------|-------|
| 1 | | | ○ | 🔴 BOŞLUK |

**Kanıt gücü:** ●●● Güçlü · ●●○ Orta · ●○○ Zayıf · ○ Kanıt yok

## Çelişkiler

| # | Konu | Kaynak A | Kaynak B | Ele Alış |
|---|------|---------|---------|---------|
| | | | | |

## Bekleyen İtirazlar

- [ ] Güçlü karşı argüman eklenecek
"""


def build_methodology(title: str) -> str:
    return f"""# METODOLOJI.md — Araştırma Metodolojisi

**Proje:** {title}
**Tarih:** {TODAY}

## Araştırma Tasarımı
- Tasarım türü: [...]
- Araştırma sorusu / hipotez: [...]

## Örneklem
- Hedef popülasyon: [...]
- Örnekleme yöntemi: [...]
- n: [...] | Güç analizi: [G*Power — doldur]

## Veri Toplama
- Araç: [...]
- Kaynak: [...]

## Analiz Planı
- Yöntem: [...]
- Yazılım: [...]
- Raporlama: [Vancouver / hedef dergi kuralı]
"""


def build_thesis_master_plan(title: str, field: str) -> str:
    return f"""# THESIS_MASTER_PLAN.md — Tıp Tezi Ana Planı

**Proje:** {title}
**Alan:** {field}
**Tarih:** {TODAY}

## Tez Kimliği
- Çalışma tipi: [retrospektif / prospektif / kesitsel / kohort / vaka-kontrol / deneysel]
- Ana araştırma sorusu: [...]
- Birincil sonlanım: [...]
- İkincil sonlanımlar: [...]

## Çekirdek Yol Haritası
- [ ] Araştırma sorusunu kilitle
- [ ] Dahil etme / dışlama kriterlerini yaz
- [ ] Etik kurul durumunu netleştir
- [ ] Veri sözlüğünü çıkar
- [ ] İstatistik planını netleştir
- [ ] Tez bölüm yapısını sabitle
- [ ] Kaynak havuzunu kur
- [ ] İlk taslak takvimini çıkar

## Zorunlu Kontroller
- [ ] Etik kurul / izin
- [ ] KVKK / anonimleştirme planı
- [ ] STROBE / CONSORT / PRISMA / CARE uygun rehber seçimi
- [ ] Vancouver veya hedef dergi stilinin teyidi

## Bölüm Planı
1. Giriş
2. Genel Bilgiler / Literatür
3. Gereç ve Yöntem
4. Bulgular
5. Tartışma
6. Sonuç
7. Kaynaklar
8. Ekler
"""


def build_manuscript_template(title: str, doc_type: str) -> str:
    if doc_type == "case-report":
        return f"""# MANUSCRIPT.md — Olgu Sunumu Taslağı

**Başlık:** {title}
**Tarih:** {TODAY}

## Title

## Abstract (unstructured, <250 words)

## Introduction
- Neden bu olgu önemli?
- Acil tıp literatüründeki boşluk ne?

## Case Presentation
- Başvuru şikayeti
- Öykü
- Fizik muayene
- Tetkikler
- Ayırıcı tanı
- Tedavi / girişim
- Klinik seyir / sonuç

## Discussion
- Literatürde benzer olgular
- Bu olgunun ayırt edici noktası
- Acil servis pratiğine katkı

## Conclusion

## Patient Consent / Ethics
- [ ] Hasta onamı alındı
- [ ] Kimliksizleştirme yapıldı

## References
"""

    return f"""# MANUSCRIPT.md — Makale Taslağı

**Başlık:** {title}
**Tarih:** {TODAY}

## Title Page
- Başlık
- Kısa başlık
- Yazarlar ve kurumlar
- Sorumlu yazar

## Structured Abstract
- Objective
- Methods
- Results
- Conclusion

## Keywords
- 3-6 anahtar kelime

## Introduction
- Klinik problem
- Literatür boşluğu
- Çalışma amacı / hipotez

## Methods
- Çalışma tasarımı
- Ortam ve zaman
- Dahil etme / dışlama kriterleri
- Değişkenler
- Sonlanımlar
- İstatistik analiz
- Etik kurul

## Results
- Örneklem akışı
- Ana bulgular
- Tablolar / şekiller

## Discussion
- Ana bulguların yorumu
- Literatür ile karşılaştırma
- Klinik anlam
- Kısıtlılıklar

## Conclusion

## Funding / Conflicts / Data Statement
- Fonlama:
- Çıkar çatışması:
- Veri paylaşımı:

## References
"""


def build_reporting_checklist(doc_type: str) -> str:
    guide = {
        "original-article": "STROBE / CONSORT / TREND (tasarıma göre)",
        "article": "STROBE / CONSORT / PRISMA (çalışma tipine göre)",
        "case-report": "CARE",
        "lit-review": "PRISMA",
        "thesis": "STROBE / CONSORT / PRISMA / CARE (uygun olanı seç)",
    }.get(doc_type, "Uygun EQUATOR rehberi")
    return f"""# REPORTING_CHECKLIST.md — Raporlama Kontrolü

**Tarih:** {TODAY}
**Önerilen rehber:** {guide}

## Çalışma Tasarımı
- [ ] Tasarım açıkça belirtildi
- [ ] Birincil sonlanım tanımlandı
- [ ] İkincil sonlanımlar tanımlandı

## Etik
- [ ] Etik kurul / izin numarası yazıldı
- [ ] Bilgilendirilmiş onam durumu belirtildi
- [ ] Anonimleştirme açıklandı

## İstatistik
- [ ] Örneklem / güç analizi belirtildi
- [ ] Testler önceden tanımlandı
- [ ] Eksik veri yaklaşımı yazıldı
- [ ] p değeri / güven aralığı planı açıklandı

## Şeffaflık
- [ ] Fonlama belirtildi
- [ ] Çıkar çatışması belirtildi
- [ ] Yapay zeka kullanımı belirtildi (varsa)
- [ ] Veri paylaşım beyanı eklendi
"""


def build_ajem_quick_guide() -> str:
    return f"""# AJEM_QUICK_GUIDE.md — American Journal of Emergency Medicine Hızlı Rehber

**Kaynak:** Guide for Authors (AJEM)
**Son işleme tarihi:** {TODAY}

## Hızlı Uygunluk Kontrolü
- [ ] Çalışma acil tıp kapsamına giriyor
- [ ] Veri güncelliği uygun (genelde son 3 yıl içinde veri tercih edilir)
- [ ] Sonuçlar veriye dayanıyor
- [ ] Yöntem okuyucunun değerlendirebileceği ayrıntıda yazıldı
- [ ] Hedef makale tipi net seçildi

## Makale Türleri — Pratik Notlar
### Original Contribution
- Yaklaşık 2750–3000 kelime
- Power analysis güçlü şekilde teşvik edilir
- İlk sayfada en fazla 15 yazar

### Brief Report
- Yaklaşık 2000 kelime
- İlk sayfada en fazla 10 yazar

### Review
- Genelde davetli / önceden editörle teyit edilmesi iyi olur
- Yaklaşık 2750–3000 kelime
- En fazla 5 yazar

### Case Report
- Acil serviste yönetilmiş olgu olmalı
- EM literatürü için özgün değer taşımalı
- <1500 kelime
- Özet <250 kelime ve genelde yapılandırılmamış
- En fazla 5 yazar

## AJEM İçin Dikkat
- Nitel araştırma, patient satisfaction, quality assurance, didactics odaklı çalışmalar zayıf aday olabilir
- Çok eski veri setleri risklidir
- Acil servise pratik katkı net gösterilmeli
- Tartışma gereksiz uzamamalı; klinik mesaj net olmalı
"""


def build_journal_targets() -> str:
    return f"""# JOURNAL_TARGETS.md — Hedef Dergi Takibi

**Tarih:** {TODAY}

| Dergi | Makale Tipi | Kelime | Özet | Referans Stili | Durum | Not |
|------|-------------|--------|------|----------------|------|-----|
| AJEM | Original / Brief / Case Report | 2750-3000 / 2000 / <1500 | Structured veya type-specific | Vancouver benzeri medikal stil | 🎯 Öncelikli | Acil tıp odağı |

## AJEM İçin Hızlı Karar Soruları
- [ ] Çalışma acil tıp pratiğine doğrudan dokunuyor mu?
- [ ] Veri yeterince güncel mi?
- [ ] Mesaj kısa ve klinik olarak net mi?
- [ ] Makale tipi doğru seçildi mi?
"""


def build_submission_package() -> str:
    return """# SUBMISSION_PACKAGE.md — Gönderim Paketi

## Zorunlu Dosyalar
- [ ] Ana metin
- [ ] Başlık sayfası
- [ ] Cover letter
- [ ] Şekil / tablo dosyaları
- [ ] Etik kurul bilgisi
- [ ] Çıkar çatışması beyanı
- [ ] Yazar katkıları
- [ ] Veri paylaşım / AI kullanım beyanı

## Son Kontrol
- [ ] Hedef dergi formatı ile uyumlu
- [ ] Kelime sınırı uygun
- [ ] Referans stili uygun
- [ ] Yazar listesi uygun
"""


def build_title_page(title: str) -> str:
    return f"""# TITLE_PAGE.md — Başlık Sayfası

## Manuscript Title
{title}

## Running Title
[50 karakter civarı kısa başlık]

## Authors
1. [Ad Soyad], [Kurum], [ORCID]
2. [Ad Soyad], [Kurum], [ORCID]

## Corresponding Author
- Ad Soyad:
- Kurum:
- Adres:
- E-posta:
- Telefon:

## Author Affiliations
- [Kurum 1]
- [Kurum 2]

## Word Count
- Main text:
- Abstract:

## Keywords
- [3-6 anahtar kelime]
"""


def build_cover_letter(title: str, doc_type: str) -> str:
    article_label = {
        "original-article": "original article",
        "article": "article",
        "case-report": "case report",
    }.get(doc_type, "manuscript")
    return f"""# COVER_LETTER.md — Cover Letter Taslağı

Dear Editor,

We are pleased to submit our {article_label}, titled **\"{title}\"**, for consideration for publication.

This manuscript addresses a clinically relevant emergency medicine question and we believe it fits the journal's scope. The work is original, has not been published previously, and is not under consideration elsewhere.

## Why this manuscript fits the journal
- [Acil tıp pratiğine doğrudan katkı]
- [Temel klinik mesaj]
- [Literatürde kapattığı boşluk]

## Declarations
- All authors approved the final manuscript.
- Ethical approval / patient consent information is reported in the manuscript.
- Conflicts of interest are disclosed.
- Generative AI use, if any, is transparently declared.

Thank you for your consideration.

Sincerely,

[Corresponding Author Name]
[Institution]
[Email]
"""


def build_author_contributions() -> str:
    return """# AUTHOR_CONTRIBUTIONS.md — Yazar Katkıları

## CRediT Roles

| Author | Conceptualization | Methodology | Data Curation | Formal Analysis | Writing - Original Draft | Writing - Review & Editing | Supervision |
|--------|-------------------|-------------|---------------|-----------------|--------------------------|----------------------------|-------------|
| A1 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| A2 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

## Narrative Summary
- [Yazar 1] contributed to ...
- [Yazar 2] contributed to ...
"""


def build_ethics_statement(doc_type: str) -> str:
    consent_line = "- [ ] Written informed consent was obtained from the patient." if doc_type == "case-report" else "- [ ] Informed consent requirement/status stated."
    return f"""# ETHICS_AND_DISCLOSURES.md — Etik ve Beyanlar

## Ethics Approval
- [ ] Institutional Review Board / Ethics Committee approval stated
- Approval number:
- Approval date:

## Consent
{consent_line}

## Conflict of Interest
- [ ] Conflict of interest statement added

## Funding
- [ ] Funding/support statement added

## Data Availability
- [ ] Data availability statement added

## Generative AI Use
- [ ] AI use statement added when applicable

## Patient Privacy / De-identification
- [ ] Direct identifiers removed
- [ ] Dates/details sufficiently anonymized
"""


def build_ajem_submission_checklist(doc_type: str) -> str:
    abstract_rule = "Unstructured abstract <250 words" if doc_type == "case-report" else "Structured abstract prepared"
    word_rule = {
        "original-article": "~2750–3000 words",
        "article": "journal article type checked",
        "case-report": "<1500 words",
    }.get(doc_type, "journal-specific limit checked")
    author_rule = {
        "original-article": "≤15 authors on first page",
        "case-report": "≤5 authors",
        "article": "author count checked for selected type",
    }.get(doc_type, "author count checked")
    return f"""# AJEM_SUBMISSION_CHECKLIST.md — AJEM Gönderim Kontrol Listesi

## Scope Fit
- [ ] Study clearly fits emergency medicine scope
- [ ] Clinical relevance for ED practice is explicit
- [ ] Dataset/study question is sufficiently current

## Article Type Fit
- [ ] Selected article type is correct
- [ ] Word count target met: {word_rule}
- [ ] Abstract rule met: {abstract_rule}
- [ ] Author count rule met: {author_rule}

## Scientific Reporting
- [ ] Methods detailed enough for reviewer evaluation
- [ ] Conclusions supported by presented data
- [ ] Appropriate reporting guideline applied (STROBE/CONSORT/CARE/PRISMA)
- [ ] Power analysis included or justified when relevant

## Required Declarations
- [ ] Ethics approval / consent reported
- [ ] Conflict of interest statement included
- [ ] Funding statement included
- [ ] AI use statement included if applicable

## Files Ready
- [ ] MANUSCRIPT.md adapted to final submission file
- [ ] TITLE_PAGE.md completed
- [ ] COVER_LETTER.md completed
- [ ] AUTHOR_CONTRIBUTIONS.md completed
- [ ] ETHICS_AND_DISCLOSURES.md completed
"""


def create_project(output_dir: Path, doc_type: str, lang: str, field: str, title: str, empirical: bool) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    for subdir in ["sources", "notes", "cikti"]:
        d = output_dir / subdir
        d.mkdir(exist_ok=True)
        (d / ".gitkeep").touch()

    files = {
        "STATUS.md": build_status(doc_type, lang, field, title),
        "READING_REPORT.md": build_reading_report(title),
        "ARGUMENTS.md": build_arguments(title),
    }

    if empirical or field == "medicine" or doc_type in MEDICAL_DOC_TYPES:
        files["METODOLOJI.md"] = build_methodology(title)

    if doc_type == "thesis" and field == "medicine":
        files["THESIS_MASTER_PLAN.md"] = build_thesis_master_plan(title, field)

    if doc_type in {"article", "original-article", "case-report"}:
        files["MANUSCRIPT.md"] = build_manuscript_template(title, doc_type)
        files["SUBMISSION_PACKAGE.md"] = build_submission_package()
        files["TITLE_PAGE.md"] = build_title_page(title)
        files["COVER_LETTER.md"] = build_cover_letter(title, doc_type)
        files["AUTHOR_CONTRIBUTIONS.md"] = build_author_contributions()
        files["ETHICS_AND_DISCLOSURES.md"] = build_ethics_statement(doc_type)

        if field == "medicine":
            files["AJEM_SUBMISSION_CHECKLIST.md"] = build_ajem_submission_checklist(doc_type)

    if field == "medicine" or doc_type in MEDICAL_DOC_TYPES:
        files["REPORTING_CHECKLIST.md"] = build_reporting_checklist(doc_type)
        files["JOURNAL_TARGETS.md"] = build_journal_targets()
        files["AJEM_QUICK_GUIDE.md"] = build_ajem_quick_guide()

    gitignore_path = output_dir / ".gitignore"
    if not gitignore_path.exists():
        gitignore_path.write_text(
            "# TezAtlas — kişisel veri\nsources/*\n!sources/.gitkeep\n*.pdf\n.env\nnotlar/\n",
            encoding="utf-8",
        )

    created, skipped = [], []
    for filename, content in files.items():
        fp = output_dir / filename
        if fp.exists():
            skipped.append(filename)
        else:
            fp.write_text(content, encoding="utf-8")
            created.append(filename)

    doc_tr, doc_en = DOCUMENT_TYPES.get(doc_type, ("Belge", "Document"))
    print("\n✅ TezAtlas Projesi Oluşturuldu / Project Created")
    print(f"   Tür / Type:  {doc_en} ({doc_tr})")
    print(f"   Alan / Field: {field}")
    print(f"   Dil / Lang:  {lang}")
    print(f"   Dizin / Dir: {output_dir}\n")

    if created:
        print("📄 Oluşturulan dosyalar / Created files:")
        for f in created:
            print(f"   + {f}")

    if skipped:
        print("\n⏭️  Atlandı (zaten mevcut) / Skipped (already exists):")
        for f in skipped:
            print(f"   = {f}")

    print("\n🚀 Başlamak için / To start:")
    print(f"   cd {output_dir}")
    print("   # Claude Code'u aç ve /tezatlas komutunu çalıştır")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="TezAtlas — Proje iskele oluşturucu / Project scaffolding tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Örnekler / Examples:
  python3 scripts/new_project.py --type article --lang tr --field law --title "Türk Hukukunda AI"
  python3 scripts/new_project.py --type thesis --lang tr --field medicine --title "Acil Serviste ..." --empirical
  python3 scripts/new_project.py --type original-article --lang en --field medicine --title "Emergency Department ..."
  python3 scripts/new_project.py --type case-report --lang en --field medicine --title "A Rare ED Case"
        """,
    )
    parser.add_argument("--type", choices=list(DOCUMENT_TYPES.keys()), required=True, help="Belge türü / Document type")
    parser.add_argument("--lang", choices=["tr", "en", "both"], default="tr", help="Çalışma dili / Working language (default: tr)")
    parser.add_argument("--field", choices=FIELDS, default="other", help="Akademik alan / Academic field (default: other)")
    parser.add_argument("--title", default="[Başlık Belirlenmedi]", help="Çalışma başlığı / Working title")
    parser.add_argument("--empirical", action="store_true", help="Ampirik çalışma — METODOLOJI.md oluştur")
    parser.add_argument("--output", type=Path, default=Path("."), help="Çıktı dizini / Output directory (default: current dir)")

    args = parser.parse_args()
    create_project(args.output, args.type, args.lang, args.field, args.title, args.empirical)


if __name__ == "__main__":
    main()
