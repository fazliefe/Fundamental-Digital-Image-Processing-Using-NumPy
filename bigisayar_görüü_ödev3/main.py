import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from typing import Optional, List


L = 256  # gri seviye düzeyi

# ---------------------------------------------------------
# Yardımcı Fonksiyonlar
# ---------------------------------------------------------
def read_image_gray(path: str) -> np.ndarray:
    """
    Verilen dosya yolundaki görüntüyü gri seviyeye çevirip (uint8) numpy array döndürür.
    Ayrıca dosyanın varlığını kontrol eder.

    Parameters
    ----------
    path : str
        Görüntü dosya yolu.

    Returns
    -------
    img : np.ndarray, dtype=np.uint8, shape=(H,W)
        Gri seviye görüntü.
    """
    # Dosya yolunun geçerli olduğunu kontrol et
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dosya bulunamadı: {path}")
    
    try:
        # Görüntüyü aç ve gri seviyeye dönüştür
        img = Image.open(path).convert("L")
    except Exception as e:
        raise ValueError(f"Görüntü dosyası açılırken bir hata oluştu: {e}")

    return np.array(img, dtype=np.uint8)


def save_image(path: str, img: np.ndarray) -> None:
    """
    Görüntüyü (uint8) olarak kaydeder.
    """
    Image.fromarray(img.astype(np.uint8)).save(path)


def clip_uint8(arr: np.ndarray) -> np.ndarray:
    """
    0-255 aralığına kırpıp uint8 döndürür.
    """
    return np.clip(arr, 0, 255).astype(np.uint8)


def ensure_gray(img: np.ndarray) -> np.ndarray:
    """
    Eğer görüntü renkli ise (H,W,3) -> gri'ye çevirir.
    """
    if img.ndim == 3:
        # basit luma dönüşümü
        # Y = 0.299 R + 0.587 G + 0.114 B
        img = (0.299*img[...,0] + 0.587*img[...,1] + 0.114*img[...,2]).astype(np.uint8)
    return img


# ---------------------------------------------------------
# Soru 1: Temel Nokta İşlemleri
# ---------------------------------------------------------
def adjust_brightness(img: np.ndarray, delta: int) -> np.ndarray:
    """
    Parlaklık ayarlama: her piksele sabit ekle/çıkar (taşma kontrolü ile).

    output = clip(input + delta)

    Parameters
    ----------
    img : np.ndarray (uint8)
    delta : int  (ör: +40 veya -30)

    Returns
    -------
    np.ndarray (uint8)
    """
    img = ensure_gray(img)
    return clip_uint8(img.astype(np.int16) + int(delta))


def adjust_contrast(img: np.ndarray, factor: float) -> np.ndarray:
    """
    Kontrast ayarlama:
        output = factor * (input - 128) + 128
    Taşma kontrolü yapılır.

    Parameters
    ----------
    img : np.ndarray (uint8)
    factor : float (örn: 1.5, 0.8)

    Returns
    -------
    np.ndarray (uint8)
    """
    img = ensure_gray(img).astype(np.float32)
    out = factor * (img - 128.0) + 128.0
    return clip_uint8(out)


def negative(img: np.ndarray) -> np.ndarray:
    """
    Görüntü negatif:
        output = 255 - input
    """
    img = ensure_gray(img).astype(np.int16)
    return clip_uint8(255 - img)


def threshold(img: np.ndarray, th: int) -> np.ndarray:
    """
    Eşikleme:
        p > th -> 255, aksi halde 0
    """
    img = ensure_gray(img)
    return (img > th).astype(np.uint8) * 255


def show_side_by_side(images: List[np.ndarray], titles: Optional[List[str]] = None, suptitle: Optional[str] = None):
    """
    Görselleri yan yana gösterir. (Ödev gereği görselleştirme kolaylığı için)
    """
    n = len(images)
    plt.figure(figsize=(4*n, 4))
    for i, im in enumerate(images):
        plt.subplot(1, n, i+1)
        plt.imshow(im, cmap='gray', vmin=0, vmax=255)
        if titles and i < len(titles):
            plt.title(titles[i])
        plt.axis('off')
    if suptitle:
        plt.suptitle(suptitle)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# Soru 2: Histogram Analizi ve Görselleştirme
# ---------------------------------------------------------
def histogram_manual(img: np.ndarray) -> np.ndarray:
    """
    Manuel histogram (hazır fonksiyon yok):
    Her gri seviye (0..255) için piksel sayısını döndürür.

    Returns
    -------
    hist : np.ndarray shape=(256,), dtype=np.int64
    """
    img = ensure_gray(img)
    # bincount ile verimli histogram
    hist = np.bincount(img.ravel(), minlength=L).astype(np.int64)
    return hist


