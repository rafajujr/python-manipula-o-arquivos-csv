name = input("Digite o nome do aluno:\n")

"""
Arquivos - Mode de Operação:

1-> Modo W - Write
2-> Modo A - Append
3-> Modo R - Read
"""

# Implementação
file = open("dados/names.txt", "a", encoding="utf-8")
file.write(f"{name}\n")
file.close()

# Implementação 2
with open("dados/names.txt", "a", encoding="utf-8") as file:
    file.write(f"{name}\n")

