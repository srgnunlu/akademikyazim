---
title: "Attrition Prevention — Risk Signal Detection"
title_tr: "Bırakma Önleme — Risk Sinyali Tespiti"
node_type: core
description: "Detects early warning signs of doctoral attrition (inactivity, missed goals, isolation) at session start by reading STATUS.md. Triggers gentle, non-punitive check-in. Based on Lovitts (2001): 40-50% PhD attrition linked to isolation and loss of self-efficacy."
description_tr: "Doktora bırakma erken uyarı sinyallerini (hareketsizlik, kaçırılan hedefler, izolasyon) oturum başında STATUS.md okuyarak tespit eder. Nazik, cezalandırıcı olmayan kontrol başlatır. Lovitts (2001): Doktora bırakma %40-50, izolasyon ve öz-yeterlilik kaybıyla bağlantılı."
tags: [core, attrition-prevention, wellbeing, session-start, lovitts, risk-detection]
links_to:
  - skills/core/session-continuity.md
  - skills/core/user-modes.md
  - skills/techniques/writing-scheduler.md
language: bilingual
version: "1.0"
---

# Bırakma Önleme — Risk Sinyali Tespiti

## Araştırma Temeli

**Lovitts (2001) — "Leaving the Ivory Tower":** Doktora bırakmanın %40-50'si yetkinlik eksikliğinden değil; izolasyon, öz-yeterlilik kaybı ve danışman ilişkisinin kopmasından kaynaklanır.

**Zimmerman (2002) — SRL:** Öz-düzenleyici döngü bozulduğunda (hedef → strateji → yansıma zinciri kırılınca) akademik ilerleme durur, kaygı artar.

**Müdahale:** Erken ve hafif. Bırakma kararı genellikle aylar içinde oluşur — oturum aralıklarındaki sinyaller yakalanabilir.

---

## Risk Sinyalleri / Risk Signals

Oturum başında `STATUS.md` okunurken şu üç sinyal kontrol edilir:

### Sinyal 1 — Uzun Hareketsizlik / Prolonged Inactivity

```python
# Pseudocode — session start check
days_inactive = today - status["last_session_date"]

if days_inactive > 60:   # risk: YÜKSEK
    trigger = "long_absence"
elif days_inactive > 14: # risk: ORTA
    trigger = "two_week_gap"
elif days_inactive > 7:  # risk: DÜŞÜK
    trigger = "one_week_gap"
```

### Sinyal 2 — Kaçırılan Hedefler / Missed Goals

`STATUS.md`'deki `goals_missed_consecutive` sayacı takip edilir:

- 3+ ardışık oturumda hedef kaçırıldı → uyarı
- Hedefe/sonuca değil kontrole atıf yap: "Strateji mi değişmeli?"

### Sinyal 3 — Danışman Boşluğu / Advisor Gap

`STATUS.md`'deki `last_advisor_checkpoint` tarihi kontrol edilir:

- Tez projesi + son checkpoint > 6 hafta → hatırlatıcı
- Öğrenci modu + checkpoint atlandı → yumuşak engel

---

## Tepki Protokolü / Response Protocol

### 1-3 Gün Ara (Normal)

```
Hoş geldin! [N] günlük aranın ardından devam ediyoruz.
Son bıraktığın yer: [STATUS.md'den]
```

### 7-14 Gün Ara (Hafif İşaret)

```
[N] günlük aranın ardından hoş geldin.
Bir şeyler zorlaştı mı? Devam etmek için ne gerekiyor?

Son hedef: [STATUS.md'den]
Şu an nereden başlamak istersin?
```

### 14-60 Gün Ara (Orta Risk)

```
[N] gündür görüşmemiştik. Umarım iyisindir.

Araştırmanın nerede olduğunu hatırlatayım:
📍 Faz: [X] | Tamamlanan: [Y]%
📚 Kaynaklar: [N] okundu

Araştırma dışında bir şeyler oluyor mu?
Buradan devam etmek için bir adım planlamak ister misin?
```

### 60+ Gün Ara (Yüksek Risk)

```
[N] gündür görüşmemiştik.

Projen hâlâ burada, seninle birlikte. Uzun bir ara genellikle
bir şeylerin değişmesi gerektiğine işaret eder.

Üç seçenek:
A) Kaldığımız yerden devam edelim
B) Projeyi yeniden değerlendirmek için konuşalım
C) Şimdilik bir kenara bırak — geldiğinde buradayız

Ne düşünüyorsun?
```

---

## Danışman Checkpoint Hatırlatıcısı

Tez projesi + son checkpoint > 6 hafta:

```
📅 Danışman görüşmesi: [SON TARİH] (X gün önce)

Araştırma danışmanınla görüşmek için iyi bir an.
Checkpoint şablonu: skills/templates/tpl-advisor-checkpoint.md

Bu hafta bir görüşme planlamak ister misin?
```

---

## Dil ve Ton Kuralları / Language Rules

**Kullanılmaz / Never use:**
- "Geride kaldın" / "You're behind"
- "Bu kadar zaman nasıl geçti?" / "What happened to all that time?"
- "Hedeflerine ulaşamadın" / "You failed to meet your goals"
- Sayısal ilerleme yüzdesi olumsuz çerçevede ("sadece %23 tamamlandı")

**Kullanılır / Always use:**
- Kontrol edilebilir nedenlere atıf: strateji, planlama — yetenek değil
- Seçenek sun, zorlama
- Başarısızlık değil: "zor bir dönem" veya "değişen koşullar"
- İlerlemeyi göster: "X paragraf yazdın, Y kaynak okudun"

---

## STATUS.md Risk Alanları

```yaml
wellbeing:
  last_session_date: "2026-02-27"
  days_inactive: 0
  goals_missed_consecutive: 0
  last_advisor_checkpoint: "2026-02-15"
  attrition_risk: low       # low | medium | high
  risk_acknowledged: false  # true = kullanıcı mesajı gördü
```

---

## Sınırlar / Limitations

Bu sistem:
- **Değil:** Klinik destek veya danışmanlık
- **Değil:** Araştırmacıyı izleme veya raporlama
- **Evet:** Oturum başında bağlam duyarlı, nazif hatırlatma

Ciddi zorluklarda önerilen: kurumun psikolojik danışmanlık servisi, doktora öğrenci topluluğu, danışmanla açık iletişim. TezAtlas araştırma akışı içinde destek verir — klinik destek değildir.
