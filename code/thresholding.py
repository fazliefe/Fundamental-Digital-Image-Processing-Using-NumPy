def thresholding(image, threshold_value):
    """
    Görüntü üzerinde eşikleme işlemi yapar.
    
    :param image: Girdi görüntüsü (numpy array).
    :param threshold_value: Eşik değeri.
    :return: Eşikleme yapılmış görüntü.
    """
    thresholded_image = np.where(image > threshold_value, 255, 0)  # Eşikleme işlemi
    return thresholded_image.astype(np.uint8)
