import cv2

def negativo (img, w) :
    img2 = img.copy()
    for i in range (img2.shape[0]) :
        for j in range (img2.shape[1]) :
            img2[i, j] = w - img[i, j]
    return img2

def binarizacao (img, t) :
    img2 = img.copy()
    for i in range (img2.shape[0]) :
        for j in range (img2.shape[1]) :
            if img[i, j] < t :
                img2[i, j] = 0
            else :
                img2[i, j] = 255
    return img2

def ternarizacao (img, t1, t2) :
    img2 = img.copy()
    for i in range (img2.shape[0]) :
        for j in range (img2.shape[1]) :
            if img[i, j] < t1 :
                img2[i, j] = 0
            elif img[i, j] > t2 :
                img2[i, j] = 255
    return img2

def alargamento_de_contraste (img, t1, t2, k1, k2, k3) :
    img2 = img.copy()
    for i in range (img2.shape[0]) :
        for j in range (img2.shape[1]) :
            if img[i, j] < t1 :
                img2[i, j] = k1 * img[i, j]
            elif img[i, j] > t2 :
                img2[i, j] = k3 * img[i, j]
            else :
                img2[i, j] = k2 * img[i, j]
    return img2

def equalizacao_histograma (img) :
    g = []
    L_max = img.max()
    img2 = img.copy()
    g_acumulado = 0

    # calcular probabilidade de cada nível de cinza
    for i in range (256) :
        # n_i = número de pixels com nível de cinza i
        n_i = (img == i).sum()
        g_acumulado = g_acumulado + n_i / (img.shape[0] * img.shape[1])
        g.append(g_acumulado)

    g_equalizado = []
    for i in range (len(g)) :
        g_equalizado.append(int(g[i] * (L_max)))

    for i in range (img.shape[0]) :
        for j in range (img.shape[1]) :
            img2[i, j] = g_equalizado[int(img[i, j])]

    return img2

if __name__ == "__main__":
    img = cv2.imread('../aula01/img/dlss.jpg', 0)
    w = img.max() + 1

    img_negativo = negativo(img, w)
    img_binarizada = binarizacao(img, w/2)
    img_binarizada2 = binarizacao(img, 255/2)
    img_ternarizada = ternarizacao(img, w/3, 2*w/3)
    img_alargada = alargamento_de_contraste(img, w/3, 2*w/3, 0.5, 1.1, 1.6)
    img_equalizada = equalizacao_histograma(img)

    cv2.imshow('Imagem Original', img)
    # cv2.imshow('Imagem Negativa', img_negativo)
    # cv2.imshow('Imagem Binarizada - v1', img_binarizada)
    # cv2.imshow('Imagem Binarizada - v2', img_binarizada2)
    cv2.imshow('Imagem Ternarizada', img_ternarizada)
    cv2.imshow('Imagem Alargada', img_alargada)
    cv2.imshow('Imagem Equalizada', img_equalizada)

    cv2.waitKey(0)
    
    cv2.destroyAllWindows()