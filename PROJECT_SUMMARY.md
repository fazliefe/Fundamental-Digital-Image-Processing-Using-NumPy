# 📦 Proje Dosyaları Özeti

Bu belge, projedeki tüm dosyaların ve klasörlerin açıklamalarını içerir.

## 📂 Proje Yapısı

```
bigisayar_görü_ödev3/
│
├── 📄 README.md                      # Ana dokümantasyon (22.5 KB)
├── 📄 QUICKSTART.md                  # Hızlı başlangıç rehberi (2.3 KB)
├── 📄 TECHNICAL_DOCS.md              # Teknik dokümantasyon (14.8 KB)
├── 📄 GITHUB_UPLOAD_GUIDE.md         # GitHub yükleme rehberi (5.7 KB)
├── 📄 CONTRIBUTING.md                # Katkıda bulunma rehberi (12.6 KB)
├── 📄 CHANGELOG.md                   # Versiyon geçmişi (3.9 KB)
├── 📄 LICENSE                        # MIT Lisansı (1.1 KB)
├── 📄 .gitignore                     # Git ignore dosyası (633 B)
│
├── 📄 main.py                        # Ana çalıştırma scripti (2.9 KB)
├── 📄 requirements.txt               # Python bağımlılıkları (42 B)
├── 📄 a.py                           # Yardımcı temizleme scripti (877 B)
│
├── 📁 code/                          # Kaynak kod modülleri
│   ├── __init__.py                   # Paket başlatıcı
│   ├── brightness_adjustment.py      # Parlaklık ayarlama
│   ├── contrast_adjustment.py        # Kontrast ayarlama
│   ├── negative_image.py             # Görüntü negatifi
│   ├── thresholding.py               # Eşikleme
│   ├── histogram_analysis.py         # Histogram analizi
│   ├── image_statistics.py           # İstatistiksel analiz
│   ├── contrast_stretching.py        # Kontrast germe
│   ├── histogram_equalization.py     # Histogram eşitleme
│   ├── gamma_correction.py           # Gamma düzeltmesi
│   └── helpers.py                    # Yardımcı fonksiyonlar
│
├── 📁 images/                        # Giriş görüntüleri
│   └── lenna.png                     # Test görüntüsü
│
├── 📁 results/                       # İşlenmiş görüntüler
│   ├── brightness_adjusted.png       # Parlaklık ayarlı
│   ├── contrast_adjusted.png         # Kontrast ayarlı
│   ├── negative_image.png            # Negatif görüntü
│   ├── thresholded_image.png         # Eşiklenmiş görüntü
│   ├── contrast_stretched.png        # Kontrast gerilmiş
│   ├── equalized_image.png           # Histogram eşitlenmiş
│   └── gamma_corrected.png           # Gamma düzeltmeli
│
└── 📁 .venv/                         # Python sanal ortamı (opsiyonel)
```

## 📄 Dosya Açıklamaları

### Dokümantasyon Dosyaları

#### README.md (Ana Dokümantasyon)
**Boyut:** 22.5 KB  
**Amaç:** Projenin ana dokümantasyonu

**İçerik:**
- Proje hakkında genel bilgi
- Kurulum talimatları
- Kullanım örnekleri
- Tüm modüllerin detaylı açıklaması
- Matematiksel formüller
- API referansı
- Örnek çıktılar
- Lisans ve iletişim bilgileri

**Hedef Kitle:** Tüm kullanıcılar

---

#### QUICKSTART.md (Hızlı Başlangıç)
**Boyut:** 2.3 KB  
**Amaç:** Projeyi hızlıca başlatmak isteyenler için

**İçerik:**
- Hızlı kurulum adımları
- Temel kullanım örnekleri
- Sorun giderme ipuçları
- Modül listesi

**Hedef Kitle:** Acele eden kullanıcılar

---

#### TECHNICAL_DOCS.md (Teknik Dokümantasyon)
**Boyut:** 14.8 KB  
**Amaç:** Derinlemesine teknik bilgi

**İçerik:**
- Mimari genel bakış
- Algoritma detayları ve karmaşıklık analizi
- Performans benchmark'ları
- Detaylı API referansı
- Genişletme rehberi
- Kod örnekleri

**Hedef Kitle:** Geliştiriciler ve araştırmacılar

---

#### GITHUB_UPLOAD_GUIDE.md (GitHub Yükleme Rehberi)
**Boyut:** 5.7 KB  
**Amaç:** Projeyi GitHub'a yükleme rehberi

**İçerik:**
- Git kurulumu ve yapılandırması
- GitHub repository oluşturma
- Komut satırı talimatları
- GitHub Desktop kullanımı
- Sonraki adımlar
- Sorun giderme

**Hedef Kitle:** GitHub'a ilk kez yükleyenler

---

#### CONTRIBUTING.md (Katkıda Bulunma Rehberi)
**Boyut:** 12.6 KB  
**Amaç:** Katkıda bulunmak isteyenler için rehber

**İçerik:**
- Davranış kuralları
- Geliştirme ortamı kurulumu
- Kod standartları (PEP 8)
- Commit mesaj formatı
- Pull request süreci
- Issue raporlama
- İyi pratikler

**Hedef Kitle:** Katkıda bulunanlar

---

#### CHANGELOG.md (Versiyon Geçmişi)
**Boyut:** 3.9 KB  
**Amaç:** Proje değişikliklerini takip etme

**İçerik:**
- Versiyon geçmişi
- Eklenen özellikler
- Düzeltilen hatalar
- Gelecek planları
- Semantic versioning açıklaması

**Hedef Kitle:** Tüm kullanıcılar

---

#### LICENSE (Lisans)
**Boyut:** 1.1 KB  
**Amaç:** Yasal kullanım koşulları

