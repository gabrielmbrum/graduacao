
## Ferramentas
##### MPLAB X
IDE para desenvolvimento assembly

##### SimulIDE
simulador da eletrônica embarcada
é um simulador de circuitos

##### Proteus
outra ferramenta para simulação de circuitos
a UNESP não tem a licensa

##### Tinkercad
ferramenta online onde pode-se simular um circuito

---
## Arquitetura e Funcionamento de Microcontroladores

a camada ISA contém um conjunto de instruções e depende de dois fatores:
- RISC
- CISC

### arquiteturas de microcontroladores
1. hardware dedicado
	- plataformas embarcados
		- os sistemas embarcados são soluções de software e hardware projetados para tarefas específicas em tempo real
		- envolve aplicações críticas, que podem causar dano a pessoas, natureza e empresas caso falhem
		
	- microcontroladores
		- tem um único circuito integrado o qual contém um núcleo de processador, memória e periféricos programáveis de entrada e saída
		- arquitetura
			- CPU
			- memória
			- I/O
			- comunicação
		- arquitetura PIC16F877A -> arquitetura de Harvard
			- possui memórias separadas para instruções e dados
			- o microcontrolador pode acessar simultaneamente instruções e dados
		- arquitetura PIC16F877A
			- armazenar seus programas no mesmo espaço de memória que os dados
	
	- RISC x CISC
		- RISC 
			- arquietetura de tamanho reduzido com alto desemepnho, em que as intruções são executadas em um único ciclo de clock
			- os processadores RISC possuem um grande número de registradores de uso geral
			- tem uma arquitetura simples, facilitando a aimplementação e a depuração de hardware
		- CISC
			- arquitetura que possui um conjunto de instruções complexo e diversificado
			- as instruções realizam operações mais compelxas, reduzindo a quantidade de código para executar tarefas específicas
			- conjunto de instruções complexo, executando várias operações em uma única instrução -> reduz a quantidade de instruções necessárias
			- oferece diferentes formas de acessar a memória, dando maior flexibilidade para as operações
			- uso intenso de memória (realizam operações diretamente na memória)
		- diferenças principais
			- RISC usa intensivamente os registradores, já a CISC uso mais a memória principal
			- RISC são mais fácil de projetas, implementar e depurar em termos de hardware, já o CISC facilitam o software e requrerem um hardware mais sofisticado
			- ARM -> seguem o modelo RISC
			- Intel x86 -> utilizam CISC

### funcionamento básico de microcontroladores
1. elementos de software
	- conceitos básicos
		- bit, hexadecimal, byte, nible (meio byte)
		- registrador (conjunto de flip-flops - geralmente tipo D - que são interligados em paralelo) -> armazenam informação binária
		- memória (circuitos semicondutores, mídias magnéticas, mídias ópticas, PROM, ePROM, e2PROM, ...)
		- instrução (única ação) e programa (conjunto de instruções)
		- software e firmware (armazenado em memória não volátil - ROM/PROM/EPROM/Flash)
		- *shift register:* sequência de flip flops D
		- deslocamento serial -> paralelo OU paralelo -> serial


### código do semáforo e configurações bases
- CONFIG FOSC=XT
	- configura o tipo de oscilador utilizado
	- o XT indica que está sendo usado um cristal externo de baixa frequência de clock
	- o termo FOSC para configuração de microcontroladores PIC da Microchip
	
- CONFIG WDTE=OFF/ON
	- o Watchdog Timer é um contaador que reinicia o microcontrolador se o programa principal não estiver funcionando corretamente
	- é definido um tempo limite (pelo fabricante)
	- o programa "alimenta" o WDTE, se ele não o alimentar, ele reinicia o sistema
	
- CONFIG PWRTE=ON
	- power up timer
	- garante que o microcontrolador tenha tempo suficiente para se estabilizar após ser ligado
	
- CONFIG BOR=ON
	- brown-out reset
	- reinicia o microcontrolador se a tensão de alimentação cair abaixo de um nível seguro
	
- CONFIG LVP=ON
	- programação de baixa voltagem
	- permite a programação do microcontroaldor com uma tensão de alimentação menor
	
- CONFIG WRT=OFF/ON
	- proteçaõ de escrita
	- evita que o código do programa seja modificado após a programação (proteção do código contra alterações acidentais ou maliciosas)
	
- CONFIG CP=OFF
	- proteçaõ de código
	- impede que o código seja lido ou copiado do microcontrolador
	
- CONFIG CPD=OFF/ON
	- código de proteção de dados

```assembly

...
configs
...

#define _XTAL_FREQ 4000000

#define VERMELHO PORTB,2
#define AMARELO PORTB,1
#define VERDE PORTB,0
#define CHAVE PORTD,0

TEMPO1 EQU 0X20
TEMPO2 EQU 0X21
TEMPO3 EQU 0X22



```