def plot_histogram(hist: np.ndarray, title: str = "Histogram"):
    """
    Histogram grafik (x=0..255, y=sayı)
    """
    x = np.arange(L)
    plt.figure(figsize=(6,4))
    plt.bar(x, hist, width=1.0)
    plt.title(title)
    plt.xlabel("Gri Seviye")
    plt.ylabel("Piksel Sayısı")
    plt.tight_layout()
    plt.show()


def image_stats(img: np.ndarray) -> dict:
    """
    Görüntü istatistikleri: mean, std, entropy, min, max

    Entropi hesaplaması:
        p_i = hist[i] / (M*N)
        H = -sum_i p_i * log2(p_i), p_i>0 için
    """
    img = ensure_gray(img)
    hist = histogram_manual(img)
    total = img.size
    probs = hist / total
    # p>0 için -p*log2(p)
    nz = probs > 0
    entropy = float(-(probs[nz] * np.log2(probs[nz])).sum())
    stats = {
        "mean": float(img.mean()),
        "std": float(img.std(ddof=0)),
        "entropy": entropy,
        "min": int(img.min()),
        "max": int(img.max()),
    }
    return stats


# ---------------------------------------------------------
# Soru 3: Kontrast Germe (Contrast Stretching)
# ---------------------------------------------------------
def contrast_stretch(img: np.ndarray) -> np.ndarray:
    """
    Kontrast germe:
        output = ((input - min) / (max - min)) * 255

    max==min durumunda düz kopya döndürür (bölme hatasını önlemek için).
    """
    img = ensure_gray(img).astype(np.float32)
    imin = float(img.min())
    imax = float(img.max())
    if imax <= imin:
        return img.astype(np.uint8)  # düz kopya
    out = (img - imin) / (imax - imin) * 255.0
    return clip_uint8(out)


def plot_cs_compare(img: np.ndarray):
    """
    Orijinal + kontrast gerilmiş görüntü ve iki histogramın 2x2 subplot gösterimi.
    """
    proc = contrast_stretch(img)
    hist_o = histogram_manual(img)
    hist_p = histogram_manual(proc)

    fig, axs = plt.subplots(2, 2, figsize=(8,6))
    axs[0,0].imshow(img, cmap='gray', vmin=0, vmax=255)
    axs[0,0].set_title("Orijinal")
    axs[0,0].axis('off')

    axs[0,1].imshow(proc, cmap='gray', vmin=0, vmax=255)
    axs[0,1].set_title("Kontrast Gerilmiş")
    axs[0,1].axis('off')

    x = np.arange(L)
    axs[1,0].bar(x, hist_o, width=1.0)
    axs[1,0].set_title("Orijinal Histogram")

    axs[1,1].bar(x, hist_p, width=1.0)
    axs[1,1].set_title("Kontrast Gerilmiş Histogram")

    for ax in axs[1,:]:
        ax.set_xlabel("Gri Seviye")
        ax.set_ylabel("Piksel Sayısı")

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# Soru 4: Histogram Eşitleme
# ---------------------------------------------------------
def hist_equalize_manual(img: np.ndarray) -> np.ndarray:
    """
    Elle histogram eşitleme.

    Adımlar:
      1) hist = manuel histogram
      2) pdf = hist / (M*N)
      3) cdf = pdf'in kümülatif toplamı
      4) dönüşüm: s_k = round((L-1) * cdf[k])
      5) tüm piksellere uygulama
    """
    img = ensure_gray(img)
    hist = histogram_manual(img).astype(np.float64)
    total = img.size
    pdf = hist / total
    cdf = np.cumsum(pdf)
    # dönüşüm fonksiyonu (0..255 -> 0..255)
    T = np.round((L-1) * cdf).astype(np.uint8)
    # piksel eşleme
    out = T[img]
    return out


def plot_he_compare(img: np.ndarray):
    """
    Orijinal ve eşitlenmiş görüntüler + her birinin histogramları (2x2 subplot).
    """
    he = hist_equalize_manual(img)
    hist_o = histogram_manual(img)
    hist_h = histogram_manual(he)

    fig, axs = plt.subplots(2, 2, figsize=(8,6))
    axs[0,0].imshow(img, cmap='gray', vmin=0, vmax=255)
    axs[0,0].set_title("Orijinal")
    axs[0,0].axis('off')

    axs[0,1].imshow(he, cmap='gray', vmin=0, vmax=255)
    axs[0,1].set_title("Histogram Eşitlenmiş")
    axs[0,1].axis('off')

    x = np.arange(L)
    axs[1,0].bar(x, hist_o, width=1.0)
    axs[1,0].set_title("Orijinal Histogram")

    axs[1,1].bar(x, hist_h, width=1.0)
    axs[1,1].set_title("Eşitlenmiş Histogram")

    for ax in axs[1,:]:
        ax.set_xlabel("Gri Seviye")
        ax.set_ylabel("Piksel Sayısı")

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# Soru 5: Gamma Düzeltmesi
# ---------------------------------------------------------
def gamma_correction(img: np.ndarray, gamma: float) -> np.ndarray:
    """
    Gamma düzeltme:
        output = 255 * (input/255)^gamma
    """
    img = ensure_gray(img).astype(np.float32) / 255.0
    out = 255.0 * np.power(img, float(gamma))
    return clip_uint8(out)


