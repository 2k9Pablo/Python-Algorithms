'''
CutNodes / Articulation Points
'''
def APUtil(g, v, visited, ap, parent, low, disc, time):

    children = 0
    visited[v] = True

    disc[v] = time
    low[v] = time
    time += 1

    for adj in g[v]:
        if not visited[adj]:

            parent[adj] = v
            children += 1
            APUtil(g, adj, visited, ap, parent, low, disc, time)

            #Actualizamos componentes
            low[v] = min(low[v], low[adj])

            if parent[v] == -1 and children > 1:
                ap[v] = True

            if parent[v] != -1 and low[adj] >= disc[v]:
                ap[v] = True

        elif adj != parent[v]:
            low[v] = min(low[v], disc[adj])

def AP(g):

    n = len(g)

    visited = [False] * n
    ap = [False] * n
    disc = [float('inf')] * n
    low = [float('inf')] * n
    parent = [-1] * n

    time = 0

    for i in range(n):
        if not visited[i]:
            APUtil(g, i, visited, ap, parent, low, disc, time)

    return ap