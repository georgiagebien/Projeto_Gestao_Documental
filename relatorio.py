import pandas as pd

# carregar dados
df = pd.read_csv("dados/documentos.csv")

# criar resumo
resumo_status = df["Status"].value_counts().reset_index()
resumo_status.columns = ["Status", "Quantidade"]

resumo_setor = df["Setor"].value_counts().reset_index()
resumo_setor.columns = ["Setor", "Quantidade"]

# criar relatório Excel
with pd.ExcelWriter("Relatorio_Gestao_Documental.xlsx") as writer:
    df.to_excel(writer, sheet_name="Documentos", index=False)
    resumo_status.to_excel(writer, sheet_name="Resumo Status", index=False)
    resumo_setor.to_excel(writer, sheet_name="Resumo Setor", index=False)

print("Relatório criado com sucesso!")