def plot_gamma_series(img: np.ndarray, gammas=(0.5, 1.0, 1.5, 2.0, 2.5)):
    """
    Farklı gamma değerleri için görüntüleri yan yana gösterir.
    """
    imgs = [img] + [gamma_correction(img, g) for g in gammas]
    titles = ["Orijinal"] + [f"γ={g}" for g in gammas]
    show_side_by_side(imgs, titles, suptitle="Gamma Düzeltmesi")


# ---------------------------------------------------------
# Ana Demo Fonksiyonu
# ---------------------------------------------------------
def run_demo(image_path: Optional[str] = "images/indir(1).jpg", out_dir: str = "sonuclar") -> None:
    """
    Hızlı demo: tek bir görüntü üzerinde tüm soruları çalıştırır ve sonuçları kaydeder.
    - Eğer image_path vermezseniz sentetik düşük kontrastlı görüntü üretir.
    - Grafikleri ekranda gösterir, ayrıca çıktı görsellerini diske kaydeder.
    """
    os.makedirs(out_dir, exist_ok=True)

    # Dosya yolunun geçerli olduğundan emin olun
    if not os.path.exists(image_path):
        print(f"Dosya bulunamadı: {image_path}")
        return  # Çıkış yap

    img = read_image_gray(image_path)

    # Soru 1
    b_plus = adjust_brightness(img, +40)
    b_minus = adjust_brightness(img, -40)
    c_15 = adjust_contrast(img, 1.5)
    neg = negative(img)
    th_120 = threshold(img, 120)

    save_image(os.path.join(out_dir, "01_brightness_plus40.png"), b_plus)
    save_image(os.path.join(out_dir, "01_brightness_minus40.png"), b_minus)
    save_image(os.path.join(out_dir, "01_contrast_factor1_5.png"), c_15)
    save_image(os.path.join(out_dir, "01_negative.png"), neg)
    save_image(os.path.join(out_dir, "01_threshold_120.png"), th_120)

    show_side_by_side([img, b_plus, b_minus, c_15, neg, th_120],
                      ["Orijinal", "Parlaklık +40", "Parlaklık -40", "Kontrast x1.5", "Negatif", "Eşik 120"],
                      "Soru 1: Nokta İşlemleri")

    # Soru 2
    hist = histogram_manual(img)
    plot_histogram(hist, "Soru 2a: Manuel Histogram")
    stats = image_stats(img)
    print("Soru 2b: Görüntü İstatistikleri")
    for k, v in stats.items():
        print(f"  {k}: {v}")

    # Soru 3
    plot_cs_compare(img)
    cs = contrast_stretch(img)
    save_image(os.path.join(out_dir, "03_contrast_stretch.png"), cs)

    # Soru 4
    plot_he_compare(img)
    he = hist_equalize_manual(img)
    save_image(os.path.join(out_dir, "04_hist_equalized.png"), he)

    # Soru 5
    plot_gamma_series(img, gammas=(0.5, 1.0, 1.5, 2.0, 2.5))
    for g in (0.5, 1.0, 1.5, 2.0, 2.5):
        save_image(os.path.join(out_dir, f"05_gamma_{g}.png"), gamma_correction(img, g))

    print(f"Tüm çıktı görselleri '{out_dir}/' klasörüne kaydedildi.")


# ---------------------------------------------------------
# Komut Satırı Arayüzü
# ---------------------------------------------------------
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Bilgisayarla Görü 3. Ödev - Nokta ve Histogram İşlemleri (Manual)")
    parser.add_argument("--image", type=str, default="images/lena_gray.gif", help="Girdi gri seviye görüntü yolu (verilmezse sentetik düşük kontrastlı görüntü kullanılır)")
    parser.add_argument("--out_dir", type=str, default="sonuclar", help="Çıktıların kaydedileceği klasör")
    args = parser.parse_args()

    run_demo(image_path=args.image, out_dir=args.out_dir)
