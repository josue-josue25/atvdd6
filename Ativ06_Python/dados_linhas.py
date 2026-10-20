import pandas as pd
import matplotlib.pyplot as plt

tabela_dados = pd.read_csv(r'dados\dados_linhas.csv')
nomes_colunas = tabela_dados.columns

plt.figure(figsize=(10, 6))
plt.plot(tabela_dados[nomes_colunas[0]], tabela_dados[nomes_colunas[1]], marker='s', linewidth=2.5, color='navy')

plt.title('Evolução dos Dados')
plt.xlabel(nomes_colunas[0])
plt.ylabel(nomes_colunas[1])

plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()

plt.show()