import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from code.brightness_adjustment import brightness_adjustment
from code.contrast_adjustment import contrast_adjustment
from code.negative_image import negative_image
from code.thresholding import thresholding
from code.histogram_analysis import compute_histogram, plot_histogram
from code.image_statistics import image_statistics
from code.contrast_stretching import contrast_stretching
from code.histogram_equalization import histogram_equalization
from code.gamma_correction import gamma_correction

# Görüntüleri yükle
image_path = 'images/lenna.png'  # Örnek test görüntüsü
image = np.array(Image.open(image_path).convert('L'))  # Gri tonlamaya çevir

# Parlaklık Ayarlama
brightness_value = 50
brightness_image = brightness_adjustment(image, brightness_value)

# Kontrast Ayarlama
contrast_factor = 1.5
contrast_image = contrast_adjustment(image, contrast_factor)

# Görüntü Negatifi
negative_img = negative_image(image)

# Eşikleme (Thresholding)
threshold_value = 128
thresholded_img = thresholding(image, threshold_value)

# Histogram Hesaplama ve Görselleştirme
histogram = compute_histogram(image)
plot_histogram(histogram)

# Görüntü İstatistikleri
image_statistics(image)

# Kontrast Germe (Contrast Stretching)
stretched_image = contrast_stretching(image)

# Histogram Eşitleme
equalized_image = histogram_equalization(image)

# Gamma Düzeltmesi
gamma = 1.5
gamma_corrected_image = gamma_correction(image, gamma)

# İşlenmiş Görselleri Kaydetme
Image.fromarray(brightness_image).save('results/brightness_adjusted.png')
Image.fromarray(contrast_image).save('results/contrast_adjusted.png')
Image.fromarray(negative_img).save('results/negative_image.png')
Image.fromarray(thresholded_img).save('results/thresholded_image.png')
Image.fromarray(stretched_image).save('results/contrast_stretched.png')
Image.fromarray(equalized_image).save('results/equalized_image.png')
Image.fromarray(gamma_corrected_image).save('results/gamma_corrected.png')

# Görselleştirme
plt.figure(figsize=(12, 6))

plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(brightness_image, cmap='gray')
plt.title('Parlaklık Ayarlı Görüntü')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(contrast_image, cmap='gray')
plt.title('Kontrast Ayarlı Görüntü')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(negative_img, cmap='gray')
plt.title('Negatif Görüntü')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(thresholded_img, cmap='gray')
plt.title('Eşiklenmiş Görüntü')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(stretched_image, cmap='gray')
plt.title('Kontrast Gerilmiş Görüntü')
plt.axis('off')

plt.show()
