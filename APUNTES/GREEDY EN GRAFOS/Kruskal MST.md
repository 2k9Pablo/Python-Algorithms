El algoritmo de Kruskal se utiliza cuando el grafo es *conexo* y tiene las aristas *ponderadas*  (con pesos)

```ad-warning
Poco eficiente sobre grafos densos
```

#### CONSIDERACIONES
- Deberemos *ordenar las aristas de forma decreciente*
- Añadiremos la arista siempre que no se forme un ciclo
- Deberemos tener *vértices - 1* aristas para completar el MST

#### PSEUDOCODE

```pseudocode
func Kruskal(graph):
    F:= ∅
    for each v ∈ graph.vertex do
        MAKE-SET(v)
    
    for each (u, v) in graph.edges ordered by weight(u, v), increasing do
        
        if FIND-SET(u) ≠ FIND-SET(v) then
            F:= F ∪ {(u, v)} ∪ {(v, u)}
            UNION(FIND-SET(u), FIND-SET(v))
    
    return F
```

#### ILLUSTRATION

![[KruskalDemo.gif]]

#### IMPLEMENTATION

```python3
from collections import deque  
  
def sortCandidates(g):  
    
    #Creamos un array donde guardar nuestro grafo ordenado  
    candidates = []  
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
    
    return sol
```

