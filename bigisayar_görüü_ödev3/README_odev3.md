# Bilgisayarla Görü 3. Ödev (Nokta İşlemleri & Histogram İşleme)

**Ders:** Görüntü İşleme (Dr. Öğr. Üyesi Ramin Abbaszadi)  
**Teslim:** 15.11.2025 (PDF yönergesi)

Bu repo/klasör, ödevde istenen tüm soruların **elle (manual)** implementasyonlarını içeren tek bir Python dosyası sağlar: `bilgisayarla_goru_odev3.py`

---

## Kurulum

```bash
pip install numpy matplotlib pillow opencv-python
```

> Not: Kod, yalnızca NumPy + Matplotlib + PIL (veya OpenCV ile okuma) kullanır; histogram hesaplama ve histogram eşitlemede **hazır fonksiyon yoktur**.

---

## Çalıştırma

En hızlı şekilde bir sentetik (düşük kontrastlı) test görüntüsüyle tüm demoyu çalıştırmak için:

```bash
python bilgisayarla_goru_odev3.py
```

Kendi gri seviye görüntünüzle çalıştırmak için:

```bash
python bilgisayarla_goru_odev3.py --image PATH/TO/image.png --out_dir sonuclar
```

Çıktılar `sonuclar/` klasörüne kaydedilir ve ara görseller/plotlar ekranda gösterilir.

---

## Dosya Yapısı

- `bilgisayarla_goru_odev3.py`: Tüm fonksiyonlar (Soru 1–5), görselleştirmeler ve CLI.
- `sonuclar/`: Koşumdan sonra otomatik oluşur; çıktı görselleri burada.

---

## Fonksiyon Özeti

### Soru 1 – Temel Nokta İşlemleri
- `adjust_brightness(img, delta)` — Parlaklık ayarı (taşma kontrolü).
- `adjust_contrast(img, factor)` — Kontrast ayarı (`factor*(x-128)+128`, taşma kontrolü).
- `negative(img)` — Negatif alma (`255 - x`).
- `threshold(img, th)` — Eşikleme (`x>th ? 255 : 0`).
- `show_side_by_side([...])` — Yan yana görselleştirme (ödev beklenen çıktısı).

### Soru 2 – Histogram Analizi & Görselleştirme
- `histogram_manual(img)` — **Manuel** histogram (`np.bincount` ile).
- `plot_histogram(hist)` — Histogramı çizer.
- `image_stats(img)` — Ortalama, std, **entropi**, min, max.

### Soru 3 – Kontrast Germe
- `contrast_stretch(img)` — `((x-min)/(max-min))*255`
- `plot_cs_compare(img)` — Orijinal/işlenmiş + her ikisinin histogramları (**2x2 subplot**).

### Soru 4 – Histogram Eşitleme
- `hist_equalize_manual(img)` — **Elle** HE (CDF tabanlı dönüşüm).
- `plot_he_compare(img)` — Orijinal/Eşitlenmiş + histogramlar (**2x2 subplot**).

### Soru 5 – Gamma Düzeltmesi
- `gamma_correction(img, gamma)` — `255*(x/255)^gamma`
- `plot_gamma_series(img)` — `γ∈{0.5,1.0,1.5,2.0,2.5}` görsel karşılaştırma.

---

## Rapor İpuçları (Kısa)

- Her soruda, ilgili formülleri ve görsel çıktıları **kısa açıklamalarla** destekleyin.
- Soru 5 için: küçük γ (<1) karanlık bölgeleri **aydınlatır**, büyük γ (>1) parlak bölgeleri **bastırır**. Aydınlatma yetersiz görüntüler için γ<1; aşırı parlak/saturasyona yakın görüntüler için γ>1 kullanılabilir.
- Soru 3 ve 4’te, histogramların yayılması (stretching) ve düzleşmesi (equalization) etkisini tartışın.

---

## Notlar

- Girdi görüntüsü renkliyse fonksiyonlar otomatik gri seviyeye dönüştürür.
- Tüm işlemler **vektörize** edilir (performans ve temizlik için).
- Kodu parça parça çalıştırmak/incelemek için fonksiyonlar sade tutulmuştur.
