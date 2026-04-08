import matplotlib.pyplot as plt
import cv2 as cv

def histograma_gray_scale(image):
    histogram = [0] * 256

    for row in image:
        for pixel in row:
            histogram[pixel] += 1

    intensidades = list(range(256))

    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(10, 5))
    plt.plot(intensidades, histogram, color='#2D3436', linewidth=2.2)
    plt.fill_between(intensidades, histogram, color='#74B9FF', alpha=0.25)
    plt.title('Histograma - Imagem em Tons de Cinza', fontsize=14, fontweight='bold')
    plt.xlabel('Intensidade do Pixel (0-255)')
    plt.ylabel('Frequencia')
    plt.xlim(0, 255)
    plt.ylim(bottom=0)
    plt.tight_layout()
    plt.show()

    return histogram

if __name__ == "__main__":

    image = cv.imread("img/niguilos.jpeg")

    if image is None:
        raise FileNotFoundError("Nao foi possivel carregar a imagem em img/niguilos.jpeg")

    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    cv.imshow("Imagem Original", image)
    cv.imshow("Imagem Gray Scale", image_gray)
    cv.waitKey(0)
    cv.destroyAllWindows()

    histogram = histograma_gray_scale(image_gray)