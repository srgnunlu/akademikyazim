# TezAtlas Fork Roadmap

Bu dosya, TezAtlas'ı bizim kullanımımıza göre sadeleştirmek ve ürünleştirmek için pratik yol haritasıdır.

## Hedef

TezAtlas'ı:
- kurulumu kolay,
- Türkçe odaklı,
- tıp/tez iş akışına uygun,
- gerçekten kullanılan komutları öne çıkaran,
- gereksiz iddiaları azaltılmış
bir research workflow aracı haline getirmek.

## Aşama 1 — Stabilizasyon

Amaç: repo ilk kurulumda sorunsuz ayağa kalksın.

- [x] `pyproject.toml` build backend düzeltmesi
- [x] CLI entrypoint olarak `tezatlas` eklenmesi
- [x] packaging kapsamına `core` modüllerinin dahil edilmesi
- [x] yerel geliştirme artıkları için `.gitignore` temizliği (`.venv`, `_demo_project`, `.pytest_cache`)
- [ ] temiz bir sanal ortamda `pip install -e .` yeniden doğrulama
- [ ] README quick start bölümünü gerçek kurulum akışına göre sadeleştirme
- [ ] varsa kırık script/import zincirlerini tarama

## Aşama 2 — Bizim Kullanımına Uygunlaştırma

Amaç: gerçekten kullanacağımız akışları öne çıkarmak.

Öncelikli kullanım alanları:
- tez/proposal hazırlığı
- literatür tarama ve kaynak havuzu yönetimi
- gap / contradiction / synthesis çıktıları
- proje durum takibi
- metodoloji taslağı oluşturma

Plan:
- [ ] tıp alanı için örnek proje şablonlarını güçlendirme
- [ ] Türkçe dosya/adlandırma standardını netleştirme
- [ ] minimum gerekli komut setini belirleme
- [ ] gereksiz veya henüz olgunlaşmamış modülleri ikinci plana atma
- [ ] örnek bir gerçek kullanım akışı dokümante etme

## Aşama 3 — Sadeleştirme

Amaç: repo'yu daha az "manifesto", daha çok "araç" haline getirmek.

- [ ] README'yi iki katmana ayırma:
  - kısa kullanıcı başlangıcı
  - detaylı felsefe / manifesto / araştırma arka planı
- [ ] web, CLI, agents ve docs sınırlarını netleştirme
- [ ] isimlendirme ve klasör yapısında tutarlılık taraması
- [ ] demo/prototype unsurlarını ayıklama

## Aşama 4 — Ürünleşme

Amaç: ileride bağımsız ürün/fork olarak büyütebilmek.

- [ ] özel branding
- [ ] default provider/agent seçimleri
- [ ] web arayüzünden proje oluşturma ve status görüntüleme
- [ ] kaynak yükleme + analiz akışı
- [ ] çıktıları tek panelden yönetme

## Bizim İçin Önerilen İlk Çekirdek Özellik Seti

İlk sürümde tutulması en mantıklı parçalar:
- proje iskeleti oluşturma
- session status
- reading tracker
- gap / contradiction / synthesis komutları
- methodology template
- sources klasör mantığı

İlk sürümde ertelenebilecek parçalar:
- aşırı geniş manifesto dili
- tam agent orkestrasyonu bağımlılığı
- çok sayıda disiplin için eşit derinlik iddiası
- tam web ürün beklentisi

## Notlar

- Mevcut repo teknik olarak kullanılabilir durumda.
- Web build başarılı.
- CLI/test temel akışı başarılı.
- En kritik kısa vadeli teknik risk packaging/kurulum akışının tutarlılığı.
