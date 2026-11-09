# Prof. Dr. Ekrem Demirli ile Düşünce ve Hayat Külliyatı

Vav Radyo'da yayımlanan Prof. Dr. Ekrem Demirli'nin **"Düşünce ve Hayat"** radyo dersleri serisinin 1'den 31'e kadar tüm bölümlerinin kapsamlı, interaktif ve açık tema çalışma fasikülleri.

> 📺 **Resmi YouTube Oynatma Listesi:** [Prof. Dr. Ekrem Demirli ile Düşünce ve Hayat - Vav Radyo](https://www.youtube.com/playlist?list=PLaK3SezGSNwkveYROjTnIAqzb3bshquQ-)  
> 🎙️ **31. Bölüm YouTube Kaydı:** [Prof. Dr. Ekrem Demirli ile Düşünce ve Hayat 31. Bölüm](https://www.youtube.com/watch?v=MUrJwEc_YsI) | Detaylı Döküm: [`episodes/bolum31_ozet.md`](episodes/bolum31_ozet.md)

## 📁 Proje Dizin Yapısı

```
dusunce-ve-hayat-rehberi/
├── index.html                   # Ana Kütüphane Portalı, Arama & Okuyucu Dashboard
├── assets/
│   ├── css/
│   │   └── worksheet.css        # Ortak el çizimi doodle, pastel ve kağıt dokusu stilleri
│   └── js/
│       └── app.js               # İlerleme, filtreleme ve modal yöneticisi
├── data/
│   └── episodes.json            # 31 bölümün tam başlık, konu, şahsiyet ve hikmet veritabanı
└── episodes/                    # 31 adet 5 sayfalık interaktif çalışma fasikülü
    ├── bolum01.html             # 1. Bölüm (Hasan-ı Basrî & Zühd)
    ├── bolum02.html             # 2. Bölüm (Fudayl b. İyâz & Sıdk)
    ├── ...
    ├── bolum30.html             # 30. Bölüm (Ebû Türâb en-Nahşebî & Fil Suresi)
    └── bolum31.html             # 31. Bölüm (Âcil & Âcil, İmam Mâtürîdî & Tamah)
```

## ✨ Tasarım ve Pedagojik Özellikler

- **Açık Tema & Sıcak Pastel Atmosfer:** Krem fon (`#f5f3ec`), 1.2px noktalı çalışma kağıdı dokusu (`radial-gradient`), 3.5px altın sarısı el çizimi sınır çizgileri (`#eab308`).
- **Doğal El Yazısı Tipografisi:** `Patrick Hand`, `Caveat`, `Plus Jakarta Sans` ve `Amiri` Arapça nass fontları ile büyük, ferah punto ölçeği.
- **5 Sayfalık Fasikül Mimarisi:**
  1. *Sayfa 1:* Kapak & Genel Bakış (Dersin Temel Düşüncesi, 4'lü Yol Haritası, Zihin Haritası Rozetleri)
  2. *Sayfa 2:* Tezkiretü'l-Evliyâ Okumaları & Öncü Âriflerin Amel Ahlakı
  3. *Sayfa 3:* Kur'an-ı Kerim Tahlilleri, Kıssalar & Tevhid Delilleri
  4. *Sayfa 4:* Tasavvufi Ahlak & Nefis Muhasebesi (Karz-ı Hasen, Tövbe, Terk)
  5. *Sayfa 5:* İbn Atâullah el-İskenderî'nin Hikem-i Atâiyye Şerhi & Kazanım Kontrol Listesi
- **İnteraktif Not Alanları:** `contenteditable="true"` çizgili defter alanları sayesinde talebeler kendi tefekkür notlarını tarayıcı üzerinde doğrudan yazabilir.
- **Yazdırma / PDF Desteği:** Sayfa kesme kuralları (`page-break-after: always`) ile tek tıkla A4 fasikül çıktısı veya PDF kaydı imkânı.
