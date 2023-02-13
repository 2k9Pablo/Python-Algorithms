**Disjoint-set data structure**
Se define una estructura de datos que lleva el seguimiento de los elementos partidos en dos *sets disjuntos*

```ad-important
Este algotimo se utiliza para encontrar ciclos en *grafos dirigidos* que no contienen *bucles*
```

#### CONSIDERACIONES
- Deberemos crear un *array parent* que tendrá el seguimiento de los subsets
- Atravesar el grafo por todas sus aristas
	- Encontrar a que subset pertenece el nodo *comprobando el padre en el array parent*
	- Si los dos nodos *el nodo y su padre* pertenecen al mismo *subset* encontramos un ciclo
	- En caso contrario, unimos los dos subsets

#### PSEUDOCODE

```pseudocode
func find(parent, node):
	
	if parent[node] == node then:
		return node
	
	else:
		return find_parent(parent, parent[node])

func union(parent, x, y):
	
	parent[x] = y

func Cyclic(graph):
	parent = [-1] * grah.vertex
	
	for i in range(graph.vertex):
		parent[i] = i
	
	for node in graph:
		
		for adj in graph[node]:
			x = find(parent, node)
			y = find(parent, adj)
			
			if x == y then:
				return True
				
			union(parent, x, y)
```

#### PATH COMPRESSION

Encontramos otra implementación de Union-Find el cual comprime el *path hasta el padre* de forma que la complejidad baja de 
	*O(n) -> O(log(n))*

#### ILLUSTRATION

![[UnionFindKruskalDemo.gif]]

#### IMPLEMENTATION UNION-FIND

```python3

```

#### IMPLEMENTATION UNION-FIND RANK COMPRESSION

```python3
```