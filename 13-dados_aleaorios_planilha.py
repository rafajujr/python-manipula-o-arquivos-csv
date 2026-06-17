import pandas as pd
import numpy as np

dados_aba1 = {
    "ID": [1, 2, 3, 4, 5],
    "Nome": ["Ana", "Bia", "Carlos", "Davi", "Eva"],
    "Idade": [10, 20, 30, 40, 50],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Salvador", "Belo Horizonte", "Fortaleza"]
}

dados_aba2 = {
    "ID": [6, 7, 8, 9, 10],
    "Nome": ["Fernanda", "Gustavo", "Helena", "Isabella", "Joaquim"],
    "Idade": [15, 25, 35, 45, 55],
    "Cidade": ["Curitiba", "Florianopolis", "Goiania", "Porto Alegre", "Sao Paulo"]
}

dados_aba3 = {
    "ID": [11, 12, 13, 14, 15],
    "Nome": ["Lucas", "Matheus", "Nathan", "Rafael", "Thiago"],
    "Idade": [15, 25, 35, 45, 55],
    "Cidade": ["Curitiba", "Florianopolis", "Goiania", "Porto Alegre", "Sao Paulo"]
}

dados_aba4 = {
    "ID": [16, 17, 18, 19, 20],
    "Nome": ["Lucas", "Matheus", "Nathan", "Rafael", "Thiago"],
    "Idade": [15, 25, 35, 45, 55],
    "Cidade": ["Curitiba", "Florianopolis", "Goiania", "Porto Alegre", "Sao Paulo"]
}

df_aba1 = pd.DataFrame(dados_aba1)
df_aba2 = pd.DataFrame(dados_aba2)
df_aba3 = pd.DataFrame(dados_aba3)
df_aba4 = pd.DataFrame(dados_aba4)

caminho_arquivo = "dados/clientes.xlsx"

with pd.ExcelWriter(caminho_arquivo, engine="openpyxl") as writer:
    df_aba1.to_excel(writer, sheet_name="aba1", index=False)
    df_aba2.to_excel(writer, sheet_name="aba2", index=False)
    df_aba3.to_excel(writer, sheet_name="aba3", index=False)
    df_aba4.to_excel(writer, sheet_name="aba4", index=False)

print(f"Arquivo excel com 4 abas criados em {caminho_arquivo}")