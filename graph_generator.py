import networkx as nx
import matplotlib.pyplot as plt

def print_menu_direcionado():
    print('''
            1. Grafo direcionado
            2. Grafo não-direcionado
            0. Sair
        ''')
    
def print_menu_app():
    print('''
            1. Inserir um a um [VERTICES/ARESTAS]
            2. Inserir em lote
            3. Exibir grafo
            4. Informacoes do grafo
            0. Sair
        ''')
    
def print_menu_1a1():
    print('''
            1. Inserir vertice
            2. Inserir aresta
            0. Sair
        ''')
    
def print_menu_insercao():
    print('''
            1. Inserir um a um
            2. Inserir em lote
        ''')

def print_menu_valorado():
    print('''
            1. Grafo Valorado
            2. Grafo Nao valorado
        ''')
    
def isDirecionado(direcionado):
    if(direcionado == 1):
        return nx.DiGraph()
    elif(direcionado == 2):
        return nx.Graph()
    elif(direcionado == 0):
        print("Saindo...")
        exit(0)
    else:
        print("Opção inválida...Saindo...")

def inserir_vertice(G):
    vertice = ""

    while True:
        vertice = input("Digite o vertice [Para parar de inserir digite: sair]: ")

        if(vertice == "sair"):
            break
        else:
            G.add_node(vertice)

def inserir_aresta_nao_valorada(G):
    while True:
        aresta1 = input("Digite o vertice inicial: ")    
        aresta2 = input("Digite o vertice final: ")
    
        G.add_edge(aresta1, aresta2)

        validator_aresta = input("Deseja adicionar mais arestas? [s/n]")

        if(validator_aresta == 'n'):
            break

def inserir_aresta_valorada(G):
    while True:
        aresta1 = input("Digite o vertice inicial: ")    
        aresta2 = input("Digite o vertice final: ")
        peso = input("Digite o peso: ")

        weighted_edges = [(aresta1, aresta2, peso)]
        G.add_weighted_edges_from(weighted_edges)
    
        G.add_edge(aresta1, aresta2, weight = peso)

        validator_aresta = input("Deseja adicionar mais arestas? [s/n]")

        if(validator_aresta == 'n'):
            break

def inserir_1a1(G, opcao_1a1, modo_valorado):
    if(opcao_1a1 == 1):
        inserir_vertice(G)

    elif(opcao_1a1 == 2):
        if modo_valorado == 1:
            inserir_aresta_valorada(G)
        
        if modo_valorado == 2:
            inserir_aresta_nao_valorada(G)

# def sao_adjacentes(grafo, vertice1, vertice2):
#     return grafo.has_edge(vertice1, vertice2)

menus = {'direcionado' : print_menu_direcionado, 'app' : print_menu_app, '1a1' : print_menu_1a1,
        'insercao' : print_menu_insercao, 'valorado' : print_menu_valorado}

menus["direcionado"]()
modo_direcionado = int(input("Opcao: "))

menus["insercao"]()
modo_insercao = int(input("Opcao: "))

menus["valorado"]()
modo_valorado = int(input("Opcao: "))

G = isDirecionado(modo_direcionado)

opcao = 999

while opcao != 0:
    
    menus["app"]()

    opcao = int(input("Opcao: "))

    if(opcao == 0):
        print("Encerrando Aplicacao....")

    if(opcao == 1):
        menus["1a1"]()

        opcao_1a1 = int(input("Opcao: "))

        inserir_1a1(G, opcao_1a1, modo_valorado)     

    if(opcao == 2):
        continue

    if(opcao == 3):
        nx.draw(G, with_labels=True)
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    if(opcao == 4):
        ordem = G.order()
        print("Ordem do Grafo:", ordem)

        tamanho = G.size()
        print("Tamanho do Grafo:", tamanho)

print(G.nodes)
print(G.edges)
