#include <stdio.h>
#include <pthread.h> /* linhas padrão */
#include <semaphore.h>
#include <unistd.h>
#include <stdlib.h>
#define SHARED 1

void *Producer(void *);
void *Consumer(void *);

sem_t empty, full; /* semáforos globais */
int data = 0;          /* buffer compartilhado */
int numIters;

/* main lê linha de comando criando os threads*/
int main(int argc, char *argv[])
{

  pthread_t producer_id, consumer_id;  /* id dos threads */
  pthread_attr_t attr; /* atributos comuns */
  pthread_attr_init(&attr);
  pthread_attr_setscope(&attr, PTHREAD_SCOPE_SYSTEM);

  sem_init(&empty, SHARED, 1); /* sem empty = 1 */
  sem_init(&full, SHARED, 0);  /* sem full = 0 */

  numIters = atoi(argv[1]); // número de iterações que é passado como argumento no executável
  pthread_create(&producer_id, &attr, Producer, NULL);
  pthread_create(&consumer_id, &attr, Consumer, NULL);
  pthread_join(producer_id, NULL);
  pthread_join(consumer_id, NULL);
}

void *Producer(void *arg)
{
  int produced;

  for (produced = 1; produced <= numIters; produced++)
  {
    printf("wants to produce %d...\n", produced);
    sem_wait(&empty);
    printf("producing %d\n", produced);
    sleep(5); // Simula o tempo de produção
    data++;
    printf("produced %d\n", data);
    sem_post(&full);
  }
}

void *Consumer(void *arg)
{
  int consumed;

  for (consumed = 1; consumed <= numIters; consumed++)
  {
    printf("wants to consume %d...\n", consumed);
    sem_wait(&full);
    printf("consuming %d\n", consumed);
    sleep(1); // Simula o tempo de consumo
    printf("consumed %d\n", data);
    sem_post(&empty);
  }
}