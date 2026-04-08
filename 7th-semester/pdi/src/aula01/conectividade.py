from vizinhanca import img_vizinhanca_4_rgb, img_vizinhanca_8_rgb
import cv2
import numpy as np

def conectividade(original, vizinhos, x, y, c) :
    conectividade = []

    for vizinho in vizinhos :
        if vizinho >= original*0.9 and vizinho <= original*1.1 :
            conectividade.append(vizinho)
    
    return conectividade



if __name__ == "__main__":
    image = cv2.imread("img/dlss.jpg")
    x, y = 100, 100

    vizinhanca_4 = img_vizinhanca_4_rgb(image, x, y, 0) + img_vizinhanca_4_rgb(image, x, y, 1) + img_vizinhanca_4_rgb(image, x, y, 2)
    # vizinhanca_8 = img_vizinhanca_8_rgb(image, x, y, 0) + img_vizinhanca_8_rgb(image, x, y, 1) + img_vizinhanca_8_rgb(image, x, y, 2)

    print(f"Vizinhanca 4 (len = {len(vizinhanca_4)}): ", vizinhanca_4)

    original = image[x][y][0]
    conectividade_4 = conectividade(np.array(original), vizinhanca_4, x, y, 0)
    print(f"Conectividade 4 (canal 0 | len = {len(conectividade_4)} | original = {original}): ", conectividade_4)
    # conectividade_8 = conectividade(np.array(original), vizinhanca_8, x, y, 0)

    original = image[x][y][1]
    conectividade_4 = conectividade(np.array(original), vizinhanca_4, x, y, 1)
    print(f"Conectividade 4 (canal 1 | len = {len(conectividade_4)} | original = {original}): ", conectividade_4)
    # conectividade_8 = conectividade(np.array(original), vizinhanca_8, x, y, 1)

    original = image[x][y][2]
    conectividade_4 = conectividade(np.array(original), vizinhanca_4, x, y, 2)
    print(f"Conectividade 4 (canal 2 | len = {len(conectividade_4)} | original = {original}): ", conectividade_4)
    # conectividade_8 = conectividade(np.array(original), vizinhanca_8, x, y, 2)

