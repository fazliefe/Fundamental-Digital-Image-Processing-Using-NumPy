def image_statistics(image):
    """
    Görüntü istatistiklerini hesaplar.
    
    :param image: Girdi görüntüsü (numpy array).
    :return: Ortalama, standart sapma, entropi, min, max.
    """
    mean = np.mean(image)
    std_dev = np.std(image)
    entropy = -np.sum(image * np.log2(image + 1e-5)) / image.size
    min_val = np.min(image)
    max_val = np.max(image)
    
    print(f"Ortalama: {mean}")
    print(f"Standart Sapma: {std_dev}")
    print(f"Entropi: {entropy}")
    print(f"Min Değer: {min_val}")
    print(f"Max Değer: {max_val}")
