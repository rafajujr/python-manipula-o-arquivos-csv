import csv

linguagem = input("informe o nome da linguagem de programação:\n")
categoria = input("informe a categoria da linguagem de programação:\n")

with open("dados/cursos.csv", "a", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow([linguagem, categoria])