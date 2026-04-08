import cv2
import numpy as np

# Carregar a imagem em tons de cinza
img_original = cv2.imread('img/niguilos.jpeg', 0)
img = cv2.imread('img/niguilos.jpeg', 0)

# 1. Equalização de Histograma Global
img_equalizada = cv2.equalizeHist(img)

# 2. CLAHE (Contrast Limited Adaptive Histogram Equalization)
# Uma versão melhorada que divide a imagem em blocos para evitar ruído excessivo
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img_clahe = clahe.apply(img)

img_transformada = img

c = (img.max() - img.min()) / 255.0  # escala de níveis de cinza
b = img.max() + img.min() / 2.0  # ajuste de brilho
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img_transformada[i, j] = c * img[i, j] + b

# Salvar ou exibir os resultados
cv2.imshow('imagem_original.jpg', img_original)
cv2.imshow('resultado_equalizado.jpg', img_equalizada)
cv2.imshow('resultado_clahe.jpg', img_clahe)
cv2.imshow('resultado_transformada.jpg', img_transformada)
cv2.waitKey(0)
cv2.destroyAllWindows()