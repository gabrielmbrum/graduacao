#include "stdio.h"
#include "stdlib.h" // Para exit()
#include "time.h"

#define N 12

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
    c[threadIdx.x] = a[threadIdx.x] + b[threadIdx.x];
}

int main(void) {
    int *a, *b, *c;
    int *d_a, *d_b, *d_c;
    int size = sizeof(int) * N;

    CUDA_CHECK(cudaMalloc((void **)&d_a, size));
    CUDA_CHECK(cudaMalloc((void **)&d_b, size));
    CUDA_CHECK(cudaMalloc((void **)&d_c, size));




    a = (int *) malloc(size);
    b = (int *) malloc(size);
    c = (int *) malloc(size);

    /* Inicializa o gerador pseudo-aleatório do C */
    srand((unsigned) time(NULL));

    for (int i = 0; i < N; i++) {
        a[i] = rand() % 100;
        b[i] = rand() % 100;
    }

    CUDA_CHECK(cudaMemcpy(d_a, a, size, cudaMemcpyHostToDevice));
    CUDA_CHECK(cudaMemcpy(d_b, b, size, cudaMemcpyHostToDevice));

    add<<<1, N>>>(d_a, d_b, d_c);
    
    // Checa se o *lançamento* do kernel deu erro (ex: configuração inválida)
    CUDA_CHECK(cudaGetLastError());

    // 5. Sincroniza e espera a GPU terminar
    CUDA_CHECK(cudaDeviceSynchronize());

    // 6. Copia o resultado do Device (GPU) para o Host
    CUDA_CHECK(cudaMemcpy(c, d_c, size, cudaMemcpyDeviceToHost));

    // 7. Imprime os arrays e resultados
    for (int i = 0; i < N; i++) {
        printf("%d + %d = %d\n", a[i], b[i], c[i]);
    }

    // 8. Libera a memória
    free(a);
    free(b);
    free(c);

    CUDA_CHECK(cudaFree(d_a));
    CUDA_CHECK(cudaFree(d_b)); // Corrigido: use ponto e vírgula, não vírgula
    CUDA_CHECK(cudaFree(d_c));

    return 0;
}