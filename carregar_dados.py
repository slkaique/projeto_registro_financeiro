import sqlite3
from datetime import datetime

import numpy as np
import pandas as pd

from funcoes import criar_tabela

df_amazon = pd.read_csv("C:/Users/User/Downloads/amazon.csv", dtype=str)
df = df_amazon[["product_name", "actual_price", "discounted_price"]].copy()


def limpar_preco(valor):
    try:
        valor = str(valor).replace("₹", "").replace(",", "").strip()
        return round(float(valor), 2)
    except:
        return 0.00


df.loc[:, "valor"] = df["actual_price"].apply(limpar_preco)
df.loc[:, "desconto"] = df["discounted_price"].apply(limpar_preco)

df.loc[:, "valor"] = df["valor"].fillna(0.00)
df.loc[:, "desconto"] = df["desconto"].fillna(0.00)
df.loc[:, "tipo"] = "Venda"

inicio = datetime(2024, 11, 1)
fim = datetime.now()
df.loc[:, "data"] = pd.to_datetime(
    np.random.randint(inicio.timestamp(), fim.timestamp(), size=len(df)), unit="s"
)

df_final = df.loc[:, ["product_name", "tipo", "valor", "desconto", "data"]].copy()
df_final.rename(columns={"product_name": "descricao"}, inplace=True)

df_final["valor"] = df_final["valor"].astype(float).round(2)
df_final["desconto"] = df_final["desconto"].astype(float).round(2)
df_final["data"] = df_final["data"].astype(str)

df_final.to_csv("amazon.csv", index=False)
criar_tabela()
conn = sqlite3.connect("registro.db", check_same_thread=False)
df_final.to_sql("registros", conn, if_exists="append", index=False)
conn.close()

print(f"{len(df_final)} registros inseridos com sucesso no banco!")
