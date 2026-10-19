tema de seminario: percepção visual e princípios de Gestalt no design de interfaces
dia 15/12

15 a 25 min por pessoa 

pode ser slides, implementação e oq quiser

---

## psicologia experimental
- lei de hick-hyman: relaciona a quantidade de alternativas ao tempo de escolha
- lei de fitts: relaciona o tamanho e a distância do alvo para acertar o alvo

## lei de Hick-Hyman

$T = k * log_2(N + 1)$, onde N é o número de alternativas e k é uma constante empírica

$T = k * \sum p_i log_2(1 + 1/p_i)$ é a probabilidade da alternativa i 

a primeira formula é utilizada quando estamos buscando em dados ordenados, já a segunda é com dados desodernados

## lei de Fitts

o tempo de apojntar depende da distância D até o alvo e de sua largura S na direção do movimento

uma formulação é $T = k x log_2(D/S + 0,5)$, onde k é uma constante empírica também

aumentar a área clicável facilita alcançar o botão

o menu circular mantém as opções próximas e equidistantes do ponto de abertura

## psicologia cognitiva aplicada 

é o mapamento dos nossos sistemas perceptivos, cognitivos e motores para uma interface efetiva para nossos sitemas de processamento humanos

faz um mapeamento arquitetural do funcionamento do nosso cérebro

nossa memória de trabalho (curta) tem de 5 a 9 chunks (unidades significativas de memórias), então ao desenvolver algo é melhor limitar que para cada resoluçaõ de problema esteja entre esse intervalo de chunks

## engenharia cognitiva

exemplo da torneira de água fria e quente

da pra ter duas torneiras uma cada, ou uma unica que vai pra direita/esquerda (quente/frio) e cima/baixo (controle de fluxo)

## teoria da ação x teoria da atividade

ação (Norman, 1991) 
- golfo de execução: dificuldade de descobrir e realizar as ações necessárias para alcançar um objetivo
- golfo de avanço: dificuldade de perceber o estado do sistema, interpretá-lo e verificar se o objetivo foi alcançado

atividade
- a atividade tem um motivo e se dirige a um objeto. ações conscientes buscam objetivos, e operações realizam essas ações nas condições existentes
- nao forma um fluxo como a teoria da ação, forma uma piramidade com seis partes: instrumento, sujeito e objeto, regras e comunidade e divisão do trabalho
- os princípios são mediação, orientação a objetos e perturbação

## exercício

### enunciado

escolha uma tarefa em interface conhecida e descreva os 6 estágios da teoria da ação. identifique dificuldades de exececução e uma de avaliação e proponha mudanças para cada uma. explique como a mudança aproxima os controles/resultados dos objetivos do usuário.

inteção, especificação da acao e execução (execução)
avaliação, interpretaçaõ e percepção (avaliação)

### resposta

interface é o APEX legend

intenção: sinalizar defesa de área
espec. da ação: abrir apex, achar partida, na partida vou segurar R1 e então na roda de ações que aparecer escolho a sinalização de defesa
execução: soltar R1 com R3 sobre a sinalização de defesa

percepção: para você e seus aliados, aparece um pin no mapa mostrando a área que precisa de defesa e um áudio avisa que precisa de defesa
interpretação: sinalizei a área a ser defendida
avaliação: conclui minha ação


dificuldades de execução: precisa controlar movimento, prestar atenção ao redor e ainda fazer todos esses comandos ao mesmo tempo
dificudades de percepção: concorrencia de ping, com spams de pings de outros aliados e voce nao saber se é seu ping ou nao

mudanca para execução: comando de voz
mudança de percepção: limitar pings por área (nao poder repetidos em mesma areas)

## exercício 2

### enunciado

escolha uma atividade coletiva e identifique sujeito, objeto, instrumentos, comunidade, regras e divisão de trabalho
- descreva uma contradição ou perturbação e proponha uma mudança no sistema ou na organização da atividade
- explique como essa mudança afeta o trabalho das outras pessoas envolvidas

### resposta

MINECRAFT

instrumento: minecraft
sujeito: players
objeto: construir uma casa
comunidade: outros players
regras: não pode pegar item no criativo, não pode usar cheat e não pode quebrar o bloco do amiguinho 
divisão do trabalho: coletar os blocos, um processa na crafting table e outro constrói

contradição: a regra para evitar perturbação (bloquear a quebra de blocos do amiguinho) gera a perturbação do amiguinho poder me prender ao redor de blocos

a mudança é que caso seja percebido que a pessoa está presa, permita quebrar os blocos

afetaria o trabalho das pessoas envolvidas ao ter que fazer um algoritmo para perceber essta contradição e permitir a quebra da regra contraditória
