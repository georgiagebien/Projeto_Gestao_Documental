import pandas as pd

# carregar dados
df = pd.read_csv("dados/documentos.csv")

# indicadores
total_documentos = len(df)

ativos = len(df[df["Status"] == "Ativo"])

arquivados = len(df[df["Status"] == "Arquivado"])

pendentes = len(df[df["Status"] == "Pendente"])

percentual_arquivados = (arquivados / total_documentos) * 100

print("===== INDICADORES DE GESTÃO DOCUMENTAL =====")

print(f"Total de documentos: {total_documentos}")

print(f"Documentos ativos: {ativos}")

print(f"Documentos arquivados: {arquivados}")

print(f"Documentos pendentes: {pendentes}")

print(f"% arquivados: {percentual_arquivados:.2f}%")

print("\nDocumentos por setor:")
print(df["Setor"].value_counts())