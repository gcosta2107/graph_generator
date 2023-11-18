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
            2. Informações dos vértices
            3. Informacoes do grafo
            4. Exibir grafo
            5. Menor custo
            0. Sair
        ''')
    
def print_menu_modo_insercao():
    print('''
            1. Inserir um a um
            2. Inserir em lote
        ''')
    
def print_menu_inserir_elementos():
    print('''
            1. Inserir vertice
            2. Inserir aresta
        ''')

def print_menu_valorado():
    print('''
            1. Aresta Valorada
            2. Aresta Nao valorada
        ''')

def print_menu_info_vertices():
    print('''
            1. Vértices adjacentes de um vértice
            2. Grau de um vértice
            3. Verificar se dois vértices são adjacentes
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
        peso = int(input("Digite o peso: "))

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

def obter_adjacentes(G, vertice):
    try:
        adjacentes = list(G.neighbors(vertice))
        print(f"Vértices adjacentes de {vertice}: {', '.join(adjacentes)}")

        if isinstance(G, nx.DiGraph):  # Se o grafo for direcionado
            adjacentes_entrada = list(G.predecessors(vertice))
            adjacentes_saida = list(G.successors(vertice))
            print(f"Vértices adjacentes de entrada para {vertice}: {', '.join(adjacentes_entrada)}")
            print(f"Vértices adjacentes de saída de {vertice}: {', '.join(adjacentes_saida)}")
    except nx.NetworkXError:
        print(f"O vértice {vertice} não existe no grafo.")

def obter_grau(G, vertice):
    try:
        grau = G.degree(vertice)
        print(f"Grau do vértice {vertice}: {grau}")

        if isinstance(G, nx.DiGraph):  # Se o grafo for direcionado
            grau_entrada = G.in_degree(vertice)
            grau_saida = G.out_degree(vertice)
            print(f"Grau de entrada do vértice {vertice}: {grau_entrada}")
            print(f"Grau de saída do vértice {vertice}: {grau_saida}")
    except nx.NetworkXError:
        print(f"O vértice {vertice} não existe no grafo.")

def sao_adjacentes(G, vertice1, vertice2):
    try:
        adjacentes = G.has_edge(vertice1, vertice2)
        if adjacentes:
            print(f"Os vértices {vertice1} e {vertice2} são adjacentes.")
        else:
            print(f"Os vértices {vertice1} e {vertice2} não são adjacentes.")
    except nx.NetworkXError:
        print(f"Um dos vértices ({vertice1}, {vertice2}) não existe no grafo.")


def calcular_caminho_mais_curto(G, vertice_origem, vertice_destino):
    try:
        caminho, custo = nx.single_source_dijkstra(G, vertice_origem, target=vertice_destino)
        print(f"Caminho mais curto entre {vertice_origem} e {vertice_destino}: {caminho}")
        print(f"Custo do menor caminho: {custo}")
    except nx.NetworkXNoPath:
        print(f"Não há caminho entre {vertice_origem} e {vertice_destino}.")
    except nx.NodeNotFound:
        print(f"Pelo menos um dos vértices ({vertice_origem}, {vertice_destino}) não existe no grafo.")

menus = {'isDirecionado' : print_menu_direcionado, 'menu_principal' : print_menu_app, 'inserir_elemento' : print_menu_inserir_elementos,
        'modo_insercao' : print_menu_modo_insercao, 'isValorado' : print_menu_valorado, 'info_vertice' : print_menu_info_vertices}

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
            menus["info_vertice"]()
            opcao_info_vertices = int(input("Opcao: "))

            if opcao_info_vertices == 1:
                vertice_consulta = input("Digite o vértice para obter os vértices adjacentes: ")
                obter_adjacentes(G, vertice_consulta)

            if opcao_info_vertices == 2:
                vertice_consulta = input("Digite o vértice para obter o grau: ")
                obter_grau(G, vertice_consulta)

            if opcao_info_vertices == 3:
                vertice1 = input("Digite o primeiro vértice: ")
                vertice2 = input("Digite o segundo vértice: ")
                sao_adjacentes(G, vertice1, vertice2)

        if(opcao == 3):
            ordem = G.order()
            print("Ordem do Grafo:", ordem)

            tamanho = G.size()
            print("Tamanho do Grafo:", tamanho)

        if(opcao == 4):
            nx.draw(G, with_labels=True)
            pos = nx.spring_layout(G)
            labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
            plt.show()
        
        if(opcao == 5):
            origem = input("Digite o vértice de origem: ")
            destino = input("Digite o vértice de destino: ")
            calcular_caminho_mais_curto(G, origem, destino)

    print(G.nodes)
    print(G.edges)
