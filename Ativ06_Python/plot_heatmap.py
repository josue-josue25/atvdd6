import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados_mapa = pd.read_csv(r'dados\dados_heatmap.csv')

valores_numericos = dados_mapa.select_dtypes(include=['number'])

plt.figure(figsize=(11, 7))
sns.heatmap(valores_numericos, annot=True, cmap='plasma', fmt='.2f')
plt.title('Visualização de Mapa de Calor')
plt.tight_layout()

plt.show()