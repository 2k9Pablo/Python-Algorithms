La idea de este algoritmo es visitar en primer lugar los adyacentes al nodo en el que nos encontramos, antes de profundizar en estos.

#### PSEUDO

```pseudo-code
Breadth_First_Serach(Graph, X) 

#Let Q be the queue  
Q.enqueue(X) 

While (Q is not empty)  
	Y = Q.dequeue( ) 
	For all the neighbors Z of Y  
		If Z is not visited, 
			Q. enqueue( Z ) 
			Mark Z as visited
```

#### ILLUSTRATION

![[1.png]]
![[2.png]]![[3.png]]![[4.png]]![[5.png]]![[6.png]]![[7.png]]
#### IMPLEMENTATION

```python3
'''  
Breath-First-Search  
'''  
from collections import deque  
  
def BFSUtil(g, visited, v):  
  
    q = deque()  
    visited[v] = True  
    q.append(v)  
      
    while q:  
        node = q.popleft()  
        for adj in g[node]:  
            if not visited[adj]:  
                q.append(adj)  
                visited[adj] = True  
  
  
def BFS(g):  
    n = len(g)  
    visited = [False] * n  
    for i in range(n):  
        if not visited[i]:  
            BFSUtil(g, visited, i)
```
