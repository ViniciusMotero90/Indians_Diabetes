import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',320)
colunas = ['preg','plas','pres','skin','test','mass','pedi','age','class']
dados = pd.read_csv('diabetes.csv',names=colunas)
dados = dados.apply(pd.to_numeric, errors='coerce')
print(dados.dtypes)
print(dados.corr(method='pearson'))

plt.figure(figsize=(10,10))
sns.heatmap(dados.corr())
plt.show()