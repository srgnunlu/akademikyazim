# AkademikYazım

AkademikYazım; tez, akademik makale, original article ve case report hazırlığı için geliştirilmiş sade bir araştırma-yazım iş akışı aracıdır.

Özellikle şunlara odaklanır:
- **Türkçe tıp tezi** hazırlığı
- **İngilizce medikal makale** yazımı
- **Original article** ve **case report** şablonları
- **AJEM** gibi sık kullanılan dergiler için gönderim hazırlığı
- kaynak, metodoloji ve gönderim dosyalarının düzenli tutulması

## Ne sağlar?

Bir proje başlatınca ihtiyaca göre hazır dosyalar üretir:
- `STATUS.md`
- `READING_REPORT.md`
- `ARGUMENTS.md`
- `METODOLOJI.md`
- `MANUSCRIPT.md`
- `TITLE_PAGE.md`
- `COVER_LETTER.md`
- `AUTHOR_CONTRIBUTIONS.md`
- `ETHICS_AND_DISCLOSURES.md`
- `REPORTING_CHECKLIST.md`
- `AJEM_QUICK_GUIDE.md`
- `AJEM_SUBMISSION_CHECKLIST.md`

## Hızlı Kurulum

```bash
git clone https://github.com/srgnunlu/akademikyazim.git
cd akademikyazim
python3 -m venv .venv
. .venv/bin/activate
pip install -U pip setuptools wheel
pip install -e .
```

Komut listesini görmek için:

```bash
tezatlas --list
```

> Not: CLI komutu şu an `tezatlas` olarak korunuyor. İleride istenirse yeniden adlandırılabilir.

## Hızlı Başlangıç

### 1) Türkçe tıp tezi

```bash
python3 scripts/new_project.py --type thesis --lang tr --field medicine --title "[Tez başlığı]" --output ./projem
```

### 2) Original article

```bash
python3 scripts/new_project.py --type original-article --lang en --field medicine --title "[Article title]" --output ./article
```

### 3) Case report

```bash
python3 scripts/new_project.py --type case-report --lang en --field medicine --title "[Case title]" --output ./case-report
```

## Tıp ve Dergi Odaklı Hazır Yapılar

Medikal projelerde otomatik olarak eklenebilen ana dosyalar:
- `REPORTING_CHECKLIST.md`
- `JOURNAL_TARGETS.md`
- `AJEM_QUICK_GUIDE.md`
- `AJEM_SUBMISSION_CHECKLIST.md`

Makale türlerinde ayrıca:
- `MANUSCRIPT.md`
- `SUBMISSION_PACKAGE.md`
- `TITLE_PAGE.md`
- `COVER_LETTER.md`
- `AUTHOR_CONTRIBUTIONS.md`
- `ETHICS_AND_DISCLOSURES.md`

## AJEM Notu

Bu repo içinde AJEM için pratik gönderim hazırlık dosyaları bulunur.
Özellikle şunları hızlı kontrol etmek için uygundur:
- makale tipi uyumu
- kelime sınırı
- abstract yapısı
- yazar sayısı
- etik / çıkar çatışması / funding beyanları
- case report gereklilikleri

## Dokümantasyon

Ek kullanım özeti:
- `docs/TURKISH_MEDICAL_WORKFLOWS.md`

## Geliştirme Durumu

Bu repo aktif olarak sadeleştirilen bir fork’tur.
Ana hedef, genel amaçlı büyük bir manifesto yerine gerçekten kullanılan akademik yazım akışlarını pratik hale getirmektir.

## Lisans

MIT
