import pandas as pd

#1-Importando os dados
tb_clientes = pd.read_excel("dados/clientes.xlsx", sheet_name="aba4")
print(tb_clientes)

#2-Adicionar coluna de index
tb_clientes = pd.read_excel("dados/clientes.xlsx", index_col=0)
print(tb_clientes)

#3-Importar colunas específicas
tb_clientes = pd.read_excel("dados/clientes.xlsx", usecols=["ID", "Nome"])
print(tb_clientes)

#4-Gerar nova planilha de uma aba
tb_clientes_aba4 = pd.read_excel("dados/clientes.xlsx", sheet_name="aba4")
tb_clientes_aba3 = pd.read_excel("dados/clientes.xlsx", sheet_name="aba3")

with pd.ExcelWriter("dados/nova_planilha.xlsx") as writer:
    tb_clientes_aba4.to_excel(writer, sheet_name="aba4", index=False)
    tb_clientes_aba3.to_excel(writer, sheet_name="aba3", index=False)

