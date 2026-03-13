---
title: "User Modes — Student Mode vs Researcher Mode"
title_tr: "Kullanıcı Modları — Öğrenci Modu vs Araştırmacı Modu"
node_type: core
description: "Defines career-stage context modes that configure TezAtlas behavior at onboarding. Research Copilot (Guided Writing) is the default for all users. Student Mode adds SRL ritual and advisor checkpoints but does NOT lock Copilot."
description_tr: "TezAtlas davranışını onboarding'de yapılandıran kariyer aşaması bağlam modlarını tanımlar. Araştırma Yardımcısı (Guided Writing) tüm kullanıcılar için varsayılandır. Öğrenci Modu SRL ritüeli ve danışman checkpoint'leri ekler ama Copilot'u kilitlemez."
tags: [core, student-mode, researcher-mode, onboarding, copilot, srl, always-active]
links_to:
  - skills/core/operating-modes.md
  - skills/core/onboarding.md
  - skills/core/session-continuity.md
  - skills/core/anti-hallucination.md
language: bilingual
version: "1.0"
---

# Kullanıcı Modları / User Modes

## Onboarding'de Mod Seçimi

Faz 0'da (proje kimliği kurulurken) şu soruyu sor:

```
Sizi nasıl tanımlamalıyım?

A) Lisansüstü öğrenci (tez / ders ödevi / araştırma önerisi yazıyorum)
B) Araştırmacı / akademisyen (makale / rapor / hibe başvurusu yazıyorum)
C) Profesyonel (çalışma raporu / teknik doküman yazıyorum)
```

| Seçim | Atanan Mod | Belge türü örtüşmesi |
|-------|-----------|---------------------|
| A | **Öğrenci Modu** | Tez, Araştırma Önerisi, Poster |
| B | **Araştırmacı Modu** | Makale, Grant, Lit. Review, Conf., Book Chapter |
| C | **Araştırmacı Modu** | Rapor, Teknik Rapor |

Mod `STATUS.md`'ye yazılır ve oturum başında okunur.

---

## Öğrenci Modu (Student Mode)

### Özellikler

| Özellik | Öğrenci Modu |
|---------|-------------|
| Copilot — Guided Writing (A/B seçenekleri) | ✅ Tam erişim |
| Copilot — Akademik Yazım Notu | ✅ Tam erişim |
| Yapısal iskele | ✅ Tam erişim |
| Paragraf geri bildirimi | ✅ Tam erişim |
| Atıf hatırlatıcı | ✅ Tam erişim |
| AI Hakem İncelemesi (faz kapılarında) | ✅ Etkin |
| Deadline Modu (tez için) | ❌ HİÇBİR ZAMAN |
| Deadline Modu (ders ödevi) | ✅ Onaylanırsa |

### Öğrenci Modu Eklentileri

- **SRL Oturum Ritüeli:** Her oturum başında mikro-hedef, sonunda yansıma (önerilir)
- **AI Hakem checkpoint'leri:** Phase gate geçişi için AI Kıdemli Hakem veya danışman onayı
- **Argüman izleyici:** Her bölümde iddialar izlenir, boşluklar gösterilir

---

## Araştırmacı Modu (Researcher Mode)

### Açık Özellikler

| Özellik | Araştırmacı Modu |
|---------|-----------------|
| Copilot — Taslak üretimi | ✅ Mevcut (kullanıcı seçimiyle) |
| Copilot — Otomatik sentez | ✅ Mevcut |
| Copilot — Argüman üretimi notlardan | ✅ Mevcut |
| Hakem yorumu döngüsü | ✅ Mevcut |
| Çok yazarlı iş akışı | ✅ Mevcut |
| Deadline Modu (makale) | ✅ Mevcut |
| SRL ritüeli | Opsiyonel |

### Araştırmacı Modu Varsayılanları

- **Araştırma Yardımcısı (Copilot)** varsayılan — `/mode assistant` ile Düşünce Ortağı'na geçilebilir
- AI Hakem İncelemesi → Meslektaş incelemesi veya kendi kendine inceleme olarak da kullanılabilir
- Hakem dönüş döngüsü (Makale Faz 6) otomatik aktif

---

## Mod Geçişi

Mod değiştirmek için:
```
/mode student     → Öğrenci moduna geç (kısıtlamalar devreye girer)
/mode researcher  → Araştırmacı moduna geç
```

Mod geçişleri `STATUS.md`'ye kaydedilir.

---

## Mod Bilgisi STATUS.md'de

```yaml
user_mode: student        # student | researcher | professional
writing_mode: copilot     # copilot (Guided Writing) | assistant (Thought Partner)
mode_last_changed: "2026-02-27"
```

---

## Sabit Özellikler (Her Modda)

Demir Kurallar 1-9, Anti-Halüsinasyon Protokolü, Citation Verifier, Kaynak Politikası — kullanıcı modu veya yazım modundan bağımsız olarak her zaman aktif.
