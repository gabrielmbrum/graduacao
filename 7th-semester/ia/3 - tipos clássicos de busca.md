
### algoritmos de buscas em espaços de estados

>**def1.:** um algoritmo é COMPLETO se sempre encontra uam solução
>
>**def2.:** um algoritmo é ÓTIMO se garante encontrar a melhor solução segundo algum critério de custo

### busca cega
- não informada
- em largura
- em profundidade
	- profundidade limitada
	- aprofundamento iterativo

- **breadth-first search (BFS)**
	- passa em todos os nós da linha `L` antes de passar para `L+1`
	- é completa se o número de açoẽs é finito
	- ótima se as ações tem custo unitário
	- mantém todos os nós em memória

- **depth-frist search (DFS)**
	- desempilha apenas quando chega em um nó de $H_{max}$
	- utiliza de pilhas -> FILO
	- não é completa, pois o ramo pode ser infinito
	- não é ótima pois encontra a primeira solução (1° estado objetivo que aparecer) e não a de menor custo
	- só guarda nós do caminho atual, então é melhor no quesito memória

- **busca com profundidade limitada**
	- a ideia é definir um limite `L` na busca em profundidade
	- nós de profundidade L são considerados como terminais
	- evita o problema de ter ramos infinitos
	- pode ocorrer de descer até `L` e ignorar soluções que estavam além de `L` 

- **busca com profundidade iterativa**
	- a ideia é buscar em profundidade mas avançando de nível a nível
	- repete a busca em profundidade limitada, mas sempre considerando a cada ciclo do algoritmo valores de L cada vez maiores
	- combinação de busca de profundidade com busca em largura
	- ![[Pasted image 20260316153113.png]]
	- é completa se o número de ações for finito, então sempre vamos encontrar uma solução
	- se as ações tem custo unitário -> checa-se um nível da árvore por vez, então encontraremos a solução ótima
	- na memória, mantém apenas o caminho atual na memória a cada ciclo, já que todos os nós são sempre revisitados a cada avanço de L

### busca informada 
- faz uso do conhecimento específico do problema para encontrar soluções mais eficientes do que na busca cega
- abordagem geral: busca pela melhor escola
	- utiliza de função de avaliação dos nós
	- expande o nó com melhor avaliação
	- possibilita implementar diferentes estratégias de busca (pode-se variar a função de avaliação)
	
- ideia chave
	- uso de função de avaliação $f(n)$ que retorna uma estimativa do valor do nó *n*
	- expandir o nó mais desejável 
	
- em termos de implementação, teremos uma lsita ordenada dos nós de fronteira
	- busca gulosa
	- busca A*

### busca gulosa (heurística bb)
- $f(n) = h(n)$ 
- a heurística é uma estimativa do custo de *n* até um nó objetivo
- ideia
	- buscar pela melhor escolha, expandindo o nó que ""parece ser"" mais próximo ao nó objetivo, com base no cálculo de $h(n)$
- desvantagens
	- como o cálculo estimado é com base no estado atual, pode deixar de escolher um caminho que inicialmente é pior mas no futuro é melhor (custo total menor)
	- pode entrar em loops com falsos caminhos, exemplo:
	- ![[Pasted image 20260316160556.png]]
- não é completa
- não é ótima
- mantém todos os nós na memória

### busca A* 
- a ideia é evitar expandir caminhos caros
- $f(n) = g(n) + h(n)$
	- $g(n)$: custo real para alcançar *n*
	- $h(n)$: custo heurístico
- é completa
- é ótima (caso tenha heurística admissível)
- mantém todos os nós na memória
- não existe algoritmo que garanta expandir menos nós do que A*

>**def.:** heurística admissível nunca superestima o custo de alcançar o objetivo (é otimista)

