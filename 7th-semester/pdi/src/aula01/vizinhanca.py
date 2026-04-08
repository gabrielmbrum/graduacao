import cv2

matrix = [[1, 2, 3],
          [4, 5, 6]]

def vizinhanca_4(x, y) :
    vizinhos = []
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    if x >= rows or y >= cols or x < 0 or y < 0 :
        print("Coordenadas fora do limite da matriz")
        return vizinhos

    if x + 1 < rows :
        vizinhos.append(matrix[x + 1][y])
    if x - 1 >= 0 :
        vizinhos.append(matrix[x - 1][y])
    if y + 1 < cols :
        vizinhos.append(matrix[x][y + 1])
    if y - 1 >= 0 :
        vizinhos.append(matrix[x][y - 1])

    return vizinhos

def vizinhanca_8(x, y) :
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    if x >= rows or y >= cols or x < 0 or y < 0 :
        print("Coordenadas fora do limite da matriz")
        return []
    
    vizinhos = vizinhanca_4(x, y)
    if x - 1 >= 0 and y - 1 >= 0 :
        vizinhos.append(matrix[x - 1][y - 1])
    if x - 1 >= 0 and y + 1 < cols :
        vizinhos.append(matrix[x - 1][y + 1])
    if x + 1 < rows and y - 1 >= 0 :
        vizinhos.append(matrix[x + 1][y - 1])
    if x + 1 < rows and y + 1 < cols :
        vizinhos.append(matrix[x + 1][y + 1])

    return vizinhos

def img_vizinhanca_4(image, x, y) :
    vizinhos = []
    rows = len(image)
    cols = len(image[0]) if rows > 0 else 0

    if x >= rows or y >= cols or x < 0 or y < 0 :
        print("Coordenadas fora do limite da imagem")
        return vizinhos

    if x + 1 < rows :
        vizinhos.append(image[x + 1][y])
    if x - 1 >= 0 :
        vizinhos.append(image[x - 1][y])
    if y + 1 < cols :
        vizinhos.append(image[x][y + 1])
    if y - 1 >= 0 :
        vizinhos.append(image[x][y - 1])

    return vizinhos

def img_vizinhanca_8(image, x, y) :
    rows = len(image)
    cols = len(image[0]) if rows > 0 else 0
    
    if x >= rows or y >= cols or x < 0 or y < 0 :
        print("Coordenadas fora do limite da imagem")
        return []
    
    vizinhos = img_vizinhanca_4(image, x, y)
    if x - 1 >= 0 and y - 1 >= 0 :
        vizinhos.append(image[x - 1][y - 1])
    if x - 1 >= 0 and y + 1 < cols :
        vizinhos.append(image[x - 1][y + 1])
    if x + 1 < rows and y - 1 >= 0 :
        vizinhos.append(image[x + 1][y - 1])
    if x + 1 < rows and y + 1 < cols :
        vizinhos.append(image[x + 1][y + 1])

    return vizinhos

def img_vizinhanca_4_rgb(image, x, y, c) :
    vizinhos = []
    rows = len(image)
    cols = len(image[0]) if rows > 0 else 0

    if x >= rows or y >= cols or x < 0 or y < 0 :
        print("Coordenadas fora do limite da imagem")
        return vizinhos

    if x + 1 < rows :
        vizinhos.append(image[x + 1][y][c])
    if x - 1 >= 0 :
        vizinhos.append(image[x - 1][y][c])
    if y + 1 < cols :
        vizinhos.append(image[x][y + 1][c])
    if y - 1 >= 0 :
        vizinhos.append(image[x][y - 1][c])

    return vizinhos

def img_vizinhanca_8_rgb(image, x, y, c) :
    rows = len(image)
    cols = len(image[0]) if rows > 0 else 0
    
    if x >= rows or y >= cols or x < 0 or y < 0 :
        print("Coordenadas fora do limite da imagem")
        return []
    
    vizinhos = img_vizinhance_4_rgb(image, x, y, c)
    if x - 1 >= 0 and y - 1 >= 0 :
        vizinhos.append(image[x - 1][y - 1][c])
    if x - 1 >= 0 and y + 1 < cols :
        vizinhos.append(image[x - 1][y + 1][c])
    if x + 1 < rows and y - 1 >= 0 :
        vizinhos.append(image[x + 1][y - 1][c])
    if x + 1 < rows and y + 1 < cols :
        vizinhos.append(image[x + 1][y + 1][c])

    return vizinhos

if __name__ == "__main__":
    print("vizinhanca de 4: ")
    print(vizinhanca_4(1, 1))

    print("vizinhanca de 8: ")
    print(vizinhanca_8(1, 1))
    
    path_file = 'img/dlss.jpg'
    image = cv2.imread(path_file)
    print("vizinhanca de 4 da imagem: ")
    vizinhanca_4 = img_vizinhanca_4_rgb(image, 100, 100, 0).append(img_vizinhanca_4_rgb(image, 100, 100, 1)).append(img_vizinhanca_4_rgb(image, 100, 100, 2))

    print("vizinhanca de 8 da imagem: ")
    print(img_vizinhanca_8_rgb(image, 1000, 1000,0).append(img_vizinhanca_8_rgb(image, 1000, 1000,1)).append(img_vizinhanca_8_rgb(image, 1000, 1000,2)))
