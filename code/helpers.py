import matplotlib.pyplot as plt

def plot_images_and_histograms(original, processed):
    """
    Orijinal ve işlenmiş görüntüleri yanı sıra histogramlarını da gösterir.
    
    :param original: Orijinal görüntü (numpy array).
    :param processed: İşlenmiş görüntü (numpy array).
    """
    plt.figure(figsize=(10, 5))
    
    # Görsel 1: Orijinal
    plt.subplot(2, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.title("Orijinal Görüntü")
    plt.axis('off')
    
    # Görsel 2: İşlenmiş
    plt.subplot(2, 2, 2)
    plt.imshow(processed, cmap='gray')
    plt.title("İşlenmiş Görüntü")
    plt.axis('off')

    # Histogram 1: Orijinal
    plt.subplot(2, 2, 3)
    plot_histogram(compute_histogram(original))
    
    # Histogram 2: İşlenmiş
    plt.subplot(2, 2, 4)
    plot_histogram(compute_histogram(processed))
    
    plt.show()
