def getNum(letra):
    return ord(letra)-ord('A')

def getLetra(num):
    return chr(num+ord('A'))


def get_grafo():
    no_nodos = int(input("Ingrese el numero de nodos que tendra el grafo(Se listaran alfabeticamente A,B,C,...Z): "))
    no_vertices = int(input("Ingrese el numero de vertices que tendra el grafo: "))
    grafo = [[False]*no_nodos for x in range(no_nodos)]
    for x in range(no_vertices):
        arista = input("Ingrese los aristas del grafo en el siguiente formato \"A B\", \"D E\": ")
        l1, l2 = arista.split()
        print(l1, l2)
        n1 = getNum(l1)
        n2 = getNum(l2)
        grafo[n1][n2] = True
        grafo[n2][n1] = True
    return grafo

def get_grados(grafo):
    dict_grados = {}
    for row in range(len(grafo)):
        dict_grados[getLetra(row)] = {"grado": 0}
        for col in range(len(grafo)):
            if grafo[row][col]:
                    dict_grados[getLetra(row)]["grado"] += 1
    print(dict_grados)
    for row in range(len(grafo)):
        grado_error = 0
        for col in range(len(grafo)):
            if grafo[row][col]:
                if dict_grados[getLetra(row)]["grado"] <= dict_grados[getLetra(col)]["grado"]:
                    grado_error += 1
        dict_grados[getLetra(row)]["grado_error"]=grado_error+dict_grados[getLetra(row)]["grado"]
    return dict_grados

def get_colores():
    no_colores = int(input("Ingrese el numero de colores para el grafo: "))
    arr_colores = []
    for x in range(no_colores):
        color = input(f"Ingrese el color No {x+1}: ")
        arr_colores.append(color)
    return arr_colores

def asignar_colores(grafo, nodos_ordenados, colores):
    dict_nodos_colores = {}
    dict_nodos_colores[nodos_ordenados[0]]=colores[0]
    curr_color = 1
    print(nodos_ordenados[1:])
    for nodo in nodos_ordenados[1:]:
        index_nodo = getNum(nodo)
        colores_disponibles = colores.copy()
        for nodo_adyacente in range(len(grafo[index_nodo])):
            if grafo[index_nodo][nodo_adyacente]:
                ### Tratar de ir eliminando de las lista los colores de los nodos adyacentes si es que tienen
                if getLetra(nodo_adyacente) in dict_nodos_colores:
                    colores_disponibles.remove(dict_nodos_colores[getLetra(nodo_adyacente)])
        if colores_disponibles!=[]:
            dict_nodos_colores[nodo]=colores_disponibles[0]
        else:
            return "El grafo no se puede colorear con los colores proporcionados"
    return dict_nodos_colores

grafo = get_grafo()
print(grafo)
dict_grados = get_grados(grafo)
print(dict_grados)
nodos_ordenados = sorted(dict_grados, key=lambda k: (dict_grados[k]["grado"], dict_grados[k]["grado_error"]))[::-1]
print(dict_grados)
print(nodos_ordenados)
colores = get_colores()
print(colores)
nodos_coloreados = asignar_colores(grafo, nodos_ordenados, colores)
print(nodos_coloreados)