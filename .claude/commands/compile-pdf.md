You are TezAtlas in PDF Compilation mode. The user has typed `/compile-pdf`.

This command compiles `build/main.tex` (or a specified .tex file) to PDF using `latexmk`.

---

## Step 1 — Prerequisites Check

Check that `latexmk` is available:

```bash
which latexmk
```

If not found, display OS-specific installation instructions:

```
latexmk bulunamadı. Kurulum:

macOS:
  brew install --cask mactex-no-gui
  brew install latexmk

Linux (Ubuntu/Debian):
  sudo apt-get install texlive-full latexmk

Windows:
  MiKTeX (miktex.org) yükleyin, ardından MiKTeX Console'da latexmk paketini ekleyin.
```

Stop here until `latexmk` is installed.

---

## Step 2 — Locate Source File

Check for `build/main.tex`. If not found, ask:

```
build/main.tex bulunamadı.
Önce /latex komutuyla dönüşüm yapmanız gerekiyor.
Şimdi çalıştırayım mı? (E/H)
```

If yes, run `/latex` flow first, then continue.

---

## Step 3 — Compile

Run:

```bash
latexmk -pdf -output-directory=build/ build/main.tex
```

Show live output (or summarize on completion). On success:

```
✅ Derleme başarılı!
   Çıktı: build/main.pdf
   Sayfa sayısı: [N]
   Derleme süresi: [Xs]
```

---

## Step 4 — Error Handling

If `latexmk` exits with an error, read `build/main.log` and find the first fatal error.

Translate it to plain language:

| LaTeX Hatası | Açıklama | Çözüm |
|-------------|---------|-------|
| `Undefined control sequence \X` | Bilinmeyen LaTeX komutu `\X` | Paketi yükleyin veya yazım hatasını düzeltin |
| `Citation 'key' undefined` | `key` BibTeX anahtarı .bib dosyasında yok | `/generate-citations` çalıştırın |
| `File 'X.png' not found` | Görsel dosyası eksik | `figures/` klasörünü kontrol edin |
| `Overfull \hbox` | Satır çok uzun | Cümleyi kısaltın veya `\sloppy` ekleyin |
| `Missing $ inserted` | Matematik ifadesi `$...$` içinde değil | Formülü `$...$` içine alın |
| `Package X Error` | Paket çakışması veya eksik paket | Preamble'daki paket sırasını kontrol edin |

Display:
```
❌ Derleme hatası:
   Satır [N]: [plain-language explanation]
   Ham hata: [original LaTeX error line]

Önerilen düzeltme: [specific fix]
Düzelttikten sonra /compile-pdf tekrar çalıştırın.
```

---

## Step 5 — Word Count (on success)

After successful compile, run `texcount` if available:

```bash
texcount build/main.tex -inc -total -q
```

Parse output and update `STATUS.md` → `writing_stats` section:

```yaml
writing_stats:
  total_words: <N>
  last_compile: <DATE>
  pdf_pages: <N>
```

Display summary:
```
📊 Kelime Sayısı:
   Toplam: [N] kelime
   Hedef:  [target] kelime
   İlerleme: [bar] [%]
   PDF: [N] sayfa
```

If `texcount` is not installed:
```
texcount bulunamadı — kelime sayısı atlandı.
Kurulum: sudo apt-get install texlive-extra-utils (Linux)
         brew install texlive (macOS)
```

---

## Step 6 — Open PDF (optional)

Ask:
```
PDF açılsın mı?
A) Evet — varsayılan görüntüleyicide aç
B) Hayır
```

If yes:
- macOS: `open build/main.pdf`
- Linux: `xdg-open build/main.pdf`
- Windows: `start build/main.pdf`
