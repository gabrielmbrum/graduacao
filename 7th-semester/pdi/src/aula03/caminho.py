import cv2

matrix = [[1, 0, 0],
          [1, 1, 1],
          [0, 0, 1]]

MAX_DIST = float('inf')

init = (0, 0)
dest = (10, 50)

def conectividade_4(matrix, x, y) :
    conexos = []
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    if x >= rows or y >= cols or x < 0 or y < 0 :
        print("Coordenadas fora do limite da matriz")
        return conexos

    if x + 1 < rows and matrix[x + 1][y] == matrix[x][y] :
        conexos.append((x + 1, y))
    if x - 1 >= 0 and matrix[x - 1][y] == matrix[x][y] :
        conexos.append((x - 1, y))
    if y + 1 < cols and matrix[x][y + 1] == matrix[x][y] :
        conexos.append((x, y + 1))
    if y - 1 >= 0 and matrix[x][y - 1] == matrix[x][y] :
        conexos.append((x, y - 1))

    return conexos

def conectividade_8(matrix, x, y) :
    conexos = conectividade_4(matrix, x, y)
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    if x - 1 >= 0 and y - 1 >= 0 and matrix[x - 1][y - 1] == matrix[x][y] :
        conexos.append((x - 1, y - 1))
    if x - 1 >= 0 and y + 1 < cols and matrix[x - 1][y + 1] == matrix[x][y] :
        conexos.append((x - 1, y + 1))
    if x + 1 < rows and y - 1 >= 0 and matrix[x + 1][y - 1] == matrix[x][y] :
        conexos.append((x + 1, y - 1))
    if x + 1 < rows and y + 1 < cols and matrix[x + 1][y + 1] == matrix[x][y] :
        conexos.append((x + 1, y + 1))

    return conexos

def conectividade_per_channel_4(image, x, y) :
    conexos = []
    rows = len(image)
    cols = len(image[0]) if rows > 0 else 0

    if x >= rows or y >= cols or x < 0 or y < 0 :
        print("Coordenadas fora do limite da imagem")
        return conexos

    if x + 1 < rows and (image[x + 1][y] >= image[x][y] - 10 and image[x + 1][y] <= image[x][y] + 10) :
        conexos.append((x + 1, y))

    if x - 1 >= 0 and (image[x - 1][y] >= image[x][y] - 10 and image[x - 1][y] <= image[x][y] + 10) :
        conexos.append((x - 1, y))

    if y + 1 < cols and (image[x][y + 1] >= image[x][y] - 10 and image[x][y + 1] <= image[x][y] + 10) :
        conexos.append((x, y + 1))

    if y - 1 >= 0 and (image[x][y - 1] >= image[x][y] - 10 and image[x][y - 1] <= image[x][y] + 10) :
        conexos.append((x, y - 1))

    return conexos

def conectividade_per_channel_8(image, x, y) :
    conexos = conectividade_per_channel_4(image, x, y)
    rows = len(image)
    cols = len(image[0]) if rows > 0 else 0

    if x >= rows or y >= cols or x < 0 or y < 0 :
        print("Coordenadas fora do limite da imagem")
        return conexos

    if x + 1 < rows and y + 1 < cols and (image[x + 1][y + 1] >= image[x][y] - 10 and image[x + 1][y] <= image[x][y] + 10) :
        conexos.append((x + 1, y + 1))

    if x + 1 < rows and y - 1 >= 0 and (image[x + 1][y - 1] >= image[x][y] - 10 and image[x + 1][y] <= image[x][y] + 10) :
        conexos.append((x + 1, y - 1))

    if x - 1 >= 0 and y - 1 >= 0 and (image[x - 1][y - 1] >= image[x][y] - 10 and image[x + 1][y] <= image[x][y] + 10) :
        conexos.append((x - 1, y - 1))

    if x - 1 >= 0 and y + 1 < cols and (image[x - 1][y + 1] >= image[x][y] - 10 and image[x + 1][y] <= image[x][y] + 10) :
        conexos.append((x - 1, y + 1))

    return conexos

def caminho(matrix, init, dest, rgb_image, c) :
    chegou = False # flag para indicar se chegou ao destino
    max_iteracoes = 100
    rows = len(matrix)
    cols = len(matrix[0])

    path = [init] # lista para armazenar o caminho percorrido

    for i in range(max_iteracoes) :
        if init == dest :
            chegou = True
            break
        x, y = init
        conexos = conectividade_8(matrix, x, y) if not rgb_image else conectividade_per_channel_8(matrix, x, y)
        if len(conexos) == 0 :
            print("Não há caminho possível")
            break

        dist = MAX_DIST
        for conexo in conexos :
            dist_conexo = abs(conexo[0] - dest[0]) + abs(conexo[1] - dest[1])
            # print(f"Conexo: {conexo} | Distância para o destino: {dist_conexo}")
            if dist_conexo < dist :
                dist = dist_conexo
                init = conexo
        # print(f"\nIteração {i + 1} | Caminho atual: {path} | Próximo passo: {init}\n")
        path.append(init)

    return path, chegou

def caminho_rgb(image, init, dest) :
    matrix_r = image[:, :, 0]
    matrix_g = image[:, :, 1]
    matrix_b = image[:, :, 2]
    
    caminho_r, chegou_r = caminho(matrix_r, init, dest, True, 0)
    print("Chegou ao destino no canal R: ", chegou_r)
    print("Caminho para o canal R: ", caminho_r)
    
    caminho_g, chegou_g = caminho(matrix_g, init, dest, True, 1)
    print("Chegou ao destino no canal G: ", chegou_g)
    print("Caminho para o canal G: ", caminho_g)

    caminho_b, chegou_b = caminho(matrix_b, init, dest, True, 2)
    print("Chegou ao destino no canal B: ", chegou_b)
    print("Caminho para o canal B: ", caminho_b)


    

if __name__ == "__main__":
    # path, chegou = caminho(matrix, init, dest, false, 0)
    # print("Chegou ao destino: ", chegou)
    # print("o path é : ", path)
    image = cv2.imread("img/rainbow.png")
    print("image shape: ", image.shape)
    caminho_rgb(image, init, dest)