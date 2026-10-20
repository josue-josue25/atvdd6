import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tabela_regressao = pd.read_csv(r'dados\dados_regressao.csv')
titulos = tabela_regressao.columns

plt.figure(figsize=(12, 7))
sns.regplot(data=tabela_regressao, x=titulos[0], y=titulos[1], scatter_kws={'alpha':0.7}, line_kws={'color':'darkred'})

plt.title('Análise de Regressão')
plt.xlabel(titulos[0])
plt.ylabel(titulos[1])
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.show()