Dado un grafo *conexo y ponderado*, el algotimo de **Dijkstra** encuentra el camino mínimo para recorrer todos los vértices

```ad-info
El algoritmo de *Dijkstra* es bastante similar en muchos aspectos al *Prim's MST*
```

#### CONSIDERACIONES
- Crearemos un *set* que recogerá los vértices incluidos en el *shortest path tree*
- Daremos una distancia infinita a todos los vértices del grafo
- La distancia al vértice inicial siempre es 0
- Actualizamos la distancia a los vértices durante la exploración

#### PSEUDOCODE

```pseudocode
func DIJKSTRA (graph, root):       
    
	for v ∈ graph.vertex:
	    distancia[v] = INF
	    parent[v] = NULL
        visited[v] = False
    
    distancia[root] = 0
    q = cola()
    q.add(root)
    
    while q:
        v = q.getmin()
        visited[v] = True
        
        for adj in g[v]:
		    if not visited[v]:     
                if distance[adj] > distancia[v] + (v, adj).peso then:
                       distance[adj] = distancia[v] + (v, adj).peso
                       parent[adj] = v
                       q.add(adj)
```

#### ILLUSTRATION

![[270px-Dijkstra_Animation.gif]]

#### IMPLEMENTATION

```python3
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
```
