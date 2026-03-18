import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def print_csv(seq1, seq2, aligned1, aligned2, score):
    df = pd.DataFrame({
        "seqA": [seq1],
        "seqB": [seq2],
        "aligned1": [aligned1],
        "aligned2": [aligned2],
        "score": [score]
    })
    df.to_csv("data.csv", mode='a', header=not pd.io.common.file_exists("data.csv"), index=False)


# ================================
# ETAPA 1 — Sequências de exemplo
# ================================

# Sequência maior (simulando um trecho de DNA maior)
seqs = [
    "ACTGACTA",
    "TGACTGA",
    "GACTTAC",
    "CCTGACAA",
    "TTGACTC",
    "ACTTGAAC",
    "GACTGGA",
    "TACTGAC",
    "GGACTTA",
    "CTGACTG" ]

# seq1 = "TTTATGCTAGCTAAA"

# Sequência menor que pode estar contida dentro da maior
# seq2 = "GGGATGCTAGGG"

# Sistema de pontuação do alinhamento
match = 2      # quando as bases são iguais
mismatch = -1  # quando as bases são diferentes
gap = -2       # penalidade por inserir lacuna

# print("Sequência 1:", seq1)
# print("Sequência 2:", seq2)

# =====================================
# ETAPA 2 — Criando a matriz de scores
# =====================================

# Matriz para armazenar os resultados finais de todas as comparações
results_matrix = np.zeros((len(seqs), len(seqs)))
alignment_matrix = np.full((len(seqs), len(seqs)), "", dtype=object)

for idx1, seq1 in enumerate(seqs):
    for idx2, seq2 in enumerate(seqs):
        print(f"Comparando:\nSeq1: {seq1}\nSeq2: {seq2}\n")
        if seq1 != seq2:
            rows = len(seq1) + 1
            cols = len(seq2) + 1

            score_matrix = np.zeros((rows, cols))

            # =====================================
            # ETAPA 3 — Preenchendo a matriz
            # =====================================

            max_score = 0
            max_pos = (0, 0)

            for i in range(1, rows):
                for j in range(1, cols):

                    # Movimento diagonal (comparando bases)
                    if seq1[i-1] == seq2[j-1]:
                        diag = score_matrix[i-1][j-1] + match
                    else:
                        diag = score_matrix[i-1][j-1] + mismatch

                    # Inserção de gap
                    up = score_matrix[i-1][j] + gap

                    # Deleção (gap na outra sequência)
                    left = score_matrix[i][j-1] + gap
                    
                    # Smith-Waterman usa zero para reiniciar alinhamento
                    score = max(0, diag, up, left)
                    score_matrix[i][j] = score

                    # Guardamos o maior valor da matriz
                    if score > max_score:
                        max_score = score
                        max_pos = (i, j)
            
            # Armazena o score máximo na matriz de resultados
            results_matrix[idx1, idx2] = max_score


            # =====================================
            # ETAPA 4 — Mostrar matriz
            # =====================================



            df = pd.DataFrame(
                score_matrix,
                index=["-"] + list(seq1),
                columns=["-"] + list(seq2)
            )


            # =====================================
            # ETAPA 5 — Heatmap da matriz
            # =====================================



            # plt.figure(figsize=(8,6))
            # plt.imshow(score_matrix)
            # plt.colorbar(label="Pontuação")
            # plt.xticks(range(cols), ["-"] + list(seq2))
            # plt.yticks(range(rows), ["-"] + list(seq1))
            # plt.title("Matriz de Alinhamento Local")
            # plt.show()

            # =====================================
            # ETAPA 6 — Traceback (reconstruir alinhamento)
            # =====================================

            aligned1 = ""
            aligned2 = ""

            i, j = max_pos

            while score_matrix[i][j] != 0:
                current = score_matrix[i][j]
                diag = score_matrix[i-1][j-1]
                up = score_matrix[i-1][j]
                left = score_matrix[i][j-1]

                if seq1[i-1] == seq2[j-1]:
                    score_diag = diag + match
                else:
                    score_diag = diag + mismatch

                if current == score_diag:
                    aligned1 = seq1[i-1] + aligned1
                    aligned2 = seq2[j-1] + aligned2
                    i -= 1
                    j -= 1

                elif current == up + gap:
                    aligned1 = seq1[i-1] + aligned1
                    aligned2 = "-" + aligned2
                    i -= 1

                elif current == left + gap:
                    aligned1 = "-" + aligned1
                    aligned2 = seq2[j-1] + aligned2
                    j -= 1

            print("Melhor alinhamento local:")
            print(aligned1)
            print(aligned2)
            print("Score:", max_score)
            alignment_matrix[idx1, idx2] = f"{aligned1}\n{aligned2}"
            print_csv(seq1, seq2, aligned1, aligned2, max_score)

