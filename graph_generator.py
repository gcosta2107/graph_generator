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
            1. Inserir elementos [VERTICES/ARESTAS]
            2. ----------------
            3. Exibir grafo
            4. Informacoes do grafo
            0. Sair
        ''')
    
def print_menu_inserir_elementos():
    print('''
            1. Inserir vertice
            2. Inserir aresta
        ''')
    
def print_menu_modo_insercao():
    print('''
            1. Inserir um a um
            2. Inserir em lote
        ''')

def print_menu_valorado():
    print('''
            1. Aresta Valorada
            2. Aresta Nao valorada
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

def inserir_elemento(G, opcao_1a1, modo_valorado):
    if(opcao_1a1 == 1):
        inserir_vertice(G)

    if(opcao_1a1 == 2):
        if modo_valorado == 1:
            inserir_aresta_valorada(G)
        
        if modo_valorado == 2:
            inserir_aresta_nao_valorada(G)
    

def inserir_em_lote(G, modo_valorado, arquivo):
    try:
        with open(arquivo, 'r') as file:
            for line in file:
                dados = line.strip().split()

                if len(dados) < 2:
                    print("Formato inválido na linha:", line)
                else:
                    vertice1, vertice2 = dados[0], dados[1]

                    if len(dados) == 3:
                        modo_valorado == 2 
                        peso = dados[2]
                        G.add_edge(vertice1, vertice2, weight=peso)
                    else:
                        G.add_edge(vertice1, vertice2)

        print("Inserção em lote concluída.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print("Ocorreu um erro durante a leitura do arquivo:", e)

# def sao_adjacentes(grafo, vertice1, vertice2):
#     return grafo.has_edge(vertice1, vertice2)

menus = {'isDirecionado' : print_menu_direcionado, 'menu_principal' : print_menu_app, 'inserir_elemento' : print_menu_inserir_elementos,
        'modo_insercao' : print_menu_modo_insercao, 'isValorado' : print_menu_valorado}

if __name__ == "__main__":
    menus["isDirecionado"]()
    modo_direcionado = int(input("Opcao: "))

    G = isDirecionado(modo_direcionado)

    opcao = 999

    modo_valorado = 0

    while opcao != 0:
        
        menus["menu_principal"]()

        opcao = int(input("Opcao: "))

        if(opcao == 0):
            print("Encerrando Aplicacao....")

        if(opcao == 1):
            menus["modo_insercao"]()
            modo_insercao = int(input("Opcao: "))

            if modo_insercao == 1:
                menus["inserir_elemento"]()
                opcao_elemento = int(input("Opcao: "))

                if opcao_elemento == 1:
                    modo_valorado = 0

                if opcao_elemento == 2:
                    menus["isValorado"]()
                    modo_valorado = int(input("Opcao: "))

                inserir_elemento(G, opcao_elemento, modo_valorado)

            if modo_insercao == 2:
                print("ATENÇÃO!!! O ARQUIVO DEVE ESTAR NO FORMATO (VERTICE1 VERTICE2 PESO (se for o caso))")
                arquivo = input("Digite o nome do arquivo: ")
                inserir_em_lote(G, modo_valorado, arquivo)

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