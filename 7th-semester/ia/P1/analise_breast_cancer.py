import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg') # Essencial para rodar no servidor sem interface gráfica
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

def main():
    # ---------------------------------------------------------
    # CARREGAMENTO DOS DADOS
    # ---------------------------------------------------------
    print("Carregando base Breast Cancer Wisconsin...")
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target # 0 = maligno, 1 = benigno

    # ---------------------------------------------------------
    # QUESTÃO 3.a - Análise de Outliers
    # ---------------------------------------------------------
    print("\n" + "="*50)
    print("A) ANÁLISE DE OUTLIERS")
    
    # Escolhendo duas variáveis contínuas: 'mean area' e 'mean compactness'
    variaveis_boxplot = ['mean area', 'mean compactness']
    
    plt.figure(figsize=(10, 5))
    for i, col in enumerate(variaveis_boxplot, 1):
        plt.subplot(1, 2, i)
        sns.boxplot(y=df[col], color='skyblue')
        plt.title(f'Boxplot: {col}')
    
    plt.tight_layout()
    plt.savefig('boxplots_outliers.png', dpi=300)
    print(" -> 'boxplots_outliers.png' salvo com sucesso!")

    # ---------------------------------------------------------
    # QUESTÃO 3.b - Matriz de Correlação e Multicolinearidade
    # ---------------------------------------------------------
    print("\n" + "="*50)
    print("B) MATRIZ DE CORRELAÇÃO")
    
    # Gerando a matriz de correlação
    corr_matrix = df.corr()
    
    # Salvando a imagem do Heatmap
    plt.figure(figsize=(12, 10))
    # Pegamos apenas as primeiras 10 variáveis para o plot não ficar ilegível
    cols_plot = list(data.feature_names[:10]) + ['target']
    sns.heatmap(df[cols_plot].corr(), annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
    plt.title('Matriz de Correlação (Top 10 Features + Target)')
    plt.tight_layout()
    plt.savefig('matriz_correlacao.png', dpi=300)
    print(" -> 'matriz_correlacao.png' salvo com sucesso!")

    # Análise programática: Quais variáveis têm maior correlação entre si?
    # Pegamos a matriz absoluta, tiramos a diagonal (que é 1.0) e pegamos os maiores valores
    corr_unstacked = corr_matrix.abs().unstack()
    corr_unstacked = corr_unstacked[corr_unstacked < 1.0] # Remove correlação consigo mesmo
    top_correlacoes = corr_unstacked.sort_values(ascending=False).drop_duplicates().head(3)
    
    print("\nTop 3 Maiores Correlações entre Atributos (Indícios de Multicolinearidade):")
    for (var1, var2), coef in top_correlacoes.items():
        print(f" - {var1} e {var2}: {coef:.4f}")

    # Análise: Quais atributos estão mais associados ao diagnóstico (target)?
    print("\nTop 3 Atributos mais associados ao Diagnóstico (target):")
    target_corr = corr_matrix['target'].drop('target').abs().sort_values(ascending=False).head(3)
    for var, coef in target_corr.items():
        print(f" - {var}: {coef:.4f}")

    # ---------------------------------------------------------
    # QUESTÃO 3.c - Normalização e Impacto
    # ---------------------------------------------------------
    print("\n" + "="*50)
    print("C) NORMALIZAÇÃO (PADRONIZAÇÃO)")
    
    # Escolhendo 3 variáveis com escalas muito diferentes
    vars_escala = ['mean area', 'mean smoothness', 'mean symmetry']
    
    print("\nEscalas originais (Média e Desvio Padrão):")
    for var in vars_escala:
        print(f" - {var}: Média = {df[var].mean():.4f}, Std = {df[var].std():.4f}")
        
    # Aplicando a Padronização (Z-score)
    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df[vars_escala]), columns=vars_escala)
    
    print("\nEscalas APÓS Padronização:")
    for var in vars_escala:
        # A média ficará muito próxima de 0 e o desvio padrão igual a 1
        print(f" - {var}: Média = {df_scaled[var].mean():.4f}, Std = {df_scaled[var].std():.4f}")

if __name__ == "__main__":
    main()