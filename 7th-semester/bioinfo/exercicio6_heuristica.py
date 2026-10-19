"""
Exercício 6: Desenvolvendo uma Heurística de Alinhamento de Sequências
Heurística Desenvolvida: Block Composition Filtering (BCF) - Filtragem por Composição de Bloco
"""

def block_composition_filtering(seq1, seq2, block_size=4, similarity_threshold=1.0):
    """
    Heurística própria inspirada no BLAST.
    Divide a seq1 em blocos fixos e calcula a contagem/composição de caracteres.
    Varre a seq2 buscando janelas com composição idêntica ou altamente similar (independente da ordem).
    Apenas onde há casamento de composição, realiza-se uma extensão local simples.
    """
    
    def get_composition(sub_seq):
        comp = {}
        for char in sub_seq:
            comp[char] = comp.get(char, 0) + 1
        return comp

    def get_comp_distance(comp1, comp2):
        all_chars = set(comp1.keys()).union(set(comp2.keys()))
        dist = 0
        for char in all_chars:
            dist += abs(comp1.get(char, 0) - comp2.get(char, 0))
        return dist

    candidates = []
    len1, len2 = len(seq1), len(seq2)
    
    # 1. Fase de Identificação de Sementes por Composição de Bloco (Filtragem)
    for i in range(0, len1 - block_size + 1, block_size): # Avança em blocos sem sobreposição para velocidade
        sub1 = seq1[i:i+block_size]
        comp1 = get_composition(sub1)
        
        # Procura correspondências de composição na Seq2 (janela deslizante passo 1)
        for j in range(0, len2 - block_size + 1):
            sub2 = seq2[j:j+block_size]
            comp2 = get_composition(sub2)
            
            # Distância 0 significa composição idêntica de caracteres (ex: ACGT e TGCA)
            if get_comp_distance(comp1, comp2) <= (block_size * (1 - similarity_threshold)):
                candidates.append((i, j))
                
    # 2. Fase de Extensão das Regiões Candidatas (Semelhante ao Ungapped Extension)
    alignments = []
    match_score = 2
    mismatch_score = -1
    gap_score = -2
    
    seen_regions = set() # Evitar duplicatas redundantes
    
    for start1, start2 in candidates:
        # Evitar re-estender sementes muito próximas já processadas
        if (start1, start2) in seen_regions:
            continue
            
        # Estender para a direita
        i, j = start1, start2
        current_score = 0
        max_score = 0
        best_end1, best_end2 = i, j
        
        # Extensão linear local sem gaps para simplicidade e velocidade da heurística
        while i < len1 and j < len2:
            if seq1[i] == seq2[j]:
                current_score += match_score
            else:
                current_score += mismatch_score
                
            if current_score > max_score:
                max_score = current_score
                best_end1 = i + 1
                best_end2 = j + 1
            elif current_score < max_score - 3: # X-drop ideal para parar extensão se o score cair muito
                break
            i += 1
            j += 1
            
        # Armazenar resultados válidos com score positivo
        if max_score > 0:
            align1 = seq1[start1:best_end1]
            align2 = seq2[start2:best_end2]
            
            # Criar representação visual simples do alinhamento
            match_line = "".join(["|" if a == b else "." for a, b in zip(align1, align2)])
            
            alignment_info = {
                "pos_seq1": (start1, best_end1),
                "pos_seq2": (start2, best_end2),
                "score": max_score,
                "align1": align1,
                "match": match_line,
                "align2": align2
            }
            if alignment_info not in alignments:
                alignments.append(alignment_info)
                
            # Marcar bloco vizinho como visto para otimização
            for k in range(block_size):
                seen_regions.add((start1 + k, start2 + k))
                
    # Ordenar alinhamentos encontrados por score decrescente
    alignments = sorted(alignments, key=lambda x: x['score'], reverse=True)
    return alignments

# Exemplo de Execução Demonstrativa exigida pelo enunciado
if __name__ == "__main__":
    print("--- TESTE DA HEURÍSTICA DE ALINHAMENTO LOCAL (BCF) ---")
    
    # Duas sequências contendo uma região conservada e mutações locais
    sequencia_A = "TTGACACGTGATCGATCTAGCTAGCTAGCTAAAGT"
    sequencia_B = "GGGGACGTGATCGATCTTTTTTTCGATCTAGCTAA"
    
    print(f"Sequência A: {sequencia_A}")
    print(f"Sequência B: {sequencia_B}\n")
    
    resultados = block_composition_filtering(sequencia_A, sequencia_B, block_size=4, similarity_threshold=1.0)
    
    print(f"Alinhamentos locais proeminentes encontrados: {len(resultados)}\n")
    for idx, res in enumerate(resultados[:3], 1): # Exibir os 3 melhores
        print(f"Alinhamento #{idx} - Score: {res['score']}")
        print(f"Posição na Seq 1: {res['pos_seq1']} | Posição na Seq 2: {res['pos_seq2']}")
        print(f"Seq 1: {res['align1']}")
        print(f"Match: {res['match']}")
        print(f"Seq 2: {res['align2']}")
        print("-" * 50)