# =====================================
# GERAÇÃO DA TABELA FINAL DE COMPARAÇÃO
# =====================================

fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('tight')
ax.axis('off')

# Criando a tabela
# cellText deve conter os valores, rowLabels e colLabels as sequências
table = ax.table(cellText=results_matrix,
                 rowLabels=seqs,
                 colLabels=seqs,
                 loc='center')

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.title("Matriz de Scores Smith-Waterman (Todos contra Todos)")
plt.savefig("tabela_comparacao.png", bbox_inches='tight', dpi=300)
print("\nImagem 'tabela_comparacao.png' gerada com sucesso!")

# =====================================
# GERAÇÃO DA TABELA DE ALINHAMENTOS
# =====================================

# Ajustando o tamanho da figura para comportar células maiores
fig2, ax2 = plt.subplots(figsize=(22, 14))
ax2.axis('tight')
ax2.axis('off')

# Criando a tabela de alinhamentos
table2 = ax2.table(cellText=alignment_matrix,
                 rowLabels=seqs,
                 colLabels=seqs,
                 loc='center')

table2.auto_set_font_size(False)
table2.set_fontsize(12) # Fonte levemente menor para garantir que caiba
table2.scale(1.0, 3.0)  # Aumentando a altura da célula para evitar corte do texto

# Ajustando a fonte para ser monoespaçada (importante para alinhamentos)
for key, cell in table2.get_celld().items():
    cell.set_text_props(fontfamily='monospace', multialignment='center')

plt.title("Matrizes de Alinhamentos (Melhores Alinhamentos Locais)")
plt.savefig("tabela_alinhamentos.png", bbox_inches='tight', dpi=300)
print("\nImagem 'tabela_alinhamentos.png' gerada com sucesso!")

# =====================================
# GERAÇÃO DA TABELA TOP 2 SCORES
# =====================================

# Coletar todos os pares únicos (excluindo auto-comparação)
all_pairs = []
for i in range(len(seqs)):
    for j in range(i + 1, len(seqs)):
        score = results_matrix[i, j]
        alignment = alignment_matrix[i, j]
        all_pairs.append({
            "Seq1": seqs[i],
            "Seq2": seqs[j],
            "Alinhamento": alignment,
            "Score": score
        })

# Ordenar por score decrescente
all_pairs.sort(key=lambda x: x["Score"], reverse=True)

# Pegar os top 2 (pode haver empates, pega os 2 primeiros da lista ordenada)
top_2 = all_pairs[:2]

# Preparar dados para a tabela
cell_text = [] 
for p in top_2:
    row = [p["Seq1"], p["Seq2"], p["Alinhamento"], str(int(p["Score"]))]
    cell_text.append(row)

col_labels = ["Sequência A", "Sequência B", "Alinhamento", "Score"]

# Plotar tabela dedicada
fig3, ax3 = plt.subplots(figsize=(12, 5))
ax3.axis('tight')
ax3.axis('off')

# Criando a tabela
table3 = ax3.table(cellText=cell_text,
                 colLabels=col_labels,
                 loc='center',
                 cellLoc='center')

table3.auto_set_font_size(False)
table3.set_fontsize(12)
table3.scale(1.0, 5.0)  # Altura generosa para o alinhamento não cortar

# Estilização fina
for (row, col), cell in table3.get_celld().items():
    if row == 0:
        cell.set_text_props(weight='bold')
        cell.set_facecolor('#f2f2f2') # Cinza claro no cabeçalho
    else:
        # Coluna do alinhamento (índice 2) deve ser monospace
        if col == 2:
            cell.set_text_props(fontfamily='monospace')

plt.title("Top 2 Melhores Alinhamentos (Excluindo Auto-comparação)")
plt.savefig("tabela_top2.png", bbox_inches='tight', dpi=300)
print("\nImagem 'tabela_top2.png' gerada com sucesso!")