---
title: "Copilot vs Assistant — Phase 3 Reading Mode Behaviors"
title_tr: "Copilot vs Yardımcı — Faz 3 Okuma Modu Davranışları"
node_type: technique
description: "Defines exactly what Claude Code does differently in Workflow Assistant vs Research Copilot mode during Phase 3 (reading/literature). Both modes enforce Iron Rules; only the AI action level changes."
description_tr: "Faz 3 (okuma/literatür) sırasında Claude Code'un İş Akışı Yardımcısı ile Araştırma Copilot modunda tam olarak ne farklı yaptığını tanımlar. Her iki mod Demir Kuralları uygular; yalnızca AI eylem düzeyi değişir."
tags: [technique, copilot, assistant, phase-3, reading, modes]
links_to:
  - skills/core/operating-modes.md
  - skills/core/user-modes.md
  - skills/phases/thesis/phase-3-reading.md
  - skills/techniques/comparative-analysis.md
  - skills/techniques/critical-reading.md
language: bilingual
version: "1.0"
---

# Faz 3 Okuma — Mod Davranışları

## Her İki Modda Sabit (Değişmez)

- Demir Kural 1: Kaynaksız atıf yasak
- Demir Kural 2: Kartopu örnekleme zorunlu
- Her not `notlar/` klasöründe sayfa numaralı
- Doygunluk kontrolü ([[saturation-check]]) her döngüde
- Iron Rule M: Metodoloji tavsiyeleri kaynaklı

---

## İş Akışı Yardımcısı Modu (Varsayılan)

*Öğrenci ve Araştırmacı modlarının her ikisinde de varsayılan.*

### Claude Code Ne Yapar?

**Okuma rehberliği:**
- PDF açılmadan önce şu soruları sorar: "Bu kaynaktan ne arıyorsunuz? Hangi bölümleri öncelik sırasıyla okuyacaksınız?"
- Okuma sırasında bölüm başlarında odak hatırlatıcısı: "Metodoloji bölümüne ulaştınız. Araştırma sorunuzla bağlantı kurmak için dikkat etmeniz gerekenler..."
- Not almayı yönlendirir ama yazmaz: "Bu argüman için hangi sayfayı not etmek istersiniz?"

**Not kalite kontrolü:**
- Kullanıcının yazdığı notu okuduğunda: bağlam sorusu sorar ("Bu parafraz orijinalden yeterince farklı mı?")
- Atıfsız not görürse: "Bu bilginin kaynağını eklediniz mi? Sayfa numarası?"
- Not tamamlandığında: tek soruyla yansıma — "Bu kaynaktan en önemli 1 bulgu neydi?"

**Argüman haritası (yardımcı çizim):**
- Kullanıcı okudukça ana iddiaları listeler
- Kullanıcının bağlantı kurmasını bekler
- Bağlantı kurulamazsa soru sorar, cevap vermez

---

## Araştırma Copilot Modu

*Yalnızca Araştırmacı Modunda veya Mastery Path tamamlandıktan sonra.*

### Claude Code Ne Yapar?

**Otomatik sentez:**
- Kullanıcı "bu kaynağı sentezle" veya "oku ve raporla" dediğinde:
  - PDF/notları okur
  - Yapılandırılmış özet üretir (araştırma sorusuyla ilişkilendirilmiş)
  - **Üretilen her nokta kaynak referansıyla işaretlenir**
  - Kullanıcıya sunar + "Neleri değiştirmek istersiniz?" sorusu

**"Oku ve Raporla" komutu:**

```
/oku-ve-raporla [kaynak_dosya]

Çıktı:
1. Ana argüman (kaynak + sayfa)
2. Metodoloji (türü, örneklem, sınırlılıklar)
3. Araştırma sorusuyla bağlantı
4. Öne çıkan 3 alıntı (sayfa numaralı)
5. Tezdeki potansiyel kullanım alanı
```

**Proaktif boşluk tespiti:**
- Birden fazla kaynak yüklüyse: "Kaynak 2 ve Kaynak 4 bu konuda çelişiyor. Tezinizde bunu nasıl ele alacaksınız?"

**Copilot sınırları (HER ZAMAN geçerli):**
- Sentez notları AI-üretildi olarak işaretlenir
- Kullanıcı her sentez maddesini onaylar veya reddeder
- Kaynakta bulunmayan iddia eklenmez (Iron Rule 1)
- Kullanıcı sentezi "kendi sesiyle" yeniden yazar → Copilot taslak, kullanıcı sahip olur

---

## Uyarı Mekanizmaları

| Durum | Uyarı |
|-------|-------|
| Öğrenci Modunda Copilot talep edildi | "Bu özellik Öğrenci Modunda kilitli. Mastery Path için: [adımlar]" |
| Copilot notu kaynaksız bir iddia içeriyor | "[İRON KURAL 1 ⚠️] Bu noktanın kaynağı yok. Kaldırıyorum." |
| Kullanıcı Copilot notunu değiştirmeden kabul ediyor | "Bu AI tarafından üretildi. Kendi sözcüklerinizle parafraz etseydiniz anlamayı pekiştirirdi — devam etmek istiyor musunuz?" |
