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
        dict_grados[getLetra(row)] = 0
        for col in range(len(grafo)):
            if grafo[row][col]:
                    dict_grados[getLetra(row)] += 1
    return dict_grados

grafo = get_grafo()
print(grafo)
dict_grados = get_grados(grafo)
print(dict_grados)