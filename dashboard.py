import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Gestão Documental",
    layout="wide"
)

df = pd.read_csv("dados/documentos.csv")

st.title("📂 Dashboard de Gestão Documental")

st.markdown("---")
st.subheader("📌 Indicadores Gerais")

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

col1.metric("📄 Total de documentos", total)
col2.metric("✅ Documentos ativos", ativos)
col3.metric("📦 Documentos arquivados", arquivados)
col4.metric("⚠️ Documentos pendentes", pendentes)

st.markdown("---")
st.subheader("📈 Análise dos Documentos")

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

# GRÁFICO TIPO DE DOCUMENTO

st.subheader("Tipos de documentos")

fig, ax = plt.subplots()

df_filtrado["Tipo_Documento"].value_counts().plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Tipo")
ax.set_ylabel("Quantidade")

st.pyplot(fig)

# ANÁLISE AUTOMÁTICA

st.subheader("📊 Resumo da análise")

setor_maior = df_filtrado["Setor"].value_counts().idxmax()
quantidade_setor = df_filtrado["Setor"].value_counts().max()

pendentes = len(
    df_filtrado[df_filtrado["Status"] == "Pendente"]
)

st.write(
    f"""
    - O setor com maior quantidade de documentos é **{setor_maior}**,
    com **{quantidade_setor} documentos**.

    - Existem **{pendentes} documentos pendentes**
    que precisam de acompanhamento.
    """
)

st.markdown("---")
st.subheader("📋 Lista de Documentos")

# TABELA

st.subheader("Documentos")

st.dataframe(df_filtrado)