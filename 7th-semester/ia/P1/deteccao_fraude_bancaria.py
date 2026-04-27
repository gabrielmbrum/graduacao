import os
import pandas as pd
import numpy as np
import xgboost as xgb
import matplotlib
# Configuração para servidores sem interface gráfica (evita erros ao gerar imagens)
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_curve
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from imblearn.combine import SMOTETomek

def main():
    # ---------------------------------------------------------
    # 1. CARREGAMENTO DOS DADOS
    # ---------------------------------------------------------
    DATA_PATH = "../data/creditcard.csv" 
    
    print("Carregando os dados...")
    df = pd.read_csv(DATA_PATH)
    
    X = df.drop('Class', axis=1)
    y = df['Class']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # ---------------------------------------------------------
    # 2. BALANCEAMENTO (SMOTETomek) COM CHECKPOINT
    # ---------------------------------------------------------
    arquivo_x_resampled = 'X_train_balanceado.csv'
    arquivo_y_resampled = 'y_train_balanceado.csv'

    if os.path.exists(arquivo_x_resampled) and os.path.exists(arquivo_y_resampled):
        print("\nArquivos de treino balanceados encontrados! Carregando do disco...")
        X_train_resampled = pd.read_csv(arquivo_x_resampled)
        y_train_resampled = pd.read_csv(arquivo_y_resampled)
    else:
        print("\nArquivos balanceados não encontrados. Iniciando SMOTETomek (isso pode demorar)...")
        smt = SMOTETomek(random_state=42)
        X_train_resampled, y_train_resampled = smt.fit_resample(X_train, y_train)
        
        print("Salvando arquivos balanceados no disco...")
        X_train_resampled.to_csv(arquivo_x_resampled, index=False)
        y_train_resampled.to_csv(arquivo_y_resampled, index=False)

    print(f"Tamanho do X_train original: {X_train.shape}")
    print(f"Tamanho do X_train balanceado: {X_train_resampled.shape}")

    # Correção do Warning do Scikit-Learn
    y_train_resampled = np.ravel(y_train_resampled)
    y_test = np.ravel(y_test)

    # ---------------------------------------------------------
    # 3. REGRESSÃO LOGÍSTICA
    # ---------------------------------------------------------
    print("\n" + "="*50)
    print("Iniciando busca rápida para Regressão Logística...")
    
    param_grid_rl = {
        'penalty': ['l1', 'l2'],
        'C': [0.01, 0.1, 1, 10, 100],
        'solver': ['liblinear', 'saga']
    }
    
    log_reg = LogisticRegression(max_iter=2000, random_state=42)
    busca_rapida_rl = RandomizedSearchCV(estimator=log_reg, param_distributions=param_grid_rl, 
                                         n_iter=10, scoring='f1', cv=3, n_jobs=-1, random_state=42, verbose=1)
    
    busca_rapida_rl.fit(X_train_resampled, y_train_resampled)
    melhor_rl = busca_rapida_rl.best_estimator_
    y_pred_rl = melhor_rl.predict(X_test)
    
    print("\nMelhores Hiperparâmetros RL:", busca_rapida_rl.best_params_)
    print("Relatório de Classificação RL:")
    print(classification_report(y_test, y_pred_rl))
    print("Matriz de Confusão RL:\n", confusion_matrix(y_test, y_pred_rl))

    # ---------------------------------------------------------
    # 4. RANDOM FOREST
    # ---------------------------------------------------------
    print("\n" + "="*50)
    print("Iniciando busca rápida para Random Forest...")
    
    param_grid_rf = {
        'n_estimators': [100, 200, 300],
        'max_depth': [10, 20, 30, None],
        'min_samples_split': [2, 5, 10],
        'max_features': ['sqrt', 'log2']
    }
    
    rf_model = RandomForestClassifier(random_state=42)
    busca_rapida_rf = RandomizedSearchCV(estimator=rf_model, param_distributions=param_grid_rf, 
                                         n_iter=10, scoring='f1', cv=3, n_jobs=-1, random_state=42, verbose=1)
    
    busca_rapida_rf.fit(X_train_resampled, y_train_resampled)
    melhor_rf = busca_rapida_rf.best_estimator_
    y_pred_rf = melhor_rf.predict(X_test)
    
    print("\nMelhores Hiperparâmetros RF:", busca_rapida_rf.best_params_)
    print("Relatório de Classificação RF:")
    print(classification_report(y_test, y_pred_rf))
    print("Matriz de Confusão RF:\n", confusion_matrix(y_test, y_pred_rf))

    # ---------------------------------------------------------
    # 5. XGBOOST
    # ---------------------------------------------------------
    print("\n" + "="*50)
    print("Iniciando busca rápida para XGBoost...")
    
    param_grid_xgb = {
        'n_estimators': [100, 200],
        'max_depth': [3, 5, 7],
        'learning_rate': [0.01, 0.1, 0.2],
        'subsample': [0.8, 1.0],
        'colsample_bytree': [0.8, 1.0]
    }
    
    xgb_model = xgb.XGBClassifier(tree_method='hist', device='cpu', eval_metric='logloss', random_state=42)
    busca_rapida_xgb = RandomizedSearchCV(estimator=xgb_model, param_distributions=param_grid_xgb, 
                                          n_iter=10, scoring='f1', cv=3, n_jobs=-1, random_state=42, verbose=1)
    
    busca_rapida_xgb.fit(X_train_resampled, y_train_resampled)
    melhor_xgb = busca_rapida_xgb.best_estimator_
    y_pred_xgb = melhor_xgb.predict(X_test)
    
    print("\nMelhores Hiperparâmetros XGBoost:", busca_rapida_xgb.best_params_)
    print("Relatório de Classificação XGBoost:")
    print(classification_report(y_test, y_pred_xgb))
    print("Matriz de Confusão XGBoost:\n", confusion_matrix(y_test, y_pred_xgb))

    # ---------------------------------------------------------
    # 6. GERAÇÃO DE GRÁFICOS PARA O RELATÓRIO
    # ---------------------------------------------------------
    print("\n" + "="*50)
    print("Gerando e salvando visualizações gráficas...")

    # Gráfico 1: Heatmap das Matrizes de Confusão
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    modelos = [('Regressão Logística', y_pred_rl), ('Random Forest', y_pred_rf), ('XGBoost', y_pred_xgb)]
    
    for i, (nome, y_pred) in enumerate(modelos):
        cm = confusion_matrix(y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[i], cbar=False)
        axes[i].set_title(f'Matriz de Confusão: {nome}')
        axes[i].set_xlabel('Predito')
        axes[i].set_ylabel('Real')
    
    plt.tight_layout()
    plt.savefig('matrizes_confusao.png', dpi=300)
    print(" -> 'matrizes_confusao.png' salvo com sucesso!")

    # Gráfico 2: Curva Precision-Recall
    plt.figure(figsize=(10, 7))
    modelos_probs = [
        ('Regressão Logística', melhor_rl.predict_proba(X_test)[:, 1]),
        ('Random Forest', melhor_rf.predict_proba(X_test)[:, 1]),
        ('XGBoost', melhor_xgb.predict_proba(X_test)[:, 1])
    ]
    
    for nome, y_prob in modelos_probs:
        precision, recall, _ = precision_recall_curve(y_test, y_prob)
        plt.plot(recall, precision, lw=2, label=nome)
        
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Curva Precision-Recall Comparativa')
    plt.legend(loc='lower left')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig('curva_precision_recall.png', dpi=300)
    print(" -> 'curva_precision_recall.png' salvo com sucesso!")

    # Gráfico 3: Feature Importance (XGBoost)
    fig, ax = plt.subplots(figsize=(12, 8))
    xgb.plot_importance(melhor_xgb, max_num_features=15, height=0.5, ax=ax, importance_type='weight')
    plt.title('Top 15 Atributos mais Importantes - XGBoost')
    plt.tight_layout()
    plt.savefig('feature_importance_xgb.png', dpi=300)
    print(" -> 'feature_importance_xgb.png' salvo com sucesso!")
    print("Pipeline concluído!")

if __name__ == "__main__":
    main()