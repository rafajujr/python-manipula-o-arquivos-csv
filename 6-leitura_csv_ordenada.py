cursos = []

with open("dados/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        linguagem, categoria = line.rstrip().split(",")
        cursos.append((linguagem, categoria))

for curso in sorted(cursos):
    print(f"{curso[0]} - {curso[1]}")        