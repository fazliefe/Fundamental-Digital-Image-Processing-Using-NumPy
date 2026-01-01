# 🖼️ Bilgisayar Görü - Görüntü İşleme Kütüphanesi

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Latest-orange.svg)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Bilgisayar Görü Ödev 3** - Temel görüntü işleme algoritmalarının sıfırdan Python ile implementasyonu. Bu proje, görüntü işleme alanındaki temel kavramları ve teknikleri öğrenmek için geliştirilmiş kapsamlı bir eğitim kütüphanesidir.

---

## 📋 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Özellikler](#-özellikler)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Modüller ve Algoritmalar](#-modüller-ve-algoritmalar)
  - [1. Parlaklık Ayarlama](#1-parlaklık-ayarlama-brightness-adjustment)
  - [2. Kontrast Ayarlama](#2-kontrast-ayarlama-contrast-adjustment)
  - [3. Görüntü Negatifi](#3-görüntü-negatifi-negative-image)
  - [4. Eşikleme](#4-eşikleme-thresholding)
  - [5. Histogram Analizi](#5-histogram-analizi-histogram-analysis)
  - [6. Görüntü İstatistikleri](#6-görüntü-i̇statistikleri-image-statistics)
  - [7. Kontrast Germe](#7-kontrast-germe-contrast-stretching)
  - [8. Histogram Eşitleme](#8-histogram-eşitleme-histogram-equalization)
  - [9. Gamma Düzeltmesi](#9-gamma-düzeltmesi-gamma-correction)
- [Proje Yapısı](#-proje-yapısı)
- [Teknik Detaylar](#-teknik-detaylar)
- [Örnek Çıktılar](#-örnek-çıktılar)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)
- [İletişim](#-i̇letişim)

---

## 🎯 Proje Hakkında

Bu proje, bilgisayar görü ve görüntü işleme alanında temel algoritmaların **sıfırdan** implementasyonunu içermektedir. OpenCV gibi hazır kütüphanelerin sunduğu fonksiyonları kullanmak yerine, algoritmaların matematiksel temellerini anlayarak NumPy ile kendi implementasyonlarımızı geliştirdik.

### 🎓 Eğitim Amaçları

- Görüntü işleme algoritmalarının matematiksel temellerini öğrenmek
- NumPy ile düşük seviyeli görüntü manipülasyonu yapmak
- Histogram analizi ve istatistiksel görüntü işleme tekniklerini uygulamak
- Piksel düzeyinde görüntü dönüşümleri gerçekleştirmek

### 💡 Kullanım Alanları

- **Eğitim**: Bilgisayar görü derslerinde temel kavramların öğretilmesi
- **Araştırma**: Görüntü işleme algoritmalarının davranışlarının incelenmesi
- **Prototipleme**: Hızlı görüntü işleme prototipi geliştirme
- **Referans**: Algoritmaların nasıl çalıştığını anlamak için kaynak kod incelemesi

---

## ✨ Özellikler

### 🔧 Temel İşlemler
- ✅ **Parlaklık Ayarlama**: Görüntüyü aydınlatma veya koyulaştırma
- ✅ **Kontrast Ayarlama**: Görüntünün dinamik aralığını değiştirme
- ✅ **Görüntü Negatifi**: Renk tersine çevirme işlemi
- ✅ **Eşikleme (Thresholding)**: İkili (binary) görüntü oluşturma

### 📊 Gelişmiş İşlemler
- ✅ **Histogram Analizi**: Piksel dağılımını görselleştirme ve analiz etme
- ✅ **Kontrast Germe**: Dinamik aralık genişletme
- ✅ **Histogram Eşitleme**: Kontrast iyileştirme
- ✅ **Gamma Düzeltmesi**: Doğrusal olmayan parlaklık ayarlama

### 📈 Analiz Araçları
- ✅ **İstatistiksel Analiz**: Ortalama, standart sapma, entropi hesaplama
- ✅ **Görselleştirme**: Matplotlib ile sonuçları görüntüleme
- ✅ **Karşılaştırma**: Orijinal ve işlenmiş görüntüleri yan yana inceleme

---

## 🚀 Kurulum

### Gereksinimler

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)

### Adım 1: Projeyi Klonlayın

```bash
git clone https://github.com/kullaniciadi/bigisayar_goru_odev3.git
cd bigisayar_goru_odev3
```

### Adım 2: Sanal Ortam Oluşturun (Önerilen)

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Adım 3: Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### Bağımlılıklar

```
numpy          # Sayısal hesaplamalar ve matris işlemleri
matplotlib     # Görselleştirme ve grafik çizimi
pillow         # Görüntü okuma ve yazma
opencv-python  # (Opsiyonel) Karşılaştırma için
```

---

## 💻 Kullanım

### Temel Kullanım

Projeyi çalıştırmak için ana dizinde:

```bash
python main.py
```

Bu komut:
1. `images/lenna.png` görüntüsünü yükler
2. Tüm görüntü işleme algoritmalarını uygular
3. Sonuçları `results/` klasörüne kaydeder
4. Görselleştirmeleri ekranda gösterir

### Kendi Görüntünüzü İşleme

`main.py` dosyasını düzenleyerek kendi görüntünüzü kullanabilirsiniz:

```python
# main.py içinde
image_path = 'images/sizin_goruntunuz.png'  # Görüntü yolunu değiştirin
```

### Parametreleri Özelleştirme

Algoritma parametrelerini ihtiyacınıza göre ayarlayabilirsiniz:

```python
# Parlaklık değeri (-255 ile 255 arası)
brightness_value = 50

# Kontrast faktörü (0.5 = düşük kontrast, 2.0 = yüksek kontrast)
contrast_factor = 1.5

# Eşik değeri (0-255 arası)
threshold_value = 128

# Gamma değeri (< 1 = aydınlatma, > 1 = koyulaştırma)
gamma = 1.5
```

### Modülleri Ayrı Ayrı Kullanma

Her modül bağımsız olarak kullanılabilir:

```python
import numpy as np
from PIL import Image
from code.brightness_adjustment import brightness_adjustment
from code.histogram_equalization import histogram_equalization

# Görüntüyü yükle
image = np.array(Image.open('images/test.png').convert('L'))

# Parlaklık ayarla
bright_image = brightness_adjustment(image, 50)

# Histogram eşitle
equalized = histogram_equalization(image)

# Kaydet
Image.fromarray(bright_image).save('output_bright.png')
Image.fromarray(equalized).save('output_equalized.png')
```

---

## 📚 Modüller ve Algoritmalar

### 1. Parlaklık Ayarlama (Brightness Adjustment)

**Dosya:** `code/brightness_adjustment.py`

**Açıklama:** Görüntünün genel parlaklığını artırır veya azaltır.

**Matematiksel Formül:**
```
I_out(x, y) = clip(I_in(x, y) + β, 0, 255)
```
- `I_in`: Giriş görüntüsü
- `β`: Parlaklık değeri (brightness_value)
- `clip`: 0-255 aralığında sınırlama

**Kullanım:**
```python
from code.brightness_adjustment import brightness_adjustment

# Parlaklığı artır (+50)
brighter = brightness_adjustment(image, 50)

# Parlaklığı azalt (-50)
darker = brightness_adjustment(image, -50)
```

**Parametreler:**
- `image` (numpy.ndarray): Giriş görüntüsü (gri tonlamalı)
- `brightness_value` (int): Parlaklık değeri (-255 ile 255 arası)

**Dönüş Değeri:**
- `numpy.ndarray`: Parlaklığı ayarlanmış görüntü (uint8)

---

### 2. Kontrast Ayarlama (Contrast Adjustment)

**Dosya:** `code/contrast_adjustment.py`

**Açıklama:** Görüntünün kontrastını (açık ve koyu tonlar arası farkı) ayarlar.

**Matematiksel Formül:**
```
I_out(x, y) = clip(α × (I_in(x, y) - 128) + 128, 0, 255)
```
- `α`: Kontrast faktörü (factor)
- `128`: Orta gri değeri (pivot noktası)

**Kullanım:**
```python
from code.contrast_adjustment import contrast_adjustment

# Kontrastı artır (1.5x)
high_contrast = contrast_adjustment(image, 1.5)

# Kontrastı azalt (0.5x)
low_contrast = contrast_adjustment(image, 0.5)
```

**Parametreler:**
- `image` (numpy.ndarray): Giriş görüntüsü
- `factor` (float): Kontrast faktörü (0.5-3.0 arası önerilir)

**Dönüş Değeri:**
- `numpy.ndarray`: Kontrastı ayarlanmış görüntü (uint8)

---

### 3. Görüntü Negatifi (Negative Image)

**Dosya:** `code/negative_image.py`

**Açıklama:** Görüntünün renklerini tersine çevirir (negatif film etkisi).

**Matematiksel Formül:**
```
I_out(x, y) = 255 - I_in(x, y)
```

**Kullanım:**
```python
from code.negative_image import negative_image

# Negatif görüntü oluştur
negative = negative_image(image)
```

**Parametreler:**
- `image` (numpy.ndarray): Giriş görüntüsü

**Dönüş Değeri:**
- `numpy.ndarray`: Negatif görüntü

**Kullanım Alanları:**
- Film negatifi simülasyonu
- Medikal görüntüleme (X-ray analizi)
- Görüntü analizi için ön işleme

---

### 4. Eşikleme (Thresholding)

**Dosya:** `code/thresholding.py`

**Açıklama:** Görüntüyü belirli bir eşik değerine göre ikili (binary) görüntüye dönüştürür.

**Matematiksel Formül:**
```
I_out(x, y) = { 255, if I_in(x, y) > T
              { 0,   otherwise
```
- `T`: Eşik değeri (threshold_value)

**Kullanım:**
```python
from code.thresholding import thresholding

# Eşik değeri 128 ile ikili görüntü oluştur
binary = thresholding(image, 128)

# Daha yüksek eşik (daha az beyaz piksel)
binary_high = thresholding(image, 180)
```

**Parametreler:**
- `image` (numpy.ndarray): Giriş görüntüsü
- `threshold_value` (int): Eşik değeri (0-255 arası)

**Dönüş Değeri:**
- `numpy.ndarray`: İkili görüntü (sadece 0 ve 255 değerleri)

**Kullanım Alanları:**
- Nesne segmentasyonu
- Ön plan/arka plan ayrımı
- OCR (Optik Karakter Tanıma) ön işleme

---

### 5. Histogram Analizi (Histogram Analysis)

**Dosya:** `code/histogram_analysis.py`

**Açıklama:** Görüntünün piksel değerlerinin dağılımını hesaplar ve görselleştirir.

**Fonksiyonlar:**

#### `compute_histogram(image)`
Görüntünün histogramını hesaplar.

**Matematiksel Tanım:**
```
H(i) = Σ δ(I(x,y) = i)  for i ∈ [0, 255]
```
- `H(i)`: i değerine sahip piksel sayısı
- `δ`: Kronecker delta fonksiyonu

**Kullanım:**
```python
from code.histogram_analysis import compute_histogram, plot_histogram

# Histogram hesapla
hist = compute_histogram(image)

# Histogram görselleştir
plot_histogram(hist)
```

#### `plot_histogram(histogram)`
Histogramı grafik olarak gösterir.

**Parametreler:**
- `histogram` (numpy.ndarray): 256 elemanlı histogram dizisi

**Kullanım Alanları:**
- Görüntü kalitesi değerlendirmesi
- Dinamik aralık analizi
- Eşikleme için optimal değer belirleme

---

### 6. Görüntü İstatistikleri (Image Statistics)

**Dosya:** `code/image_statistics.py`

**Açıklama:** Görüntünün istatistiksel özelliklerini hesaplar.

**Hesaplanan Metrikler:**

1. **Ortalama (Mean):**
   ```
   μ = (1/N) Σ I(x,y)
   ```

2. **Standart Sapma (Standard Deviation):**
   ```
   σ = sqrt((1/N) Σ (I(x,y) - μ)²)
   ```

3. **Entropi (Entropy):**
   ```
   E = -Σ p(i) × log₂(p(i))
   ```
   - `p(i)`: i değerinin olasılığı

4. **Minimum ve Maximum Değerler**

**Kullanım:**
```python
from code.image_statistics import image_statistics

# İstatistikleri hesapla ve yazdır
image_statistics(image)
```

**Çıktı Örneği:**
```
Ortalama: 124.56
Standart Sapma: 45.23
Entropi: 7.42
Min Değer: 0
Max Değer: 255
```

---

### 7. Kontrast Germe (Contrast Stretching)

**Dosya:** `code/contrast_stretching.py`

**Açıklama:** Görüntünün dinamik aralığını 0-255 aralığına genişletir.

**Matematiksel Formül:**
```
I_out(x, y) = ((I_in(x, y) - I_min) / (I_max - I_min)) × 255
```
- `I_min`: Görüntüdeki minimum piksel değeri
- `I_max`: Görüntüdeki maksimum piksel değeri

**Kullanım:**
```python
from code.contrast_stretching import contrast_stretching

# Kontrast germe uygula
stretched = contrast_stretching(image)
```

**Parametreler:**
- `image` (numpy.ndarray): Giriş görüntüsü

**Dönüş Değeri:**
- `numpy.ndarray`: Kontrastı gerilmiş görüntü

**Kullanım Alanları:**
- Düşük kontrastlı görüntüleri iyileştirme
- Medikal görüntüleme
- Uydu görüntülerinin analizi

---

### 8. Histogram Eşitleme (Histogram Equalization)

**Dosya:** `code/histogram_equalization.py`

**Açıklama:** Histogramı düzleştirerek görüntünün kontrastını iyileştirir.

**Algoritma Adımları:**

1. **Histogram Hesaplama:**
   ```
   H(i) = piksel sayısı (değer = i)
   ```

2. **Kümülatif Dağılım Fonksiyonu (CDF):**
   ```
   CDF(i) = Σ(j=0 to i) H(j) / N
   ```

3. **Dönüşüm Fonksiyonu:**
   ```
   T(i) = floor(255 × CDF(i))
   ```

4. **Piksel Dönüşümü:**
   ```
   I_out(x, y) = T(I_in(x, y))
   ```

**Kullanım:**
```python
from code.histogram_equalization import histogram_equalization

# Histogram eşitleme uygula
equalized = histogram_equalization(image)
```

**Parametreler:**
- `image` (numpy.ndarray): Giriş görüntüsü

**Dönüş Değeri:**
- `numpy.ndarray`: Histogram eşitlenmiş görüntü

**Kullanım Alanları:**
- Düşük kontrastlı görüntülerin iyileştirilmesi
- Medikal görüntüleme
- Gözetim kamerası görüntüleri

---

### 9. Gamma Düzeltmesi (Gamma Correction)

**Dosya:** `code/gamma_correction.py`

**Açıklama:** Doğrusal olmayan parlaklık ayarlama işlemi yapar.

**Matematiksel Formül:**
```
I_out(x, y) = 255 × (I_in(x, y) / 255)^γ
```
- `γ < 1`: Görüntüyü aydınlatır (koyu bölgeler daha görünür)
- `γ = 1`: Değişiklik yok
- `γ > 1`: Görüntüyü koyulaştırır (aydınlık bölgeler daha belirgin)

**Kullanım:**
```python
from code.gamma_correction import gamma_correction

# Görüntüyü aydınlat (gamma < 1)
lighter = gamma_correction(image, 0.5)

# Görüntüyü koyulaştır (gamma > 1)
darker = gamma_correction(image, 2.0)

# Standart gamma düzeltmesi
corrected = gamma_correction(image, 1.5)
```

**Parametreler:**
- `image` (numpy.ndarray): Giriş görüntüsü
- `gamma` (float): Gamma değeri (0.1-5.0 arası önerilir)

**Dönüş Değeri:**
- `numpy.ndarray`: Gamma düzeltmesi yapılmış görüntü

**Kullanım Alanları:**
- Monitör kalibrasyonu
- HDR görüntü işleme
- Gece görüntülerinin iyileştirilmesi

---

## 📁 Proje Yapısı

```
bigisayar_görü_ödev3/
│
├── code/                              # Ana kod modülleri
│   ├── __init__.py                    # Paket başlatıcı
│   ├── brightness_adjustment.py       # Parlaklık ayarlama modülü
│   ├── contrast_adjustment.py         # Kontrast ayarlama modülü
│   ├── negative_image.py              # Görüntü negatifi modülü
│   ├── thresholding.py                # Eşikleme modülü
│   ├── histogram_analysis.py          # Histogram analizi modülü
│   ├── image_statistics.py            # İstatistiksel analiz modülü
│   ├── contrast_stretching.py         # Kontrast germe modülü
│   ├── histogram_equalization.py      # Histogram eşitleme modülü
│   ├── gamma_correction.py            # Gamma düzeltmesi modülü
│   └── helpers.py                     # Yardımcı fonksiyonlar
│
├── images/                            # Giriş görüntüleri
│   └── lenna.png                      # Test görüntüsü
│
├── results/                           # İşlenmiş görüntüler
│   ├── brightness_adjusted.png        # Parlaklık ayarlı
│   ├── contrast_adjusted.png          # Kontrast ayarlı
│   ├── negative_image.png             # Negatif görüntü
│   ├── thresholded_image.png          # Eşiklenmiş görüntü
│   ├── contrast_stretched.png         # Kontrast gerilmiş
│   ├── equalized_image.png            # Histogram eşitlenmiş
│   └── gamma_corrected.png            # Gamma düzeltmeli
│
├── .venv/                             # Python sanal ortamı (opsiyonel)
├── main.py                            # Ana çalıştırma dosyası
├── a.py                               # Yardımcı temizleme scripti
├── requirements.txt                   # Python bağımlılıkları
└── README.md                          # Bu dosya
```

---

## 🔬 Teknik Detaylar

### Görüntü Formatı

- **Giriş:** RGB veya gri tonlamalı görüntüler
- **İşleme:** Gri tonlamalı (grayscale) görüntüler üzerinde
- **Çıkış:** 8-bit gri tonlamalı görüntüler (0-255 aralığı)

### Veri Tipleri

```python
# NumPy array formatı
image.dtype = np.uint8      # 8-bit unsigned integer
image.shape = (height, width)  # 2D array (gri tonlamalı)
```

### Performans Optimizasyonu

- **Vektörleştirilmiş İşlemler:** NumPy'nin vektörleştirilmiş operasyonları kullanılarak hız artırıldı
- **Bellek Yönetimi:** Gereksiz kopyalama işlemleri minimize edildi
- **Tip Dönüşümleri:** Sadece gerekli yerlerde uint8 dönüşümü yapıldı

### Hata Yönetimi

```python
# Değer sınırlama (clipping)
np.clip(image, 0, 255)  # Değerleri 0-255 aralığında tut

# Tip güvenliği
image.astype(np.uint8)  # uint8 formatına dönüştür
```

---

## 📸 Örnek Çıktılar

### Parlaklık Ayarlama Karşılaştırması

| Orijinal | Parlaklık +50 | Parlaklık -50 |
|----------|---------------|---------------|
| ![Original](images/lenna.png) | ![Bright](results/brightness_adjusted.png) | ![Dark](results/brightness_adjusted.png) |

### Kontrast İşlemleri

| Kontrast Ayarlama | Kontrast Germe | Histogram Eşitleme |
|-------------------|----------------|---------------------|
| ![Contrast](results/contrast_adjusted.png) | ![Stretch](results/contrast_stretched.png) | ![Equalized](results/equalized_image.png) |

### Diğer İşlemler

| Negatif | Eşikleme | Gamma Düzeltmesi |
|---------|----------|------------------|
| ![Negative](results/negative_image.png) | ![Threshold](results/thresholded_image.png) | ![Gamma](results/gamma_corrected.png) |

---

## 🧪 Test ve Doğrulama

### Manuel Test

```bash
python main.py
```

Çıktıları `results/` klasöründe kontrol edin.

### Kendi Testlerinizi Yazma

```python
import numpy as np
from PIL import Image
from code.brightness_adjustment import brightness_adjustment

# Test görüntüsü oluştur
test_image = np.random.randint(0, 256, (100, 100), dtype=np.uint8)

# İşlem uygula
result = brightness_adjustment(test_image, 50)

# Doğrulama
assert result.dtype == np.uint8
assert result.shape == test_image.shape
assert np.all(result >= 0) and np.all(result <= 255)
print("✅ Test başarılı!")
```

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Projeye katkıda bulunmak için:

1. **Fork** edin
2. **Feature branch** oluşturun (`git checkout -b feature/YeniOzellik`)
3. Değişikliklerinizi **commit** edin (`git commit -m 'Yeni özellik: XYZ'`)
4. Branch'inizi **push** edin (`git push origin feature/YeniOzellik`)
5. **Pull Request** oluşturun

### Katkı Kuralları

- Kod standartlarına uyun (PEP 8)
- Docstring'leri eksiksiz yazın
- Yeni özellikler için örnek kullanım ekleyin
- README'yi güncel tutun

---

## 📝 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

```
MIT License

Copyright (c) 2026 [Adınız]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 İletişim

**Proje Sahibi:** [Adınız]

- 📧 Email: [email@example.com]
- 🐙 GitHub: [@kullaniciadi](https://github.com/kullaniciadi)
- 💼 LinkedIn: [linkedin.com/in/profiliniz](https://linkedin.com/in/profiliniz)

**Proje Linki:** [https://github.com/kullaniciadi/bigisayar_goru_odev3](https://github.com/kullaniciadi/bigisayar_goru_odev3)

---

## 🙏 Teşekkürler

- **NumPy Topluluğu** - Güçlü sayısal hesaplama kütüphanesi için
- **Matplotlib Geliştiricileri** - Görselleştirme araçları için
- **PIL/Pillow Ekibi** - Görüntü işleme desteği için
- **Bilgisayar Görü Topluluğu** - İlham ve kaynak materyaller için

---

## 📚 Kaynaklar ve Referanslar

### Kitaplar
- Gonzalez, R. C., & Woods, R. E. (2018). *Digital Image Processing* (4th ed.). Pearson.
- Szeliski, R. (2022). *Computer Vision: Algorithms and Applications* (2nd ed.). Springer.

### Online Kaynaklar
- [NumPy Documentation](https://numpy.org/doc/)
- [OpenCV Tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html)
- [Image Processing Fundamentals](https://homepages.inf.ed.ac.uk/rbf/HIPR2/)

### Akademik Makaleler
- Pizer, S. M., et al. (1987). "Adaptive histogram equalization and its variations"
- Rahman, Z., et al. (1996). "Multi-scale retinex for color image enhancement"

---

## 🔄 Versiyon Geçmişi

### v1.0.0 (2026-01-02)
- ✨ İlk sürüm yayınlandı
- ✅ 9 temel görüntü işleme algoritması eklendi
- ✅ Kapsamlı dokümantasyon hazırlandı
- ✅ Örnek görüntüler ve test senaryoları eklendi

---

## 🎯 Gelecek Planları

- [ ] Renkli görüntü desteği
- [ ] Adaptif eşikleme algoritmaları
- [ ] Morfolojik işlemler (erosion, dilation)
- [ ] Kenar algılama (Sobel, Canny)
- [ ] Gürültü azaltma filtreleri
- [ ] GUI arayüzü (Tkinter/PyQt)
- [ ] Batch işleme desteği
- [ ] Video işleme özellikleri

---

<div align="center">

**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın! ⭐**

Made with ❤️ by [Adınız]

</div>
