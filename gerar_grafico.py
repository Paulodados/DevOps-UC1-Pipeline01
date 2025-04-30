import pandas as pd  
import matplotlib.pyplot as plt  

df = pd.read_csv('data.csv') 

#criar figura e eixo explicitamente
fig. ax = plt subplots()

#associa o plot aos eixos criados
df['idade'].plot(kind='hist' , ax=ax)
ax  
plt.title('Distribuição de Idades')  
plt.savefig('grafico.png')  