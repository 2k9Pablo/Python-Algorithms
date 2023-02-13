'''
Prim's MST IMPLEMENTATION - 25 Nov 22
'''

from random import randint

def selectMin(candidates, visited):
    node = None
    weight = float('Inf')

    for n in range(1, len(candidates)):
        if not visited[n] and candidates[n] < weight:
            node = n
            weight = candidates[n]

    return node, weight

def Prim(g):

    n = len(g)
    visited = [False] * n
    initial = randint(1, n-1)
    sol = 0
    candidates = [float('Inf')] * n

    visited[initial] = True

    for src, dst, wei in g[initial]:
        candidates[dst] = wei

    #Empezamos en dos porque el primer nodo visitado ya lo hemos marcado como visto
    for i in range(2, n):
        nextNode, cost = selectMin(candidates, visited)
        if cost < float('Inf'):
            sol += cost
            visited[nextNode] = True

            for src, dst, weight in g[nextNode]:
                if not visited[dst]:
                    candidates[dst] = min(weight, candidates[dst])


    return sol

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #Declaracion del grafo
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