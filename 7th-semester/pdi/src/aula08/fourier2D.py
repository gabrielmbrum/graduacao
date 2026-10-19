import cv2
import matplotlib.pyplot as plt 
import numpy as np

def dft_2d_4loops(image):
    """
    Calcula a Transformada Discreta de Fourier 2D de uma imagem em escala de cinza
    usando 4 loops 'for' aninhados, conforme a equação matemática clássica.
    
    Parâmetros:
    image (numpy.ndarray): Imagem de entrada 2D (escala de cinza).
    
    Retorna:
    numpy.ndarray: Matriz complexa representando a imagem no domínio da frequência.
    """
    # M é a altura (linhas), N é a largura (colunas)
    M, N = image.shape
    
    # Cria uma matriz de zeros complexos para armazenar o resultado X[u, v]
    dft_result = np.zeros((M, N), dtype=complex)
    
    # Constante para otimizar o cálculo dentro do loop
    pi_2j = -2j * np.pi
    
    # 1º e 2º loops: Iteram sobre as variáveis de frequência (u, v)
    for u in range(M):
        for v in range(N):
            
            soma_parcial = 0.0 + 0.0j
            
            # 3º e 4º loops: Iteram sobre as variáveis espaciais da imagem (m, n)
            for m in range(M):
                for n in range(N):
                    # Calcula o expoente: -j * 2π * ((u*m)/M + (v*n)/N)
                    expoente = pi_2j * ((u * m) / M + (v * n) / N)
                    
                    # Somatória de x[m,n] * e^(expoente)
                    soma_parcial += image[m, n] * np.exp(expoente)
            
            # Aplica o fator de escala 1 / (M * N) conforme a imagem
            dft_result[u, v] = soma_parcial / (M * N)
            
    return dft_result

def dft_2d_fft(image):
    """
    Calcula a Transformada Discreta de Fourier 2D de uma imagem usando 
    o algoritmo otimizado FFT do Numpy.
    
    Parâmetros:
    image (numpy.ndarray): Imagem de entrada 2D (escala de cinza).
    
    Retorna:
    numpy.ndarray: Matriz complexa representando a imagem no domínio da frequência.
    """
    M, N = image.shape
    
    # Executa a FFT 2D nativa e otimizada (escrita em C/Fortran)
    fft_result = np.fft.fft2(image)
    
    # Divide por (M * N) para bater exatamente com a convenção da sua fórmula matemática
    dft_result = fft_result / (M * N)
    
    return dft_result

# Carrega a imagem em escala de cinza (garanta que a imagem seja pequena para esse teste)
# Exemplo: uma imagem de 32x32 pixels
img = cv2.imread('imagem_cinza.png', cv2.IMREAD_GRAYSCALE)

# Redimensiona para um tamanho bem pequeno para evitar que demore horas
img_pequena = cv2.resize(img, (32, 32))

# Executa a nossa função
dft_customizada = dft_2d_4loops(img_pequena)

dft_fftzada = dft_2d_fft(img_pequena)

# O resultado é um número complexo. Para visualizar, calculamos a magnitude.
# Usamos np.log(1 + magnitude) para comprimir os valores e visualizar melhor
magnitude_espectro = np.log(1 + np.abs(dft_customizada))

# Mostra o resultado
plt.imshow(magnitude_espectro, cmap='gray')
plt.title('Espectro de Magnitude (DFT com 4 Loops)')
plt.show()