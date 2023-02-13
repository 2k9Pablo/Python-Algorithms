'''
Dijkstra IMPLEMENTATION - 25 Nov 22

2 Functions:
    - getBestItem -> returns the best item (minimum distance)
    - Dijsktra recursive algo

'''

def getBestItem(distances, visited):

    minDist = float('Inf')
    bestItem = 0

    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < minDist:
            bestItem = i

    return bestItem


def Dijkstra(g, startingNode):

    n = len(g)
    visited = [False] * n
    distances = [float('Inf')] * n

    visited[startingNode] = True
    distances[startingNode] = 0

    #Consideramos la distancia entre dos nodos como el peso de la arista
    for src, dst, wei in g[startingNode]:
        distances[dst] = wei


    for _ in range(2, n):
        nextNode = getBestItem(distances, visited)

        visited[nextNode] = True

        for src, dst, wei in g[nextNode]:
            distances[dst] = min(distances[dst], distances[src] + wei)

    return distances


if __name__ == '__main__':

    #Declaracion del grafo
    g = [

        [],
        [(1, 2, 5), (1, 4, 3)],  # nodo origen, nodo destino, peso
        [(2, 5, 1)],
        [],
        [(4, 2, 1), (4, 3, 11), (4, 5, 6)],
        [(5, 3, 1)]

    ]