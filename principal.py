from agenda import ass_contact, view_contacts, delete_contacts, delete_contact

def main():
    while True:
        print("Agenda de Contatos")
        print("1 - Adicionar contato")
        print("2 - Visualizar contatos")
        print("3 - Excluir contato")
        print("4 - Excluir todos os contatos")
        print("5 - Sair")

        option = input("Digite a opção desejada:\n")

        if option == "1":
            ass_contact()
        elif option == "2":
            view_contacts()
        elif option == "3":
            delete_contact()
        elif option == "4":
            delete_contacts()
        elif option == "5":
            break

if __name__ == "__main__":
    main()