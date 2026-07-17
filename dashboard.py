import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Gestão Documental",
    layout="wide"
)

df = pd.read_csv("dados/documentos.csv")

st.title("📂 Dashboard de Gestão Documental")


# FILTROS
st.sidebar.header("Filtros")

setor = st.sidebar.multiselect(
    "Selecione o setor:",
    df["Setor"].unique(),
    default=df["Setor"].unique()
)

status = st.sidebar.multiselect(
    "Selecione o status:",
    df["Status"].unique(),
    default=df["Status"].unique()
)


# Aplicar filtros
df_filtrado = df[
    (df["Setor"].isin(setor)) &
    (df["Status"].isin(status))
]


# INDICADORES

total = len(df_filtrado)
ativos = len(df_filtrado[df_filtrado["Status"] == "Ativo"])
arquivados = len(df_filtrado[df_filtrado["Status"] == "Arquivado"])
pendentes = len(df_filtrado[df_filtrado["Status"] == "Pendente"])


col1, col2, col3, col4 = st.columns(4)

col1.metric("Total", total)
col2.metric("Ativos", ativos)
col3.metric("Arquivados", arquivados)
col4.metric("Pendentes", pendentes)


# GRÁFICO SETOR

st.subheader("Documentos por setor")

fig, ax = plt.subplots()

df_filtrado["Setor"].value_counts().plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)


# GRÁFICO STATUS

st.subheader("Status dos documentos")

fig, ax = plt.subplots()

df_filtrado["Status"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax
)

ax.set_ylabel("")

st.pyplot(fig)


# TABELA

st.subheader("Documentos")

st.dataframe(df_filtrado)