**İçerik:**
- MIT Lisansı metni
- Telif hakkı bilgisi
- Kullanım izinleri

**Hedef Kitle:** Tüm kullanıcılar

---

### Yapılandırma Dosyaları

#### .gitignore
**Boyut:** 633 B  
**Amaç:** Git'in görmezden geleceği dosyalar

**İçerik:**
- Python cache dosyaları
- Sanal ortam klasörleri
- IDE ayar dosyaları
- Geçici dosyalar
- Büyük veri dosyaları

---

#### requirements.txt
**Boyut:** 42 B  
**Amaç:** Python bağımlılıkları

**İçerik:**
```
numpy
matplotlib
pillow
opencv-python
```

---

### Kod Dosyaları

#### main.py
**Boyut:** 2.9 KB  
**Amaç:** Ana çalıştırma scripti

**İşlevler:**
- Görüntü yükleme
- Tüm algoritmaları uygulama
- Sonuçları kaydetme
- Görselleştirme

**Kullanım:**
```bash
python main.py
```

---

#### a.py
**Boyut:** 877 B  
**Amaç:** Null byte temizleme yardımcı scripti

**İşlev:**
- Dosyalardaki null byte'ları temizler

---

### Code Modülleri

#### brightness_adjustment.py
**İşlev:** Parlaklık ayarlama  
**Fonksiyon:** `brightness_adjustment(image, brightness_value)`  
**Karmaşıklık:** O(n×m)

---

#### contrast_adjustment.py
**İşlev:** Kontrast ayarlama  
**Fonksiyon:** `contrast_adjustment(image, factor)`  
**Karmaşıklık:** O(n×m)

---

#### negative_image.py
**İşlev:** Görüntü negatifi  
**Fonksiyon:** `negative_image(image)`  
**Karmaşıklık:** O(n×m)

---

#### thresholding.py
**İşlev:** Eşikleme  
**Fonksiyon:** `thresholding(image, threshold_value)`  
**Karmaşıklık:** O(n×m)

---

#### histogram_analysis.py
**İşlev:** Histogram analizi  
**Fonksiyonlar:**
- `compute_histogram(image)` - O(n×m)
- `plot_histogram(histogram)` - O(256)

---

#### image_statistics.py
**İşlev:** İstatistiksel analiz  
**Fonksiyon:** `image_statistics(image)`  
**Hesaplamalar:** Ortalama, std, entropi, min, max

---

#### contrast_stretching.py
**İşlev:** Kontrast germe  
**Fonksiyon:** `contrast_stretching(image)`  
**Karmaşıklık:** O(n×m)

---

#### histogram_equalization.py
**İşlev:** Histogram eşitleme  
**Fonksiyon:** `histogram_equalization(image)`  
**Karmaşıklık:** O(n×m + 256)

---

#### gamma_correction.py
**İşlev:** Gamma düzeltmesi  
**Fonksiyon:** `gamma_correction(image, gamma)`  
**Karmaşıklık:** O(n×m)

---

#### helpers.py
**İşlev:** Yardımcı fonksiyonlar  
**Fonksiyon:** `plot_images_and_histograms(original, processed)`

---

## 📊 Dosya İstatistikleri

### Toplam Boyutlar

| Kategori | Dosya Sayısı | Toplam Boyut |
|----------|--------------|--------------|
| Dokümantasyon | 6 | ~63 KB |
| Kod Dosyaları | 11 | ~5.5 KB |
| Yapılandırma | 3 | ~2.6 KB |
| **TOPLAM** | **20** | **~71 KB** |

### Satır Sayıları (Tahmini)

| Dosya Tipi | Satır Sayısı |
|------------|--------------|
| Python Kodu | ~300 satır |
| Dokümantasyon | ~1500 satır |
| **TOPLAM** | **~1800 satır** |

---

## 🎯 Hangi Dosyayı Okumalıyım?

### Yeni Kullanıcıysanız:
1. **README.md** - Projeyi anlamak için
2. **QUICKSTART.md** - Hızlıca başlamak için
3. **main.py** - Nasıl kullanıldığını görmek için

### Geliştirici İseniz:
1. **TECHNICAL_DOCS.md** - Algoritmaları anlamak için
2. **CONTRIBUTING.md** - Katkıda bulunmak için
3. **code/** klasörü - Kaynak kodu incelemek için

### GitHub'a Yükleyecekseniz:
1. **GITHUB_UPLOAD_GUIDE.md** - Adım adım talimatlar
2. **.gitignore** - Hangi dosyaların yüklenmeyeceğini görmek için

### Katkıda Bulunacaksanız:
1. **CONTRIBUTING.md** - Katkı kuralları
2. **CHANGELOG.md** - Değişiklik geçmişi
3. **LICENSE** - Lisans koşulları

---

## 🚀 Hızlı Başlangıç

```bash
# 1. Projeyi klonlayın
git clone https://github.com/kullaniciadi/bigisayar_goru_odev3.git
cd bigisayar_goru_odev3

# 2. Bağımlılıkları yükleyin
pip install -r requirements.txt

# 3. Çalıştırın
python main.py

# 4. Sonuçları kontrol edin
# results/ klasöründe işlenmiş görüntüler
```

---

## 📝 Notlar

- Tüm dokümantasyon Türkçe dilinde yazılmıştır
- Kod içi yorumlar ve docstring'ler Türkçe'dir
- Matematiksel formüller uluslararası standartlardadır
- Kod PEP 8 standartlarına uygundur

---

**Son Güncelleme:** 2026-01-02  
**Versiyon:** 1.0.0  
**Toplam Dosya Boyutu:** ~71 KB (kod ve dokümantasyon)
