#include "stdio.h"
#include "stdlib.h" // Para exit()

/**
 * Macro para verificação de erros CUDA.
 * Ela checa o resultado da função 'err'. Se não for 'cudaSuccess',
 * imprime a mensagem de erro, arquivo e linha, e encerra o programa.
 */
#define CUDA_CHECK(err) __cudaCheckError(err, __FILE__, __LINE__)

inline void __cudaCheckError(cudaError_t err, const char *file, int line) {
    if (err != cudaSuccess) {
        fprintf(stderr, "ERRO CUDA: '%s' no arquivo %s, linha %d\n", cudaGetErrorString(err), file, line);
        exit(EXIT_FAILURE);
    }
}

// Kernel (sem mudanças)
__global__ void add(int *a, int *b, int *c) {
    *c = *a + *b;
}

int main(void) {
    int a, b;
    int c = 0; // Boa prática: inicialize a variável host
    int *d_a, *d_b, *d_c;
    int size = sizeof(int);

    // 1. Aloca memória na GPU (note o CUDA_CHECK)
    CUDA_CHECK(cudaMalloc((void **)&d_a, size));
    CUDA_CHECK(cudaMalloc((void **)&d_b, size));
    CUDA_CHECK(cudaMalloc((void **)&d_c, size));

    // 2. Define valores no Host
    a = 2;
    b = 7;

    // 3. Copia do Host para o Device (GPU)
    CUDA_CHECK(cudaMemcpy(d_a, &a, size, cudaMemcpyHostToDevice));
    CUDA_CHECK(cudaMemcpy(d_b, &b, size, cudaMemcpyHostToDevice));

    // 4. Lança o Kernel
    add<<<1, 1>>>(d_a, d_b, d_c);
    
    // Checa se o *lançamento* do kernel deu erro (ex: configuração inválida)
    CUDA_CHECK(cudaGetLastError());

    // 5. Sincroniza e espera a GPU terminar
    // Se o kernel travou (ex: acesso ilegal de memória), esta chamada vai reportar!
    CUDA_CHECK(cudaDeviceSynchronize());

    // 6. Copia o resultado do Device (GPU) para o Host
    CUDA_CHECK(cudaMemcpy(&c, d_c, size, cudaMemcpyDeviceToHost));

    // 7. Imprime o resultado
    printf("a = %d\nb = %d\nc = %d\n", a, b, c);

    // 8. Libera a memória da GPU
    CUDA_CHECK(cudaFree(d_a));
    CUDA_CHECK(cudaFree(d_b)); // Corrigido: use ponto e vírgula, não vírgula
    CUDA_CHECK(cudaFree(d_c));

    return 0;
}