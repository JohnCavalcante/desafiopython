# 3. Criar novas colunas com mês e ano a partir da coluna `data_inversa`.

import pandas as pd

data1 = pd.read_csv("datatran2019.csv", encoding="latin-1", sep=";")
data2 = pd.read_csv("datatran2020.csv", encoding="latin-1", sep=";")

dadosgerais = pd.concat([data1, data2], ignore_index=True)  # Junção dos dois dataframes


dadosgerais["data_inversa"] = pd.to_datetime(
    dadosgerais["data_inversa"], format="%Y-%m-%d"
)

dadosgerais["ano"] = dadosgerais[
    "data_inversa"
].dt.year  # coluna 'ano' com o ano da data

dadosgerais["mes"] = dadosgerais[
    "data_inversa"
].dt.month  # coluna 'mes' com o mês da data


print(
    dadosgerais.head(6)
)  # Exibição dos 6 primeiros resultados já com a coluna de ano e mês criados
