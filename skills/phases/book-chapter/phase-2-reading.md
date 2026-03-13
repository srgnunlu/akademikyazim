---
title: "Phase 2 — Reading"
title_tr: "Aşama 2 — Okuma"
node_type: phase
phase_number: 2
document_type: book-chapter
phase_gate_in: "phase-1-literature.md"
phase_gate_out: "phase-3-argument.md"
description: "Process the chapter's literature using the standard 3-level reading system. Special consideration for sources that contradict other chapters' claims — handle with scholarly care rather than avoidance. Iron Rules apply throughout."
description_tr: "Standart 3 düzeyli okuma sistemini kullanarak bölümün literatürünü işleyin. Diğer bölümlerin iddialarıyla çelişen sources için özel dikkat — kaçınmak yerine akademik özenle ele alın. Demir Kurallar boyunca geçerlidir."
tags: [phase, book-chapter, reading, 3-level, contradiction, iron-rules]
outputs:
  - "reading_notes.md"
links_to:
  - skills/core/iron-rules.md
  - skills/phases/book-chapter/phase-1-literature.md
language: bilingual
version: "1.0"
---

# Phase 2 — Reading
# Aşama 2 — Okuma

## Gate Rule / Geçiş Kuralı

**EN:** Iron Rules apply. This is especially important in an edited volume where your chapter is read alongside others — a factual error or misattribution reflects on the entire volume, not just your chapter.

**TR:** Demir Kurallar geçerlidir. Bu, bölümünüzün diğerleriyle birlikte okunduğu editörlü bir ciltte özellikle önemlidir — olgusal bir hata veya yanlış atıf yalnızca bölümünüzü değil, tüm cildi etkiler.

---

## 1. The 3-Level System / 3 Düzeyli Sistem

**EN:** Apply the standard reading system to all sources in the lit_position.md source list.

**TR:** lit_position.md kaynak listesindeki tüm sourcesa standart okuma sistemini uygulayın.

**Level 1 — Scan / Tarama**
- Abstract, introduction, conclusion, headings
- Decision: relevant to chapter's argument? `[READ]` or `[SKIP]`
- Time: 5–10 minutes per source

**Level 2 — Read / Okuma**
- Full read; mark key passages
- Annotate in relation to chapter's specific argument (not the field in general)
- Time: varies by source length

**Level 3 — Extract / Çıkarma**
- Extract specific claims, quotations, data with full citation
- Tag each extract by its role in the chapter's argument

---

## 2. Annotation Tags for Book Chapters / Kitap Bölümleri için Açıklama Etiketleri

**EN:** Standard tags plus two chapter-specific additions.

**TR:** Standart etiketler artı iki bölüme özgü eklenti.

| Tag / Etiket | Use / Kullanım |
|-------------|----------------|
| `[KEY]` | Core claim for the chapter's argument |
| `[FOUND]` | Foundational text — establishes the scholarly conversation |
| `[SUPPORT]` | Supports a specific claim in the chapter |
| `[CONTRA]` | Contradicts the chapter's argument — must be addressed |
| `[CONTRA-VOL]` | Contradicts a claim made in another chapter of this volume |
| `[CROSS-REF]` | Should be cross-referenced to another chapter in the volume |
| `[QUOTE]` | Direct quotation for use in chapter |
| `[SKIP]` | Not relevant |

---

## 3. Handling [CONTRA-VOL] Sources / [KARŞI-CİLT] Kaynaklarını Yönetme

**EN:** When a source contradicts what another chapter in the volume argues, you face a choice that cannot be avoided:

**TR:** Bir kaynak, ciltteki başka bir bölümün savunduğuyla çeliştiğinde, kaçınılamaz bir seçimle karşılaşırsınız:

**Option A — Acknowledge and position / Kabul et ve konumlan:**
"While [Author X] (Chapter N in this volume) argues [claim], recent evidence suggests [your position] because [evidence]. This difference may be explained by [context/scope difference]."

**Option B — Coordinate with the other author / Diğer yazarla koordinasyon:**
Contact the other author through the editor. One chapter may be wrong, or the apparent contradiction may dissolve under closer analysis.

**Option C — Leave to the editor's introduction / Editörün girişine bırak:**
Some volume-level tensions are best flagged to the editor, who can address them in the editorial introduction.

**Do NOT / Yapma:**
- Ignore the contradiction and hope readers don't notice
- Misrepresent the other chapter's position to eliminate the tension

---

## 4. Reading in the Book's Context / Kitabın Bağlamında Okuma

**EN:** As you read, continuously ask: how does this source help advance the book's central argument (not just my chapter's argument)? Sources that only serve your chapter without contributing to the book's argument should be used sparingly — every citation is a claim on the reader's attention.

**TR:** Okurken sürekli sorun: bu kaynak (yalnızca bölümümün argümanını değil) kitabın merkezi argümanını ilerletmeye nasıl yardımcı oluyor? Yalnızca bölümünüze hizmet eden ancak kitabın argümanına katkıda bulunmayan sources tutumlu kullanılmalıdır — her atıf, okuyucunun dikkatine bir taleptir.

---

## 5. Reading Notes Structure / Okuma Notları Yapısı

**EN:** Organize reading notes by role in the chapter argument, not by source.

**TR:** Okuma notlarını kaynağa göre değil, bölüm argümanındaki role göre düzenleyin.

```markdown
## Reading Notes / Okuma Notları

### Establishing the scholarly conversation / Akademik konuşmayı oluşturma
[KEY / FOUND sources]

### Supporting the chapter's main claim / Bölümün ana iddiasını destekleme
[SUPPORT sources with extracted claims]

### Contrary evidence to address / Ele alınacak karşıt kanıt
[CONTRA sources — must appear in chapter]

### Cross-volume tensions / Cilt içi gerilimler
[CONTRA-VOL sources — flag to editor if unresolvable]
```

---

## Completion Checklist / Tamamlama Kontrol Listesi

- [ ] All sources from lit_position.md processed at Level 1 / Tüm sources Düzey 1'de işlendi
- [ ] Key sources read at Level 2 / Temel sources Düzey 2'de okundu
- [ ] All [CONTRA-VOL] sources identified and handling decision made / Tüm [KARŞI-CİLT] sourcesı belirlendi ve yönetim kararı verildi
- [ ] Iron Rules: every extract has full citation / Demir Kurallar: her çıkarmanın tam atıfı var
- [ ] Reading notes organized by role in argument / Okuma notları argümandaki role göre düzenlendi

**Gate in:** phase-1-literature.md
**Gate out:** → phase-3-argument.md
