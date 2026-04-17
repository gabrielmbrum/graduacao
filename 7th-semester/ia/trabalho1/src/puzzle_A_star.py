import heapq
import random
import time

"""
    puzzle problem
    - the puzzle has 9 positions, with 8 pieces and one empty space
    - the goal is to move the pieces around until they are equal to [0, 1, 2, 3, 4, 5, 6, 7, 8], where 0 represents the empty space
    - the pieces can be moved up, down, left, or right, but only if the empty space is in the correct position to allow the move 
    
    initial random state

    f(n) = g(n) + h(n)
    -> g(n) = cost from start to n
    -> h(n) = heuristic cost from n to goal

    heuristic 1: number of pieces out of place

    heristic 2: sum of the distances of the pieces from their goal positions (manhattan distance)

    use heapq to manage the edge (priority queue) -> this garantee that the node with the lowest f(n) is expanded first

    use a set, or dict, to keep track of visited states to avoid redundant work

    search
    1 - catch the first node from the priority queue, expand it
    2 - checks if it's the goal
    3 - if not, check if it's already visited, if not, add it to the visited set and add its neighbors to the priority queue with their f(n) values

    ```pseudocode
       
        função BUSCA-DE-CUSTO-UNIFORME(problema) retorna uma solução ou falha
            nó ← um nó com ESTADO = problema.ESTADO-INICIAL, CUSTO-DE-CAMINHO = 0
            borda ← fila de prioridade ordenada pelo CUSTO-DE-CAMINHO, com nó como elemento único
            explorado ← um conjunto vazio
            repita
                se VAZIO?(borda), então retornar falha
                nó ← POP(borda) 
                se problema.TESTE-OBJETIVO(nó.ESTADO) então retornar SOLUÇÃO(nó)

                adicionar (nó.ESTADO) para explorado
                para cada ação em problema. AÇÕES(nó.ESTADO) faça
                    filho ← NÓ-FILHO (problema, nó, ação)
                    se (filho.ESTADO) não está na borda ou explorado então
                        borda ← INSIRA (filho, borda)   
                    senão se (filho.ESTADO) está na borda com o maior CUSTO-DE-CAMINHO então
                        substituir aquele nó borda por filho
    
    ```

    tests
    - create 10 instances with crescent difficulty, increasing the deepness of the solution (number of moves to solve the puzzle)
        - to do this, start from the goal state and make random moves to create the initial state
    
    - for each pair heuristic-difficulty, run at least 100 times calculating the time taken to solve the puzzle and the number of nodes expanded, and calculate the average time and number of nodes expanded for each difficulty level
        - with this info, its possibile to calculate the "fator de ramificação efetivo" (effective branching factor) for each heuristic and difficulty level, which is a measure of how well the heuristic is guiding the search process, the formula
            N + 1 = 1 + b* + b* x 2 + ... + b* x d

        - where N is total number of nodes expanded, b* is the effective branching factor, and d is the depth of the solution

    - after all the test, compares the reuslts of the two heuristics, showing the search cost and b* for each difficulty level
"""

goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

max_difficulty = 21
max_tests_per_difficulty = 100

class PuzzleState:
    def __init__(self, state, g=0, heuristic_func=1):
        self.state = state
        self.g = g
        self.heuristic_func = heuristic_func # Armazena qual usar
        self.h = self.heuristic() if heuristic_func == 1 else self.manhattan_distance()
        self.f = self.g + self.h

    def heuristic(self):
        # heuristic 1: number of pieces out of place
        return sum(1 for i in range(9) if self.state[i] != goal[i])
    
    def manhattan_distance(self):
        # heuristic 2: sum of the distances of the pieces from their
        # goal positions (manhattan distance)
        distance = 0
        for i in range(9):
            if self.state[i] != 0: # ignore the empty space
                current_row, current_col = divmod(i, 3)
                goal_row, goal_col = divmod(self.state[i], 3)
                distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance

    def get_children(self):
        children = []
        zero_index = self.state.index(0)
        row, col = divmod(zero_index, 3)

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_zero_index = new_row * 3 + new_col
                new_state = self.state[:]
                new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
                
                children.append(PuzzleState(new_state, self.g + 1, self.heuristic_func))
        return children
    
    def __eq__(self, other):
        return self.state == other.state
    
    def __lt__(self, other):
        return self.f < other.f
    
def a_star_search(initial_state):
    start_time = time.time()
    initial_node = PuzzleState(initial_state, heuristic_func=2) 
    frontier = []
    heapq.heappush(frontier, initial_node)
    explored = set()
    
    nodes_generated = 1 

    while frontier:
        current_node = heapq.heappop(frontier)

        if current_node.state == goal:
            end_time = time.time()
            return end_time - start_time, nodes_generated
        
        explored.add(tuple(current_node.state))

        children = current_node.get_children()
        
        nodes_generated += len(children) 
        
        children.sort(key=lambda x: x.f)

        for child in children:
            if tuple(child.state) not in explored and child not in frontier:
                heapq.heappush(frontier, child)
            elif child in frontier:
                index = frontier.index(child)
                if child.f < frontier[index].f:
                    frontier[index] = child
                    heapq.heapify(frontier)

    end_time = time.time()
    return end_time - start_time, nodes_generated

def generate_random_state(moves=10):
    state = goal[:]
    for _ in range(moves):
        zero_index = state.index(0)
        row, col = divmod(zero_index, 3)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dr, dc = random.choice(moves)
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero_index = new_row * 3 + new_col
            state[zero_index], state[new_zero_index] = state[new_zero_index], state[zero_index]
    return state

def calcular_b_star(N, d, erro=0.0001):
    if d == 0: return 1.0
    if N == 0: return 0.0
    
    low, high = 1.0, float(N)
    while high - low > erro:
        mid = (low + high) / 2.0
        # Soma da PG: (mid^(d+1) - 1) / (mid - 1)
        soma = (mid**(d + 1) - 1) / (mid - 1) if mid != 1.0 else d + 1
        
        if soma > N + 1:
            high = mid
        else:
            low = mid
    return (low + high) / 2.0

if __name__ == "__main__":
    for difficulty in range(2, max_difficulty, 2):
        total_time = 0
        total_nodes = 0
        for _ in range(max_tests_per_difficulty):
            initial_state = generate_random_state(difficulty)
            # print("Initial State:", initial_state)
            time_taken, nodes_generated = a_star_search(initial_state)
            total_time += time_taken
            total_nodes += nodes_generated
        
        avg_time = total_time / max_tests_per_difficulty
        avg_nodes = total_nodes / max_tests_per_difficulty

        print(f"Difficulty: {difficulty}, Average Time: {avg_time:.10f} seconds, Average Nodes Generated: {avg_nodes:.2f}")
        
        # effective branching factor calculation (N + 1 = 1 + b* + b* x 2 + ... + b* x d)
        # N = total_nodes, d = difficulty
        # b* = (N + 1)^(1/d) - 1
        effective_branching_factor = (avg_nodes + 1) ** (1/difficulty) - 1
        
        print(f"Effective Branching Factor: {effective_branching_factor:.4f}")
        # print("Final State:", initial_state)