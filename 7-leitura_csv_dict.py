cursos = []

with open("dados/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        linguagem, categoria = line.rstrip().split(",")
        curso = {}

        curso["linguagem"] = linguagem
        curso["categoria"] = categoria

        cursos.append(curso)

for curso in cursos:
    print(f"{curso['linguagem']} - {curso['categoria']}")