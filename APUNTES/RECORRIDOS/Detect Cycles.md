Un ciclo se produce cuando durante un mismo recorrido, encontramos un *backedge* o arista de retorno a un nodo por el que ya hemos pasado.

Para detectar ciclos en grafos, realizaremos un DFS del mismo comprobando los *backedges*

#### PSEUDOCODE

```pseudo
func isCyclic(graph):
	
	visited = False * len(graph)
	reckstack = False * len(graph)
	
	for i < len(graph):
		if not visited[i] then:
			if isCyclicUtil(graph, i, visited, reckstack) then:
				return True
	return False

func isCyclicUtil(graph, node, visited, reckstack):
	
	visited[node] = True
	reckstack[node] = True
	
	for i in graph[node]:
		if not visited[i] then:
			if isCyclicUtil(graph, node, visited, reckstak) then:
				return True
		elif reckstack[i] == True then:
			return True
	
	reckstack[node] = False
	return False
```

#### ILLUSTRATION

![[DFS_finding_cycle.gif]]

#### CONSIDERACIONES
Deberemos mantener:
- *Array visited* con los nodos visitados
- *ReckStack* que marca los nodos visitados durante esa recursión
- Encontraremos un ciclo cuando el *reckstack* de los adyacentes al nodo en el que nos encontremos == 1, puesto que ya habremos pasado por ellos

#### IMPLEMENTATION DIRECTED GRAPH

```python3
def isCyclicUtil(g, v, visited, reckstack):
    visited[v] = True
    reckstack[v] = True
    
    for adj in g[v]:
        
        if not visited[adj]:
            if isCyclicUtil(g, adj, visited, reckstack):
                return True
        
        elif reckstack[adj]:
            return True
    
    reckstack[v] = False
    return False

def isCyclic(g):
    n = len(g)
    visited = [False] * n
    reckstack = [False] * n
    for i in range(n):
        if not visited[i]:
            if isCyclicUtil(g, i, visited, reckstack):
                return True
    
    return False
```

####  IMPLEMENTATION UNDIRECTED GRAPH

```phython3
def isCyclicUtil(g, v, visited, parent):
    visited[v] = True
    
    for adj in g[v]:
        
        if not visited[adj]:
            if isCyclicUtil(g, adj, visited, v):
                return True
        
        elif parent != adj:
            return True
    
    return False

def isCyclic(g):
    n = len(g)
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            if isCyclicUtil(g, i, visited, -1):
                return True
    
    return False
```
