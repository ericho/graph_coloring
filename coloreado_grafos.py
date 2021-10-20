def getNum(letra):
    return ord(letra)-ord('A')

def getLetra(num):
    return chr(num+ord('A'))

def crear_grafo(no_nodos, aristas):

    G = nx.Graph()
    G.add_nodes_from(list(range(no_nodos)))
    G.add_edges_from(aristas)

    graph = [[None]*no_nodos for x in range(no_nodos)]
    for edge in aristas:
        graph[edge[0]][edge[1]] = True
        graph[edge[1]][edge[0]] = True
    
    return graph, G

def get_grados(grafo):
    dict_grados = {}
    for row in range(len(grafo)):
        dict_grados[getLetra(row)] = {"grado": 0}
        for col in range(len(grafo)):
            if grafo[row][col]:
                    dict_grados[getLetra(row)]["grado"] += 1
    for row in range(len(grafo)):
        grado_error = 0
        for col in range(len(grafo)):
            if grafo[row][col]:
                if dict_grados[getLetra(row)]["grado"] <= dict_grados[getLetra(col)]["grado"]:
                    grado_error += 1
        dict_grados[getLetra(row)]["grado_error"]=grado_error+dict_grados[getLetra(row)]["grado"]
    return dict_grados


def asignar_colores(grafo, nodos_ordenados, colores):
    dict_nodos_colores = {}
    dict_nodos_colores[nodos_ordenados[0]]=colores[0]
    for nodo in nodos_ordenados[1:]:
        index_nodo = getNum(nodo)
        colores_disponibles = colores.copy()
        for nodo_adyacente in range(len(grafo[index_nodo])):
            if grafo[index_nodo][nodo_adyacente]:
                ### Tratar de ir eliminando de las lista los colores de los nodos adyacentes si es que tienen
                if getLetra(nodo_adyacente) in dict_nodos_colores:
                    try:
                        colores_disponibles.remove(dict_nodos_colores[getLetra(nodo_adyacente)])
                    except Exception:
                        pass

        if colores_disponibles!=[]:
            dict_nodos_colores[nodo]=colores_disponibles[0]
        else:
            print("El grafo no se puede colorear con los colores proporcionados")
            break
    
    return dict_nodos_colores

def colores_a_lista(colores, graph_size):
    colores_list = ["gray"] * graph_size
    for c in colores:
        idx = ord(c)-ord('A')
        colores_list[idx] = colores[c]

    return colores_list

def graficar_grafo(G, colores, output_file):
    colores = colores_a_lista(colores, len(G))
    labels = {}
    for node in G:
        labels[node] = getLetra(node)
    _fig = plt.figure(figsize=(5, 5))
    pos = nx.spring_layout(G, seed=3)
    elabels = nx.get_edge_attributes(G,'weight')
    nx.draw(G, with_labels=True, node_color=colores, pos=pos, labels=labels)
    nx.draw_networkx_edge_labels(G, pos,  edge_labels=elabels)
    plt.savefig(output_file)

if __name__ == '__main__':

    import networkx as nx
    import matplotlib.pyplot as plt

    
    inputs = input()
    inputs = list(map(lambda x: int(x), inputs.split()))

    num_nodes = inputs[0]
    num_edges = inputs[1]
    num_colores = inputs[2]

    edges = []

    for i in range(num_edges):
        edge_def = input().rstrip().split()
        n1 = ord(edge_def[0]) - ord('A')
        n2 = ord(edge_def[1]) - ord('A')
       
        edges.append([n1, n2])

    colores = []
    for _ in range(num_colores):
        color_temp = input()
        colores.append(color_temp)

    output_file = input()

    grafo, G = crear_grafo(num_nodes, edges)

    dict_grados = get_grados(grafo)

    nodos_ordenados = sorted(dict_grados, \
        key=lambda k: (dict_grados[k]["grado"] * -1, dict_grados[k]["grado_error"] * -1))

    nodos_coloreados = asignar_colores(grafo, nodos_ordenados, colores)
    graficar_grafo(G, nodos_coloreados, output_file)
    print(nodos_coloreados)
    
