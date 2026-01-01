def contrast_stretching(image):
    """
    Görüntüde kontrast germe işlemi yapar.
    
    :param image: Girdi görüntüsü (numpy array).
    :return: Kontrast gerilmiş görüntü.
    """
    min_val = np.min(image)
    max_val = np.max(image)
    stretched_image = ((image - min_val) / (max_val - min_val)) * 255
    return stretched_image.astype(np.uint8)
