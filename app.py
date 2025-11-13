from datetime import datetime

import pandas as pd
import streamlit as st

from funcoes import conectar, criar_tabela, inserir_registro

criar_tabela()

st.sidebar.title("📊 Navegação")
pagina = st.sidebar.radio("Escolha a página:", ["Registrar Movimentos", "Dashboard"])

if pagina == "Registrar Movimentos":
    st.title("📝 Registro de Caixa")
    descricao = st.text_input("Descrição")
    tipo = st.selectbox("Tipo de movimento", ["Venda", "Despesa"])
    valor = st.number_input("Valor", min_value=0.0, format="%.2f")
    desconto = st.number_input("Desconto", min_value=0.0, format="%.2f")

    if st.button("Salvar"):
        if descricao and valor:
            inserir_registro(descricao, tipo, valor, desconto)
            st.success("Registro salvo com sucesso!")
        else:
            st.warning("Preencha todos os campos obrigatórios.")

elif pagina == "Dashboard":
    st.title("📈 Dashboard de Resultados")
    conn = conectar()
    df = pd.read_sql_query("SELECT * FROM registros", conn)
    conn.close()

    if df.empty:
        st.info("Nenhum dado cadastrado ainda.")
    else:
        df["data"] = pd.to_datetime(df["data"])
        df["mes"] = df["data"].dt.month_name()
        vendas = df[df["tipo"] == "Venda"]

        produto_top = vendas.groupby("descricao")["valor"].sum().idxmax()
        ultimo_mes = datetime.now().month
        vendas_mes = vendas[vendas["data"].dt.month == ultimo_mes]["valor"].sum()

        st.metric("Produto mais vendido", produto_top)
        st.metric("Vendas acumuladas no mês", f"R$ {vendas_mes:.2f}")

        st.bar_chart(vendas.groupby("mes")["valor"].sum())
