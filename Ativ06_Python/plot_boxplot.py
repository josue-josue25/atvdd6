import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tabela_caixa = pd.read_csv(r'dados\dados_boxplot.csv')

plt.figure(figsize=(10, 6))

colunas_numericas = tabela_caixa.select_dtypes(include=['number'])

sns.boxplot(data=colunas_numericas, palette='pastel')

plt.title('Distribuição dos Dados (Boxplot)')
plt.grid(axis='y', linestyle='-.', alpha=0.6)
plt.tight_layout()

plt.show()