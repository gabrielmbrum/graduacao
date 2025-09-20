

uso de **threads não é viável** para interação entre processos quanto o **paralelismo** ocorrer usando **sistemas multicomputadores**

utiliza-se uma interação no modelo cliente-servidor

a troca de mensagem é feita em cima dos protocolos TCP/UDP, usando bibliotecas como SOCKETS e NSL

a **comunicação** ocorre por meio da criação de **sockets**, **condicionada** à existência de um processo **servidor**

```
/*
	format - system/internet
	type - circuito virtual/datagrama
	protocol - TCP/UDP
*/
sd = socket (format, type, protocol);

// associa endereço de um host
host = gethostbyname(host_identification)
```

estrutura de dados de um socket:
```
struct sockaddr_in {
	sa_family_t sin_family;  // address family: AF_INET
	in_port_t sin_port;      // port in network byte order
	struct in_addr sin_addr; // internet address
};

// internet address
struct in_addr{
	uint32_t s_addr;         // adress in network byte order
}
```

**do lado do servidor:**
```
bind (sd, addres, lenght); //associa o endereço do servidor ao descritor sd

listen (sd, qlength); // aguarda uma requisição em sd (máximo de qlength)

nds = accept(sd, address, addrlen); //aceita uma conexão que será tratada no socket nsd
/*
	cria outro socket, para atender o cliente
/*
```

**do lado do cliente:**
```
getaddrinfo(node, service, hint, res) // coleta endereços do domínio node a partir de um service, armazenando resultados em res

connect(sd, address, length) //requisita a conexão com o servidor em address
```

**trocando mensagens:**
```
// sd -> socket por onde irá trocar mensagem
// msg -> bytes que irá mandar
// flags -> indicação de erros
count = send (sd, msg, length, flags);

// buf -> endereço do buffer que irei receber os dados
count = recv (sd, buf, length, flags);
```

outras alternativas:
- uso de datagramas com sendto() e recvfrom() 
- uso de read() e write(), caso já esteja com a conexão estabelecida

```
shutdown(sd, node); // fecha uma conexão, mas o sd continua ativo

close(); // fecha (destrói) um socket

getsocokname(sd, name, length); // pega o nome do socket que foi ligado pelo bind

getsockopt(sock, level, opt, opval, len); // recupera os valroes de opções de comunicação de sock operando no nível dado

setsockopt(sock, level, opt, opval, len); // pegar no classroom
```

**exemplo cliente/servidor**
com o uso de sockets, um sistema cliente/servidor deve ser composto por um par de programas

o servidor fica em um loop de espera

#### servidor
```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <arpa/inet.h>

int main (int argc, char *argv[])
{
	int sock, connected, bytes_recv, true = 1, i, j;
	
	char send_data[1024, recv_data[1024];
	struct sockaddr_int server_addr, client_addr;
	int sin_size;
	
	// cria socket e verifica se foi bem suciedo na operação
	if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
		perror("Erro na criaçao do socket");
		exit(1);
	}
	
	// ajusta opções para os ocket criado
	if (setsockopt(sock, SOL_SOCKET, SO_REUSERADDR, &true, sizeof(int)) == -1) {
		perror("Erro em setsockopt");
		exit(1);
	}
	
	// inicializa os parametros para o socket (endereço da porta 5000)
	server_addr,sin_family = AF_INET;
	server_addr,sin_port = htons(5000); //host-endian to network-endian
	server_addr.sin_addr.s_addr = INADDR_ANY;
	bzero(&(server_addr.sin_zero), 8);
	
	if(bind(sock, (struct sockaddr *)&server_addr, sizeof(struct sockaddr)) == -1) 
	{
		perror("binding não foi possível");
		exit(1);
	}
	
	if (listen, 5) == -1)	
	
	....

}

while (true) {
	sin_size = sizeof(struct sockaddr_in);
	
	conencted - accept(sock, (struct sockaddr*) & cliente_addr, &sin_size);
	
	printf("conexão recebida (CLiente: %s, POrta: %d)", inet_ntoa(cliente_addr.sin_addr), ntohs(cliente_addr.sin_port))
	
	fflush();
	
	// este laço é executado para todas conexões
	while (still_talking) {
		// recebe a solicitaçaõ
		if ((bytes_recv = recv(connected, recv_data, 1024, 0) <= 0)) {
			printf("conexão perdida");
			break;
		}
	
	
		recv_Data[bytes_recv] = '\0';
		
		// copia a entrada para a futura saída
		j = strlen(recv_data) - 2;
		for (i = 0; i <= j; i++)
			send_data[i] = recv_data[j-i];
		send_data[i] = '\0';
	}
	
	if (receive == 'q') {
		send_data = "encerrando conexão"
		envia mensagem
		printa 'conexão encerrada pelo cliente'
		fecha conexão
		break;
	} else
		send(connected, send_data, strlen(send_data),0);
	fflush(stdout);
	

	close(sock);	
}
```

#### cliente
