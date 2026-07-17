import pandas as pd
import random
from datetime import datetime, timedelta
import os

# criar pasta dados se não existir
os.makedirs("dados", exist_ok=True)

# gerar dados de documentos
tipos = ["Contrato", "Relatório", "Nota Fiscal", "Processo", "Ofício"]
setores = ["RH", "Financeiro", "Jurídico", "TI", "Administrativo"]

dados = []

for i in range(100):
    documento = {
        "ID": i + 1,
        "Tipo_Documento": random.choice(tipos),
        "Setor": random.choice(setores),
        "Data_Criacao": datetime.now() - timedelta(days=random.randint(1, 1000)),
        "Responsavel": f"Pessoa {random.randint(1,20)}",
        "Status": random.choice(["Ativo", "Arquivado", "Pendente"])
    }
    dados.append(documento)

df = pd.DataFrame(dados)

# salvar arquivo
df.to_csv("dados/documentos.csv", index=False, encoding="utf-8")

print("Dados gerados com sucesso!")