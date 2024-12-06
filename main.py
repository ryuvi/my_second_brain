import os
from pyvis.network import Network

# Caminho para a pasta "second_brain"
base_path = "second_brain"

# Função para construir a estrutura de dados
def build_structure(base_path):
    structure = {"name": "second_brain", "children": []}

    for category in os.listdir(base_path):
        category_path = os.path.join(base_path, category)
        if os.path.isdir(category_path):
            category_data = {"name": category, "children": []}

            for subcategory in os.listdir(category_path):
                subcategory_path = os.path.join(category_path, subcategory)
                if os.path.isdir(subcategory_path):
                    subcategory_data = {"name": subcategory, "children": []}

                    for file in os.listdir(subcategory_path):
                        if file.endswith(".md"):  # Apenas arquivos Markdown
                            subcategory_data["children"].append({"name": file})

                    category_data["children"].append(subcategory_data)

            structure["children"].append(category_data)

    return structure

# Função para gerar a visualização
def build_network(structure):
    net = Network(height="800px", width="100%", directed=False)

    # Adiciona a pasta base
    net.add_node(structure["name"], label=structure["name"], size=40, color="red")

    def add_children(parent_name, children, size, color):
        for child in children:
            net.add_node(child["name"], label=child["name"], size=size, color=color)
            net.add_edge(parent_name, child["name"])
            if "children" in child:
                add_children(child["name"], child["children"], size - 5, color="blue")

    add_children(structure["name"], structure["children"], 30, "green")
    return net

# Construção da estrutura
structure = build_structure(base_path)

# Geração da rede e salvamento como HTML
net = build_network(structure)
net.show("docs/second_brain_network.html", notebook=False)

print("Arquivo 'second_brain_network.html' criado com sucesso!")

