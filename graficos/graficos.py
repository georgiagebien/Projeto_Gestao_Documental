import pandas as pd
import matplotlib.pyplot as plt
import os

# carregar dados
df = pd.read_csv("dados/documentos.csv")

# criar pasta de gráficos
os.makedirs("graficos", exist_ok=True)

# Gráfico 1 - documentos por tipo
df["Tipo_Documento"].value_counts().plot(kind="bar")

plt.title("Quantidade de documentos por tipo")
plt.xlabel("Tipo de documento")
plt.ylabel("Quantidade")

plt.tight_layout()
plt.savefig("graficos/documentos_por_tipo.png")

plt.show()


# Gráfico 2 - documentos por setor
df["Setor"].value_counts().plot(kind="bar")

plt.title("Quantidade de documentos por setor")
plt.xlabel("Setor")
plt.ylabel("Quantidade")

plt.tight_layout()
plt.savefig("graficos/documentos_por_setor.png")

plt.show()


# Gráfico 3 - status dos documentos
df["Status"].value_counts().plot(kind="pie", autopct="%1.1f%%")

plt.title("Status dos documentos")

plt.ylabel("")
plt.tight_layout()
plt.savefig("graficos/status_documentos.png")

plt.show()