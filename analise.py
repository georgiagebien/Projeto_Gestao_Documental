import pandas as pd

# carregar dados
df = pd.read_csv("dados/documentos.csv")

# visualizar primeiros registros
print("\nPrimeiros dados:")
print(df.head())

# informações do arquivo
print("\nInformações:")
print(df.info())

# quantidade de documentos por tipo
print("\nTipos de documentos:")
print(df["Tipo_Documento"].value_counts())

# documentos por setor
print("\nDocumentos por setor:")
print(df["Setor"].value_counts())

# status dos documentos
print("\nStatus:")
print(df["Status"].value_counts())