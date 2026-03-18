import cv2

matrix = [[1, 0, 0],
          [1, 1, 1],
          [0, 0, 1]]

MAX_DIST = 4

init = (0, 0)
dest = (2, 2)

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

def conectividade_per_channel(image, x, y, c) :
    conexos = []
    rows = len(image)
    cols = len(image[0]) if rows > 0 else 0

    if x >= rows or y >= cols or x < 0 or y < 0 :
        print("Coordenadas fora do limite da imagem")
        return conexos

    if x + 1 < rows and y + 1 < cols and (image[x + 1][y + 1][c] >= image[x][y][c] - 10 and image[x + 1][y][c] <= image[x][y][c] + 10) :
        conexos.append(image[x + 1][y + 1][c])

    if x + 1 < rows and y - 1 >= 0 and (image[x + 1][y - 1][c] >= image[x][y][c] - 10 and image[x + 1][y][c] <= image[x][y][c] + 10) :
        conexos.append(image)

    if x - 1 >= 0 and y - 1 >= 0 and (image[x - 1][y - 1][c] >= image[x][y][c] - 10 and image[x + 1][y][c] <= image[x][y][c] + 10) :
        conexos.append((x, y + 1))

    if x - 1 >= 0 and y + 1 < cols and (image[x - 1][y + 1][c] >= image[x][y][c] - 10 and image[x + 1][y][c] <= image[x][y][c] + 10) :
        conexos.append((x, y - 1))

    return conexos

def caminho(matrix, init, dest) :
    chegou = False # flag para indicar se chegou ao destino
    max_iteracoes = 10
    rows = len(matrix)
    cols = len(matrix[0])

    path = [init] # lista para armazenar o caminho percorrido

    for i in range(max_iteracoes) :
        if init == dest :
            chegou = True
            break
        x, y = init
        conexos = conectividade_8(matrix, x, y)
        if len(conexos) == 0 :
            print("Não há caminho possível")
            break

        dist = MAX_DIST
        for conexo in conexos :
            dist_conexo = abs(conexo[0] - dest[0]) + abs(conexo[1] - dest[1])
            print(f"Conexo: {conexo} | Distância para o destino: {dist_conexo}")
            if dist_conexo < dist :
                dist = dist_conexo
                init = conexo
        print(f"\nIteração {i + 1} | Caminho atual: {path} | Próximo passo: {init}\n")
        path.append(init)

    return path, chegou

def caminho_rgb(image, init, dest) :
    matrix_r = image[:, :, 0]
    matrix_g = image[:, :, 1]
    matrix_b = image[:, :, 2]

    conexos_r = conectividade_per_channel(matrix_r, init, dest)
    conexos_g = conectividade_per_channel(matrix_g, init, dest)
    conexos_b = conectividade_per_channel(matrix_b, init, dest)
    
    

if __name__ == "__main__":
    # path, chegou = caminho(matrix, init, dest)
    # print("Chegou ao destino: ", chegou)
    # print("o path é : ", path)
    image = cv2.imread("img/dlss.jpg")


        