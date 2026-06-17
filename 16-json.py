import json

dados = {
    "clientes":[
        {
            "id": 1,
            "nome": "Ana",
            "idade": 10,
            "cidade": "São Paulo"
        },
        {
            "id": 2,
            "nome": "Bia",
            "idade": 20,
            "cidade": "Rio de Janeiro"
        },
        {
            "id": 3,
            "nome": "Carlos",
            "idade": 30,
            "cidade": "Salvador"
        },
        {
            "id": 4,
            "nome": "Davi",
            "idade": 40,
            "cidade": "Belo Horizonte"
        },
        {
            "id": 5,
            "nome": "Eva",
            "idade": 50,
            "cidade": "Fortaleza"
        }
    ]
}

caminho_arquivo = "dados/clientes.json"

# 1-Escrevendo dados em arquivos JSON
with open(caminho_arquivo, "w", encoding="utf-8") as file:
    json.dump(dados, file, indent=4)

# 2-Lendo dados em arquivos JSON
with open(caminho_arquivo, "r", encoding="utf-8") as file:
    dados_lidos = json.load(file)
    print(dados_lidos)

# 3-Manipulando os dados
for cliente in dados_lidos["clientes"]:
    if cliente["idade"] > 30:
        cliente["idade"] -= 10

novo_cliente = {
    "id": 6,
    "nome": "Fernanda",
    "idade": 25,
    "cidade": "Curitiba"
}

dados_lidos["clientes"].append(novo_cliente)

# 4-Atualizando os dados
with open(caminho_arquivo, "w", encoding="utf-8") as file:
    json.dump(dados_lidos, file, indent=4)