import numpy as np

def brightness_adjustment(image, brightness_value):
    """
    Görüntü üzerinde parlaklık ayarı yapar.
    
    :param image: Girdi görüntüsü (numpy array).
    :param brightness_value: Parlaklık değeri (pozitif veya negatif).
    :return: Parlaklığı ayarlanmış görüntü.
    """
    adjusted_image = np.clip(image + brightness_value, 0, 255)  # 0-255 aralığında tutma
    return adjusted_image.astype(np.uint8)
