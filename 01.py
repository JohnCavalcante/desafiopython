#1. Carregar os dados de 2019 e 2020 (datatran2019.csv e datatran2020.csv);

import pandas as pd

data1 = pd.read_csv('datatran2020.csv', encoding='latin-1',sep=';')
data2 = pd.read_csv('datatran2020.csv', encoding='latin-1',sep=';')

print(data1.head(6))  #Resultado dos 10 primeiras linhas do DataFrame
print(data2.head(6))  #Resultado dos 10 primeiras linhas do DataFrame


