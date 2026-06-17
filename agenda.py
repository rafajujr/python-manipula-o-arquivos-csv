import os

# Função para adicionar um contato
def ass_contact():
    name = input("Digite o nome do contato:\n")
    address = input("Digite o endereço do contato:\n")
    phone = input("Digite o telefone do contato:\n")

    contact = f"{name};{address};{phone}\n"

    with open("dados/contatos.txt", "a", encoding="utf-8") as file:
        file.write(contact)

# Função para visualizar os contatos
def view_contacts():
    if not os.path.exists("dados/contatos.txt"):
        print("Nenhum contato cadastrado.")
        return
    with open("dados/contatos.txt", "r", encoding="utf-8") as file:
        contacts = file.read()
    print("Lista de contatos:")
    print(contacts)

# Função para excluir todos os contatos
def delete_contacts():
    if not os.path.exists("dados/contatos.txt"):
        print("Nenhum contato cadastrado.")
        return
    
    print("Todos os contatos serão exclidos do sistema.")
    sim = input("Deseja excluir todos os contatos? (S/N):\n")
    if sim != "S":
        return
    with open("dados/contatos.txt", "w", encoding="utf-8") as file:
        file.write("")
    
    print("Contato excluido com sucesso.")

# Função para excluir um contato
def delete_contact():
    if not os.path.exists("dados/contatos.txt"):
        print("Nenhum contato cadastrado.")
        return
    name = input("Digite o nome do contato que deseja excluir:\n")
    if name not in open("dados/contatos.txt", "r", encoding="utf-8").read():
        print("Contato nao encontrado.")
        return
    with open("dados/contatos.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    with open("dados/contatos.txt", "w", encoding="utf-8") as file:
        for line in lines:
            if name not in line:
                file.write(line)
    print("Contato excluido com sucesso.")