def compute_histogram(image):
    """
    Görüntünün histogramını hesaplar.
    
    :param image: Girdi görüntüsü (numpy array).
    :return: Histogram (numpy array).
    """
    histogram = np.zeros(256)
    for pixel in image.ravel():  # Görüntüdeki tüm pikselleri düzleştirip sayıyoruz
        histogram[pixel] += 1
    return histogram

def plot_histogram(histogram):
    """
    Histogramı görselleştirir.
    
    :param histogram: Histogram verisi.
    """
    plt.plot(histogram)
    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()
