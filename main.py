import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Exercicio 1
dfSpace = pd.read_csv('space.csv', delimiter=";")

empresas_EUA = dfSpace[dfSpace['Location'].str.contains('USA', case=False)] #Empresas que estão os EUA
empresas_EUA = empresas_EUA['Company Name'].unique()
empresas_EUA = len(empresas_EUA) #Quantidade de empresas unicas


empresas_China = dfSpace[dfSpace['Location'].str.contains('China', case=False)] #Empresas que estão na China
empresas_China = empresas_China['Company Name'].unique()
empresas_China = len(empresas_China) #Quantidade de empresas unicas

paises = ['EUA', 'China']
numeros = [empresas_EUA, empresas_China]

#Construindo o gráfico
plt.bar(range(len(paises)), numeros, color='green')
plt.xlabel('Paises')
plt.ylabel('Quantidade')
plt.title('Quantidade de Empresas Espaciais')
plt.xticks(range(len(paises)), paises)
plt.show()

# Exercicio 2
dfPaises = pd.read_csv('paises.csv', delimiter=";")

paises_North = dfPaises[dfPaises['Region'].str.contains('NORTHERN AMERICA', case=False)] #Paises que estão na America do Norte
mortalidade = paises_North['Deathrate']
natalidade =paises_North['Birthrate']

x = np.array(paises_North.iloc[:, 0])
y = np.array(mortalidade)
y2 = np.array(natalidade)

plt.xlabel('Paises da America do Norte')
plt.ylabel('Valores de Mortalidade e Natalidade')
plt.plot(x, y, 'r--', x, y2, 'b--')
plt.show()

