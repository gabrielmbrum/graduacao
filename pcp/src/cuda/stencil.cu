#define BLOCK_SIZE 16
#define RADIUS 1

__global__ void stencil_1d(int *in, int *out) {
    __shared__ int temp[BLOCK_SIZE + 2 * RADIUS];
    int gindex = threadIdx.x + blockIdx.x * blockDim.x;
    int lindex = threadIdx.x + RADIUS;

    // read input elements into shared memory
    temp[lindex] = in[gindex];
    if (threadIdx.x < RADIUS) {
        temp[lindex - RADIUS] = in[gindex - RADIUS];
        temp[lindex + BLOCK_SIZE] = in[gindex + BLOCK_SIZE];
    }

    __syncthreads();

    // apply the stencil
    int result = 0;
    for (int offset = -RADIUS; offset <= RADIUS; offset++) 
        result += temp[lindex + offset];

    // store the result
    out[gindex] = result;
}