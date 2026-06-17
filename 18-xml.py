import xml.etree.ElementTree as ET

dados = """<?xml version="1.0" encoding="utf-8"?>
<clientes>
    <cliente>
        <id>1</id>
        <nome>Carlos</nome>
        <idade>30</idade>
        <cidade>Salvador</cidade>
    </cliente>
    <cliente>
        <id>2</id>
        <nome>Helena</nome>
        <idade>25</idade>
        <cidade>Sao Paulo</cidade>
    </cliente>
</clientes>
"""

caminho_arquivo = "dados/clientes.xml"

# 1-Exportando dados para xml
with open(caminho_arquivo,"w", encoding="utf-8") as file:
    file.write(dados)

# 2-Lendo dados do xml
tree = ET.parse(caminho_arquivo)
root = tree.getroot()

for cliente in root:
    id = cliente.find("id").text
    nome = cliente.find("nome").text
    idade = cliente.find("idade").text
    cidade = cliente.find("cidade").text

    print(f"ID: {id}, Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

# 3-Adicionar novo cliente
novo_cliente = ET.Element("cliente")
novo_id = ET.SubElement(novo_cliente, "id")
novo_id.text = "6"
novo_nome = ET.SubElement(novo_cliente, "nome")
novo_nome.text = "Fernanda"
novo_idade = ET.SubElement(novo_cliente, "idade")
novo_idade.text = "25"
novo_cidade = ET.SubElement(novo_cliente, "cidade")
novo_cidade.text = "Curitiba"

root.append(novo_cliente)

tree.write(caminho_arquivo, encoding="utf-8", xml_declaration=True)