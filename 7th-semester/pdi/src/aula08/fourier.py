import numpy as np
import matplotlib.pyplot as plt

x = [2, 3, 4, 4]

x = np.fft.fft(x)

magnitudes = np.abs(x)

freqs = np.arange(len(x))/len(x)

plt.stem(freqs, magnitudes)
plt.xlabel('Frequência Normalizada')
plt.ylabel('Magnitude')
plt.title('Gráfico da DFT')

plt.savefig('dft.png')

x = [2, 3, 4, 4]

magnitudes = np.abs(x)

freqs = np.arange(len(x))/len(x)

plt.stem(freqs, magnitudes)
plt.xlabel('Frequência Normalizada')
plt.ylabel('Magnitude')
plt.title('Gráfico da DFT')

plt.savefig('original.png')