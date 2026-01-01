def gamma_correction(image, gamma):
    """
    Görüntü üzerinde gamma düzeltmesi yapar.
    
    :param image: Girdi görüntüsü (numpy array).
    :param gamma: Gamma değeri.
    :return: Gamma düzeltmesi yapılmış görüntü.
    """
    corrected_image = 255 * (image / 255) ** gamma
    return np.clip(corrected_image, 0, 255).astype(np.uint8)
