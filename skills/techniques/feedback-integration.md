---
title: "Feedback Integration — Managing Revisions and Reviewer Responses"
title_tr: "Geri Bildirim Entegrasyonu — Revizyon ve Hakem Yanıtı Yönetimi"
node_type: technique
description: "Systematic protocol for receiving, categorizing, and integrating feedback from advisors, peer reviewers, editors, and co-authors. Includes revision matrix, response letter structure, and git-based change tracking."
description_tr: "Danışman, hakem, editör ve ortak yazarlardan gelen geri bildirimleri alma, sınıflandırma ve entegre etme protokolü. Revizyon matrisi, yanıt mektubu yapısı ve git tabanlı değişiklik takibi içerir."
tags: [feedback, revision, peer-review, advisor, response-letter, git, phase-5, phase-6]
links_to:
  - skills/core/iron-rules.md
  - skills/core/academic-integrity.md
  - skills/templates/tpl-advisor-checkpoint.md
  - skills/tooling/git-workflow.md
used_by:
  - skills/phases/thesis/phase-6-writing.md
  - skills/phases/article/phase-5-revision.md
  - skills/phases/article/phase-6-revision-cycle.md
language: bilingual
version: "1.0"
---

# Geri Bildirim Entegrasyonu / Feedback Integration

Akademik çalışmalarda geri bildirim, metnin kalitesini artırmak ve argümanları güçlendirmek için hayati öneme sahiptir. Bu teknik, geri bildirimleri etkili bir şekilde yönetmek, revizyonları sistematik olarak uygulamak ve hakemlere veya danışmanlara profesyonel yanıtlar hazırlamak için bir çerçeve sunar.

## Geri Bildirim Türleri (Feedback Types)

Farklı kaynaklardan gelen geri bildirimlerin kendine özgü beklentileri ve zamanlamaları vardır.

| Kaynak (Source) | Tür (Type) | Tipik Zamanlama (Typical Timing) | Beklentileri (Expectations) |
| :-------------- | :--------- | :------------------------------- | :-------------------------- |
| **Danışman (Advisor)** | Kapsamlı, yapısal, metodolojik, içeriksel, dilbilgisel | Sürekli, taslak teslimlerinde | Çalışmanın genel yönü, argüman tutarlılığı, metodolojik sağlamlık, yayın stratejisi |
| **Hakem (Peer Reviewer)** | Metodolojik, teorik, deneysel, literatür, dilbilgisel | Dergi/konferans gönderimi sonrası | Bilimsel katkı, metodolojik geçerlilik, literatürle ilişki, açıklık |
| **Editör (Editor)** | Kapsam, format, etik, yayın politikası, genel okunabilirlik | İlk inceleme, hakem sonrası | Derginin kapsamına uygunluk, etik standartlar, dil ve format kalitesi, hakem yanıtı |
| **Ortak Yazar (Co-author)** | İçeriksel, veri analizi, argüman geliştirme, dilbilgisel | Ortak yazım süreci boyunca | Kendi uzmanlık alanlarına ilişkin katkılar, veri yorumlama, argüman uyumu |

## İlk Okuma Protokolü (First Read Protocol)

Geri bildirimleri savunmacı bir tepki vermeden, objektif bir şekilde değerlendirmek için aşağıdaki protokolü uygulayın:

1.  **Adım 1: İlk okumada not alma, sadece anlama (First read, note-taking, focus on understanding)**
    Tüm yorumları baştan sona okuyun. Bu aşamada eleştiriye odaklanmayın, sadece ne denmek istendiğini anlamaya çalışın. Notlar alırken, yorumun ana fikrini ve hangi bölüme ait olduğunu işaretleyin. Henüz yanıt veya çözüm düşünmeyin.
2.  **Adım 2: 24 saat bekle (Wait 24 hours for emotional distance)**
    Geri bildirimi okuduktan sonra en az 24 saat bekleyin. Bu, ilk duygusal tepkilerinizi yatıştırmanıza ve yorumlara daha rasyonel bir bakış açısıyla yaklaşmanıza olanak tanır.
3.  **Adım 3: Her yorum için kategori ata (Categorize each comment)**
    Her bir geri bildirim yorumunu aşağıdaki gibi kategorilere ayırın:
    *   **Kritik (Critical):** Çalışmanın temelini veya geçerliliğini etkileyen, mutlaka ele alınması gereken konular.
    *   **Önemli (Important):** Çalışmanın kalitesini önemli ölçüde artıracak, güçlü argümanlar gerektiren konular.
    *   **İsteğe Bağlı (Optional):** Küçük düzeltmeler, stil önerileri veya yazarın takdirine bırakılan konular.
4.  **Adım 4: Revizyon matrisi oluştur (Create a revision matrix)**
    Tüm geri bildirimleri bir revizyon matrisine aktarın. Bu, her yorumu takip etmenizi ve yanıtlarınızı organize etmenizi sağlar. (Aşağıdaki bölüme bakın.)
5.  **Adım 5: Önceliklendirme (Prioritize: critical / important / optional)**
    Matristeki yorumları kategorilerine göre önceliklendirin. Önce kritik ve önemli yorumlara odaklanın. İsteğe bağlı yorumları zamanınız ve kaynaklarınız elverdiğince ele alın.

## Revizyon Matrisi (Revision Matrix)

Revizyon matrisi, geri bildirimleri yönetmek ve revizyon sürecini şeffaf hale getirmek için vazgeçilmez bir araçtır.

