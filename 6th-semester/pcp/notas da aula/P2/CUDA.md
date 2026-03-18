
#CUDAisLIFE #MakeAmericaGreatAgain #SurfNaked

criada para programação em GPU da Nvidia

já é ótimizada para tais placas de vídeo, tanto que um código mediano em CUDA tem desempenho semalhante a um código excelente em OpenCL (estando em uma paca da nvidia)

**arquitetura**
- expoe paralelismo da GPU para computação de propósito geral

**CUDA C/C++**
- baseado no padrão C/C++
- pequeno conjunto de extensões para habilitar programação heterogênea (código parcialmente executado na CPU e parcialmente na GPU)
- APIs direcionadas para gerenciar dispositivos, memória

### hello world
**hello world - versão C (mitinho)**
```c
int main (void) {
	printf("Hello World!\n");
	return 0;
}
```

```bash
$ nvcc
hello_world.cu
$ a.out
hello world!
```

**hello world - versão CUDA IS LIFE**
```c
__global__ void mykernel (void) {
}

int main (void) {
	mykernel<<<1,1>>>();
	printf("hello world!\n");
	return 0;	
}
```

keywords
- `__global__` : indica uma função que executara na GPU
- `nvcc`: separa o src entre host e dispositivo (host é GPU e dispositivo é GPU)
- `mykernel<<<1,1>>>()`: os < e > triplos marcam uma chamada do código host para um código device, por hora retornaremos para os parametros (1,1)

### soma de matrizes

**cuidados com a memória**
- ponteiros de dispositivos
	- apontas para memória de GPU
	- nao podem ser referenciados no código do *host*
	- pode-se passar o conteúdo dele (por meio de chamada de funções)

- ponteiros de host
	- apontam para memória de CPU
	- nao podem ser referenciados no código do *device*
	- pode-se passar o conteúdo dele (por meio de chamada de funções)


```c
// add() roda na GPU, então estes ponteiros precisam ser de la
__global__ void add (int *A, int *B, int *C) {
	*C = *A + *B;
}

int main (void) {
	int a, b, c;
	int *d_a, *d_b, *d_c;
	
	cudaMalloc((void **) &d_a, size);
	cudaMalloc((void **) &d_b, size);
	cudaMalloc((void **) &d_c, size);
	
	a = 2;
	b = 7;
	
	cudaMemcpy(d_a, &a, size, cudaMemcpyHostToDevice);
	cudaMemcpy(d_b, &b, size, cudaMemcpyHostToDevice);
	
	add<<<1,1>>>(d_a, d_b, d_c);
	
	cudaMemcpy(&c, d_c, size, cudaMemcpyDeviceToHost);
	
	cudaFree(d_a); cudaFree(d_b); cudaFree(d_c);
	return 0; 
}
```

mesmo assim, ta uma merda, não ta executando em paralelo

### a porra da paralelização surge (e urge)

`add<<<1,1>>>` -> `add<<<N,1>>>`

cada chamada de add() é referenciada como um *block*, um conjunto de *blocks* é um *set*, cada chamada pode ser referenciada pelo índice do bloco usando *blockIdx.x*

```c
__global__ void add(int *a, int *b, int *c) {
	c[blockIdx.x] = a[blockIdx.x] + b[blockIdx.x]
}

int main (void) {
	int a, b, c;
	int *d_a, *d_b, *d_c;
	int size = N * sizeof(int);
	
	cudaMalloc((void **) &d_a, size);
	cudaMalloc((void **) &d_b, size);
	cudaMalloc((void **) &d_c, size);
	
	a = (int *) malloc(size); random_ints(a, N);
	b = (int *) malloc(size); random_ints(b, N);
	c = (int *) malloc(size); 
	
	cudaMemcpy(d_a, &a, size, cudaMemcpyHostToDevice);
	cudaMemcpy(d_b, &b, size, cudaMemcpyHostToDevice);
	
	add<<<N,1>>>(d_a, d_b, d_c);
	
	cudaMemcpy(&c, d_c, size, cudaMemcpyDeviceToHost);
	
	free(a); free(b); free(c);
	cudaFree(d_a); cudaFree(d_b); cudaFree(d_c);
	return 0; 
}
```

### block x threads

![[Pasted image 20251113152918.png]]

>`int index = threadIdx.x + (blockIdx.x * blockDim.x)`

![[Pasted image 20251113153126.png]]

<<<x,y>>>
x -> quantidade de blocos (N posições totais/quantidade de threads por bloco)
y -> quantidade de threads por bloco

### stencil

>cooperação entre threads de um bloco

conceitos fundamentais
1. `__shared__` 
2. `__syncthreads()` 

problema do stencil
- calcular um novo vetor onde cada elemento é a soma dos seus vizinhos no vetor original
- exemplo com raio 3
	- a posição 10 é a as posições 7 + 8 + 9 + 10 + 11  + 12 + 13

- problema de perfomance
	- a primeira ideia é fazer com que cada thread cuide de um elemento de saída
	- isto é ineficiente por conta de se basear na memória global da GPU
	- o mesmo espaço de memória é lido varias vezes, causando desperdício de performance
	
- primeira solução - `__shared__`
	- cada bloco de threads será responsável por um pedaço do vetor de saída
	- as threads carregam cooperativamente o pedaço que precisam
	- depois que tudo estiver na memoria shared cada thread faz seu cálculo
	- cada valor de input é lido da memória lenta apenas uma vez
	- porem gera um problema de condição de corrida
- race condition
	- uma thread termina de carregar antes de outra e começa o processamento
- barreira de sincronismo - `__syncthreads()`

### coordenando host & device

CPU precisa sincronizar antes de consumir os resultados
- `cudaMemcpy()` -> bloqueia a CPU até que a copia é completada
- `cudaMemcpyAsync()` -> a cópia começa quando todas as chamadas precedentes do CUDA foram finalizadas assincronmanete, não bloquei a CPU
- `cudaDeviceSynchronize()` -> bloqueia a CPU até que as chamadas de CUDA sejam finalizadas

### erros

todas as chamadas para a API do cuda retorna um código de erro (`cudaError_t`)

`cudaError_t cudaGetLastError(void)`-> pega o código de erro do último erro
`char *cudaGetErrorString(cudaError_t)` -> pega a string para descrever o erro

### gerenciamento do dispositivo

aplicações podem consultar e selecionar GPUs
- `cudaGetDeviceCount(int *count)`
- `cudaSetDevice(int device)`
- `cudaGetDevice(int *device)`
- `cudaGetDeviceProperties(cudaDeviceProp *prop, int device)`

múltiplas threads podem compartilhar um dispositivo

uma única thread pode gerenciar vários dispositivos
- `cudaSetDevice(i)`
- `cudaMemcpy()`
