import matplotlib.pyplot as plt

def apply_gaussian_noise(image, mean=0, stddev=25):
    import numpy as np
    gaussian_noise = np.random.normal(mean, stddev, image.shape)
    noisy_image = image + gaussian_noise
    return np.clip(noisy_image, 0, 255).astype(np.uint8)

def plt_histogram(image, title, max_y=None):
    histogram = [0] * 256

    for row in image:
        for pixel in row:
            histogram[pixel] += 1

    intensidades = list(range(256))

    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(10, 5))
    plt.plot(intensidades, histogram, color='#2D3436', linewidth=2.2)
    plt.fill_between(intensidades, histogram, color='#74B9FF', alpha=0.25)
    plt.title(title+f" - (max y = {max_y})", fontsize=14, fontweight='bold')
    plt.xlabel('Intensidade do Pixel (0-255)')
    plt.ylabel('Frequencia')
    plt.xlim(0, 255)
    if max_y is None:
        plt.ylim(bottom=0)
    else:
        plt.ylim(0, max_y)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    import cv2 as cv

    image = cv.imread("img/niguilos.jpeg")

    if image is None:
        raise FileNotFoundError("Nao foi possivel carregar a imagem em img/niguilos.jpeg")

    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


    noisy_image = apply_gaussian_noise(image_gray, mean=0, stddev=25)


    print("tamanho da imagem (original): ", image.shape)
    print("tamanho da imagem (cinza): ", image_gray.shape)
    print("tamanho da imagem (noise): ", noisy_image.shape)
    cv.imshow("Imagem Original", image_gray)
    cv.imshow("Imagem com Ruido Gaussiano", noisy_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    plt_histogram(noisy_image, "COM ruído gaussiano", max_y=1000)
    plt_histogram(image_gray, "SEM ruído gaussiano", max_y=1000)