| # | Geri Bildirim (Feedback) | Kaynak (Source) | Öncelik (Priority) | Eylem (Action) | Durum (Status) |
| :- | :----------------------- | :-------------- | :----------------- | :------------- | :------------- |
| 1 | Metodoloji bölümünde örneklem büyüklüğü gerekçesi yetersiz. | Hakem 2 | Kritik | Örneklem gücü analizi ekle, literatürle destekle. | Tamamlandı |
| 2 | Giriş bölümü, çalışmanın yeniliğini yeterince vurgulamıyor. | Editör | Önemli | Girişin son paragrafını yeniden yaz, katkıyı netleştir. | Devam Ediyor |
| 3 | Şekil 3'teki eksen etiketleri daha açıklayıcı olmalı. | Danışman | İsteğe Bağlı | Şekil 3'ün eksen etiketlerini güncelle. | Tamamlandı |
| 4 | Tartışma bölümünde bulguların teorik çıkarımları genişletilmeli. | Hakem 1 | Kritik | İlgili teorik çerçevelerle bağlantıları güçlendir. | Planlandı |

## Yanıt Mektubu Yapısı (Response Letter — for journal submissions)

Hakemlere ve editöre yazılan yanıt mektubu, profesyonelliğinizi ve geri bildirimleri ciddiye aldığınızı gösterir. Her yorumu tek tek ele alın.

**Genel Yapı:**

1.  **Giriş:** Editöre ve hakemlere teşekkür edin. Revizyonların çalışmayı nasıl geliştirdiğini belirtin.
    *   *TR:* "Değerli Editör ve Hakemler, çalışmamıza gösterdiğiniz ilgi ve değerli geri bildirimleriniz için içtenlikle teşekkür ederiz. Yorumlarınız, makalemizin kalitesini önemli ölçüde artırmamıza yardımcı olmuştur."
    *   *EN:* "Dear Editor and Reviewers, we sincerely thank you for your time and valuable feedback on our manuscript. Your comments have significantly helped us improve the quality of our paper."
2.  **Hakemlere Yanıtlar:** Her hakemin yorumlarını ayrı ayrı ele alın. Her yorumu kopyalayıp altına yanıtınızı yazın.
    *   **"We thank the reviewer for..." (Teşekkür ve Kabul)**
        *   *TR:* "Hakem [X]'in [Y] konusundaki yorumu için teşekkür ederiz. Bu öneriyi tamamen kabul ediyor ve makalenin [sayfa numarası] bölümünü [yapılan değişiklik] şeklinde revize ettik."
        *   *EN:* "We thank Reviewer [X] for their comment regarding [Y]. We fully agree with this suggestion and have revised section [page number] of the manuscript by [description of change]."
    *   **"We have revised..." (Revizyonun Açıklaması)**
        *   *TR:* "Hakemin [Z] konusundaki endişesini gidermek için, metodoloji bölümüne [yapılan ekleme/değişiklik] detaylarını ekledik (bkz. sayfa [X], paragraf [Y])."
        *   *EN:* "To address the reviewer's concern about [Z], we have added details about [addition/change made] to the methodology section (see page [X], paragraph [Y])."
    *   **"We respectfully disagree because..." (Saygılı İtiraz)**
        *   *TR:* "Hakemin [W] konusundaki yorumunu dikkatle değerlendirdik. Ancak, [neden] nedeniyle bu değişikliğin çalışmamızın ana odağını değiştireceğini düşünüyoruz. Bu nedenle, orijinal metni korumayı tercih ettik."
        *   *EN:* "We carefully considered the reviewer's comment regarding [W]. However, we respectfully believe that implementing this change would alter the main focus of our study due to [reason]. Therefore, we have chosen to retain the original text."
3.  **Sonuç:** Editöre ve hakemlere tekrar teşekkür edin ve ek soruları yanıtlamaya hazır olduğunuzu belirtin.

## Git ile Revizyon Takibi

Revizyon süreçlerini yönetmek için Git gibi versiyon kontrol sistemlerini kullanmak, değişiklikleri izlenebilir ve geri alınabilir hale getirir. Her revizyon turunu ayrı bir Git commit'i olarak kaydedin.

*   **Her revizyon turu = bir Git commit'i:** Örneğin, hakemlerden gelen ilk geri bildirimleri uyguladıktan sonra tüm değişiklikleri tek bir commit'te toplayın.
*   **Commit mesajı kuralı:** Anlaşılır ve bilgilendirici commit mesajları kullanın.
    *   Örnek: `revision(R1): address reviewer comments on methodology and introduction`
    *   Örnek: `revision(R2): incorporate editor's suggestions on formatting and clarity`
*   Bu yaklaşım, çalışmanızın farklı versiyonları arasında kolayca geçiş yapmanızı ve hangi değişikliklerin ne zaman yapıldığını görmenizi sağlar. Daha fazla bilgi için [[git-workflow]] düğümüne bakın.

Bu geri bildirim entegrasyonu teknikleri, [[iron-rules]] düğümündeki Demir Kural 5 (Danışman Kontrol Noktaları) ile doğrudan bağlantılıdır. Danışmanınızla düzenli olarak geri bildirimleri ve revizyon planınızı paylaşmak, sürecin şeffaf ve verimli ilerlemesini sağlar. Bu, hem sizin hem de danışmanınızın beklentilerini yönetmenize yardımcı olur.