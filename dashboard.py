import streamlit as st
import pandas as pd
import plotly.express as px


# ==========================
# CONFIGURAÇÃO
# ==========================

st.set_page_config(
    page_title="Gestão Documental",
    page_icon="📂",
    layout="wide"
)


# ==========================
# ESTILO
# ==========================

st.markdown(
    """
    <style>

    .main {
        background-color:#f5f7fa;
    }

    h1 {
        color:#1f4e79;
    }

    h2, h3 {
        color:#1f4e79;
    }

    div[data-testid="metric-container"] {
        background:white;
        padding:15px;
        border-radius:15px;
        box-shadow:0px 2px 8px #cccccc;
    }

    </style>
    """,
    unsafe_allow_html=True
)



# ==========================
# CARREGAR DADOS
# ==========================

df = pd.read_csv(
    "dados/documentos.csv"
)


df["Data_Criacao"] = pd.to_datetime(
    df["Data_Criacao"]
)


df = df.dropna()



# ==========================
# CABEÇALHO
# ==========================

st.title(
    "📂 Sistema de Inteligência Documental"
)


st.caption(
    "Dashboard analítico para controle e acompanhamento de documentos."
)



# ==========================
# FILTROS
# ==========================

st.sidebar.header(
    "🔎 Filtros"
)



setores = df["Setor"].unique()


setor = st.sidebar.multiselect(
    "Setor:",
    setores,
    default=list(setores)
)



status_lista = df["Status"].unique()


status = st.sidebar.multiselect(
    "Status:",
    status_lista,
    default=list(status_lista)
)



responsaveis = df["Responsavel"].unique()


responsavel = st.sidebar.multiselect(
    "Responsável:",
    responsaveis,
    default=list(responsaveis)
)



df_filtrado = df[
    (df["Setor"].isin(setor)) &
    (df["Status"].isin(status)) &
    (df["Responsavel"].isin(responsavel))
]



if df_filtrado.empty:

    st.warning(
        "Nenhum documento encontrado."
    )

    st.stop()



# ==========================
# INDICADORES
# ==========================

total = len(df_filtrado)


ativos = len(
    df_filtrado[
        df_filtrado["Status"]=="Ativo"
    ]
)


arquivados = len(
    df_filtrado[
        df_filtrado["Status"]=="Arquivado"
    ]
)


pendentes = len(
    df_filtrado[
        df_filtrado["Status"]=="Pendente"
    ]
)



# ==========================
# ABAS
# ==========================

aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs(
[
"📌 Visão Geral",
"🏢 Setores",
"📊 Status",
"📁 Tipos",
"👥 Responsáveis",
"📋 Dados"
]
)



# ==========================
# VISÃO GERAL
# ==========================

with aba1:


    st.subheader(
        "Indicadores Gerais"
    )


    c1,c2,c3,c4 = st.columns(4)


    c1.metric(
        "📄 Total",
        total
    )


    c2.metric(
        "✅ Ativos",
        ativos
    )


    c3.metric(
        "📦 Arquivados",
        arquivados
    )


    c4.metric(
        "⚠️ Pendentes",
        pendentes
    )


    st.divider()


    maior_setor = (
        df_filtrado["Setor"]
        .value_counts()
        .idxmax()
    )


    maior_responsavel = (
        df_filtrado["Responsavel"]
        .value_counts()
        .idxmax()
    )


    st.info(
        f"""
        📌 Maior volume documental:

        **Setor:** {maior_setor}

        **Responsável com mais documentos:**
        {maior_responsavel}
        """
    )


# ==========================
# SETORES
# ==========================

with aba2:


    st.subheader(
        "Documentos por setor"
    )


    dados = (
        df_filtrado["Setor"]
        .value_counts()
        .reset_index()
    )


    dados.columns=[
        "Setor",
        "Quantidade"
    ]



    fig = px.bar(
        dados,
        x="Setor",
        y="Quantidade",
        text="Quantidade"
    )


    fig.update_layout(
        xaxis_tickangle=-45
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



    st.subheader(
        "📅 Evolução mensal"
    )


    mensal = (
        df_filtrado
        .groupby(
            df_filtrado["Data_Criacao"]
            .dt.to_period("M")
            .astype(str)
        )
        .size()
        .reset_index()
    )


    mensal.columns=[
        "Mês",
        "Quantidade"
    ]



    fig2 = px.line(
        mensal,
        x="Mês",
        y="Quantidade",
        markers=True
    )


    st.plotly_chart(
        fig2,
        use_container_width=True
    )



# ==========================
# STATUS
# ==========================

with aba3:


    st.subheader(
        "Distribuição dos status"
    )


    dados = (
        df_filtrado["Status"]
        .value_counts()
        .reset_index()
    )


    dados.columns=[
        "Status",
        "Quantidade"
    ]


    fig = px.pie(
        dados,
        names="Status",
        values="Quantidade",
        hole=0.4
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



# ==========================
# TIPOS
# ==========================

with aba4:


    st.subheader(
        "Tipos de documentos"
    )


    dados = (
        df_filtrado["Tipo_Documento"]
        .value_counts()
        .reset_index()
    )


    dados.columns=[
        "Tipo",
        "Quantidade"
    ]


    fig = px.bar(
        dados,
        x="Tipo",
        y="Quantidade",
        text="Quantidade"
    )


    fig.update_layout(
        xaxis_tickangle=-45
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



# ==========================
# RESPONSÁVEIS
# ==========================

with aba5:


    st.subheader(
        "Documentos por responsável"
    )


    dados = (
        df_filtrado["Responsavel"]
        .value_counts()
        .reset_index()
    )


    dados.columns=[
        "Responsável",
        "Quantidade"
    ]



    fig = px.bar(
        dados,
        x="Responsável",
        y="Quantidade",
        text="Quantidade"
    )


    fig.update_layout(
        xaxis_tickangle=-45
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



# ==========================
# DADOS
# ==========================

with aba6:


    st.subheader(
        "Base documental"
    )


    st.dataframe(
        df_filtrado,
        use_container_width=True
    )