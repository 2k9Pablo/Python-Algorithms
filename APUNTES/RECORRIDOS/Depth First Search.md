La idea de este algoritmo es profundizar en los nodos adyacentes antes de visitarlos todos

#### PSEUDO

```pseudocode
DFS(_G_, _v_) is
    label _v_ as discovered
	for all directed edges from _v_ to _w that are_ in _G_.adjacentEdges(_v_) do
        if vertex _w_ is not labeled as discovered then
            recursively call DFS(_G_, _w_)

procedure DFS_iterative(G, v) is
    let S be a stack
    S.push(v)
    while S is not empty do
        v = S.pop()
        if v is not labeled as discovered then
            label v as discovered
            for all edges from v to w in G.adjacentEdges(v) do 
                S.push(w)
```

#### ILLUSTRATION

![[ezgif.com-gif-maker7.gif]]

#### IMPLEMENTATION

```python3
'''
Depth Firt Search
'''

def DFSUtil(g, visited, v):
    
    visited[v] = True
    for adj in g[v]:
        if not visited[adj]:
            DFSUtil(g, visited, adj)


def DFS(g):
    
    n = len(g)
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            DFSUtil(g, visited, i)
```

