---
title: "Autonomous Telemetry & Feedback System"
title_tr: "Otonom Telemetri ve Geri Bildirim Sistemi"
node_type: architecture
priority: medium
description: "Monitors user friction, tracks workflow efficiency, and generates an anonymized JSON feedback payload at the end of a project to help developers improve TezAtlas."
description_tr: "Kullanıcı zorlanmalarını izler, iş akışı verimliliğini takip eder ve geliştiricilerin TezAtlas'ı iyileştirmesine yardımcı olmak için proje sonunda anonimleştirilmiş bir JSON geri bildirim paketi oluşturur."
tags: [architecture, telemetry, feedback, ux, privacy, continuous-improvement]
links_to:
  - skills/phases/thesis/phase-7-finalization.md
  - skills/core/research-ethics.md
language: bilingual
version: "1.1"
---

# Autonomous Telemetry & Feedback System / Otonom Telemetri ve Geri Bildirim Sistemi

## Purpose / Amaç

**EN:** To enable TezAtlas to organically grow and improve based on real user experiences. This system detects where users struggle, what features they request, and compiles this into a strict, privacy-safe telemetry report at the end of the project.
**TR:** TezAtlas'ın gerçek kullanıcı deneyimlerine dayanarak organik olarak büyümesini ve gelişmesini sağlamak. Bu sistem, kullanıcıların nerede zorlandığını, hangi özellikleri talep ettiğini tespit eder ve bunu proje sonunda katı, gizlilik açısından güvenli bir telemetri raporunda derler.

---

## 1. Real-Time Background Tracking / Arka Planda Anlık Takip

**Trigger:** Active from project initialization (`/tezatlas`).
**AI Action:** The AI creates and maintains a `tezatlas_feedback.json` file in the root directory from day one.
*   **Continuous Updates:** Whenever a friction point (looping, confusion, error) is detected, the AI immediately updates the JSON file.
*   **Transparency:** The file is always visible to the user. They can inspect its content at any time to see exactly what is being logged.

*Note:* The AI notes the friction point descriptiveley but anonymized (e.g., "User struggled with defining the research question in Phase 0").

## 2. JSON Payload Structure & Scrubbing / JSON Yapısı ve Temizleme

The AI manages the file with **STRICT SCRUBBING RULES** to ensure zero leak of research content.

*Format (Updated in real-time):*
```json
{
  "tezatlas_version": "1.0",
  "project_start_date": "2026-02-26",
  "document_type": "thesis",
  "discipline": "social-sciences",
  "phases_completed": ["phase-0", "phase-1"],
  "telemetry_log": [
    {
      "timestamp": "...",
      "phase": "phase-0",
      "event_type": "friction",
      "description": "User asked for 3 different clarifications on contribution claim logic."
    },
    {
      "timestamp": "...",
      "phase": "phase-1",
      "event_type": "feature_request",
      "description": "User requested support for a specific archival database in Turkey."
    }
  ]
}
```

## 3. The Post-Mortem Consent (End of Project) / Gönderim Onayı

**Trigger:** Finalization Phase.
**AI Action:** Since the file already exists and the user has likely seen it, the AI simply asks for permission to transmit.

**AI Prompting Script:**
*"Tebrikler! Belgenizi tamamladık. Proje başlangıcından beri arka planda tuttuğum anonim deneyim raporu `tezatlas_feedback.json` olarak hazır.*
*Ekibimize (Tarık İsmet ALKAN ve geliştirici ekibine) bu raporu e-posta ile iletmem için izin verir misiniz? İçeriği istediğiniz zaman kontrol edebilirsiniz."*

## 4. Transmission / İletim (Email Method)

**EN:** Since TezAtlas is a local CLI tool, the AI will assist the user in sending the feedback manually to the development team to ensure maximum transparency.

**TR:** TezAtlas yerel bir CLI aracı olduğu için, yapay zeka şeffaflığı sağlamak adına geri bildirimi geliştirme ekibine manuel olarak göndermeniz için size yardımcı olacaktır.

**AI Action (The Final Prompt):**
*"Harika. Geri bildirim dosyanız `tezatlas_feedback.json` olarak kök dizine kaydedildi. TezAtlas'ın gelişimine katkıda bulunmak için bu dosyayı şu adrese e-posta ile gönderebilirsiniz:*

**To:** `tialkan@tezatlas.com`
**Subject:** `TezAtlas User Feedback - [Document Type]`

*Dilerseniz terminalinizde şu komutu çalıştırarak mail taslağını otomatik olarak açmayı deneyebilirsiniz:*
`open "mailto:tialkan@tezatlas.com?subject=TezAtlas%20Feedback&body=Please%20find%20the%20attached%20tezatlas_feedback.json%20file."`"

## 5. Transparency Guarantee / Şeffaflık Garantisi

**EN:** To maintain academic trust, the AI operates under a "Zero-Knowledge" principle regarding the feedback payload. It exists only to improve the workflow engine, not to collect research data.
**TR:** Akademik güveni korumak için yapay zeka, geri bildirim paketi konusunda "Sıfır Bilgi" prensibiyle çalışır. Bu sistem sadece iş akış motorunu geliştirmek için vardır, araştırma verilerini toplamak için değil.

---

## AI Implementation Directive

1.  **Always Preview:** You MUST print the full content of the `tezatlas_feedback.json` to the screen before asking for permission to save or send it.
2.  **No Exceptions:** If you detect any research title or specific finding in the JSON, you must redact it immediately before the preview.
3.  **Encouraging Tone:** Frame the feedback as a contribution to the global academic community. "Help us help future researchers."
