#include <omp.h>
#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]) {
    int nthreads, tid;
    omp_set_num_threads(4);

    #pragma omp parallel private(nthreads, tid)
    {
        tid = omp_get_thread_num();
        printf("Thread %d: Hello, World!\n", tid);

        #pragma omp master
        {
            nthreads = omp_get_num_threads();
            printf("Number of threads = %d\n", nthreads);   
        }
        
    }
}