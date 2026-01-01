def histogram_equalization(image):
    """
    Görüntü üzerinde histogram eşitleme işlemi yapar.
    
    :param image: Girdi görüntüsü (numpy array).
    :return: Eşitlenmiş görüntü.
    """
    # Histogramı hesapla
    histogram = compute_histogram(image)
    
    # Kümülatif dağılım fonksiyonu (CDF) hesapla
    cdf = np.cumsum(histogram) / image.size
    
    # Dönüşüm fonksiyonu
    transform = np.floor(255 * cdf).astype(np.uint8)
    
    # Görüntüdeki her pikseli dönüştür
    equalized_image = transform[image]
    return equalized_image
