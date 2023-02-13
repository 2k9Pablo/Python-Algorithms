El algoritmo de Prim se utiliza sobre grafos *no dirigidos*, *conexos* y *ponderados*

```ad-warning
Siempre que podamos, deberemos elegir Prim's MST sobre Kruskal MST
```

La principal diferencia es que Prim se fija en que hayamos recorrido todos los nodos, en lugar de todas las aristas.

Por ello, será más eficiente en grafos **densos**

#### CONSIDERACIONES

- Crear un *set* que recoge los *vértices ya visitados*
- Inicializar todos los vértices con valor "infinito"
- Actualizar la distancia a los vértices durante la explotación
- Guarda el vértice con menor valor que no encontremos en el *set*

#### PSEUDOCODE

```pseudocode
func Prim(G, w, s):
	for each v in V
		color(v) <- WHITE
		key(v) <- infinity
		p(v) <- NIL
	
	Q <- empty list // Q keyed by key[v]
	color(s) <- GRAY
	Insert(Q, s)
	key(s) <- 0
	
	while Q != empty
		u <- Extract-Min(Q)
		for v in Adj[u]
			if color(v) = WHITE
				then color(v) <- GRAY
					Insert(Q,v)
					key(v) <- w(u,v)
					p(v) <- u
			elseif color(v) = GRAY
				then if key(v) > w(u,v)
					then key(v) <- w(u,v)
						p(v) <- u
		color(v) <- BLACK
	
	return(p)
```

#### ILLUSTRATION

![[PrimAlgDemo.gif]]

#### IMPLEMENTATION

```python3
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
```
