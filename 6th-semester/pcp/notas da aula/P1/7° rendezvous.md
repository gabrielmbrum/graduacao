
![[rendezvout1.png]]


processo remoto realiza chamadas para o servidor
o servidor está rodando, em certo ponto, fica aberto para receber pedidos, atende o que chegar e continua sua execução

### sintaxe

**lado do cliente**

```
call mname.opname(params);
```

**lado do servidor**
```
- definição das operações exportadas
	op opname (tipos dos parametros)
	
- no ponto de rendezvous
	in 
		  opname (id param) -> S; //em que S é uma sequência de comandos 
	ni 
```

o ponto de rendezvous pode envolver várias operações e também condições de escalonamneto, como em:
```
in 
	op1 (formals1) and B1 by e1 -> S1;
	[]...
	[] opN (formalsN) and Bn by eN -> SN;
ni
```
 

### exemplos

>problema dos filósofos famintos e burros
```
process Philosopher [i = 0 to 4]
{
	while (true)
	{
		call getforks(i);
		eat();
		call relforks(i);
		think();
	}
}

module Table
	op getforks(int), relforks(int);
body
	process Waiter
	{
		bool eating[5] ([5] false);
		while (true)
		{
			in 
				getforks(i) 
					and eating[right(i)]==false 
					and eating[left(i)]==false -> eating[i]==true
				
				[] relforks(i) -> eating[i]=false;
			ni
		}
	}
end Table
```

>servidor de relógio
```

```