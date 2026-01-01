def contrast_adjustment(image, factor):
    """
    Görüntü üzerinde kontrast ayarı yapar.
    
    :param image: Girdi görüntüsü (numpy array).
    :param factor: Kontrast faktörü.
    :return: Kontrastı ayarlanmış görüntü.
    """
    adjusted_image = factor * (image - 128) + 128  # Kontrast ayarı formülü
    adjusted_image = np.clip(adjusted_image, 0, 255)  # 0-255 aralığında tutma
    return adjusted_image.astype(np.uint8)