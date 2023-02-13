'''
Kruskal IMPLEMENTATION - 25 Nov 22
'''
from collections import deque


def sortCandidates(g):

    #Creamos un array donde guardar nuestro grafo ordenado
    candidates = []

    #Reestructuramos nuestro grafo para guardar la componente peso en primer lugar,
    # puesto que es desde donde se ordena mediante el sort
    for adj in g:
        for src, dest, weight in g[adj]:
            candidates.append((weight, src, dest))

    candidates.sort()
    return candidates

def updateComponents(componentes, old_id, new_id):
    for i in range(len(componentes)):
        if componentes[i] == old_id:
            componentes[i] = new_id



def Kruskal(g):

    candidates = sortCandidates(g)
    componentes = list(range(len(g)))
    count = len(candidates) - 1

    i = 0
    sol = 0
    while count > 1 and len(candidates)>i:
        (weight, src, dst) = candidates[i]
        if componentes[src] != componentes[dst]:       #Comprobamos que la arista no sea un bucle
            sol += weight
            count -= 1
            updateComponents(componentes, componentes[src], componentes[dst])

if __name__ == '__main__':

    # DECLARACION DEL GRAFO (src, dest, weight)
    g = [
        [],
        [(1, 3, 1), (1, 4, 2), (1, 7, 6)],  # adyacentes del nodo 1.
        [(2, 5, 2), (2, 6, 4), (2, 7, 7)],
        [(3, 1, 1), (3, 4, 3), (3, 7, 5)],
        [(4, 1, 2), (4, 3, 3), (4, 5, 1), (4, 6, 9)],
        [(5, 2, 2), (5, 4, 1), (5, 7, 8)],
        [(6, 2, 4), (6, 4, 9)],
        [(7, 1, 6), [7, 2, 7], (7, 3, 5), (7, 5, 8)]
    ]