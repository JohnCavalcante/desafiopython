#2. Criar um único *dataframe* como os dados de 2019 e 2020; e


import pandas as pd

data1 = pd.read_csv('datatran2019.csv', encoding='latin-1',sep=';')
data2 = pd.read_csv('datatran2020.csv', encoding='latin-1',sep=';')

dadosgerais = pd.concat([data1, data2], ignore_index=True)


print(dadosgerais.head(10))  #Exive os 10 primeiros resultados da junção dos dados de 2019 e 2020 criados num único dataframe
