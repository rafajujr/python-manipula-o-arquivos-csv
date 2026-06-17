import pickle

class Cliente:
    def __init__(self, id, nome, idade, cidade):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Idade: {self.idade} anos, Cidade: {self.cidade}"
    
clientes = [
    Cliente(1, "Ana", 10, "São Paulo"),
    Cliente(2, "Bia", 20, "Rio de Janeiro"),
    Cliente(3, "Carlos", 30, "Salvador"),
    Cliente(4, "Davi", 40, "Belo Horizonte"),
    Cliente(5, "Eva", 50, "Fortaleza")
]

# Salvar lista de clinetes em arquivo pickle
with open("dados/clientes.pkl", "wb") as file:
    pickle.dump(clientes, file)

# Carregando os dados do arquivo pickle
with open("dados/clientes.pkl", "rb") as file:
    clientes = pickle.load(file)

for cliente in clientes:
    print(cliente)

# Adicionar um cliente
novo_cliente = Cliente(6, "Fernanda", 25, "Curitiba")
clientes.append(novo_cliente)

# Salvar a lista atualizada
with open("dados/clientes.pkl", "wb") as file:
    pickle.dump(clientes, file)
    print("Lista atualizada salva com sucesso.")

# Carregando os dados do arquivo pickle
with open("dados/clientes.pkl", "rb") as file:
    clientes = pickle.load(file)

for cliente in clientes:
    print(cliente)