cursos = []

with open("dados/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        linguagem, categoria = line.rstrip().split(",")
        curso = {}

        curso["linguagem"] = linguagem
        curso["categoria"] = categoria

        cursos.append(curso)

# Ordenação com base em uma função relacionada ao key

def get_language(course):
    return course["linguagem"]

def get_category(course):
    return course["categoria"]

for curso in sorted(cursos, key=get_category):
    print(f"{curso['linguagem']} - {curso['categoria']}")