def addEdge(adj, u, v):
    #undirected graph
    adj[u].append(v)
    adj[v].append(u)
    
def printGraph(adj):
    for e in adj:
        print(e)
        
        
from  collections import deque        
def bsfVersionOne(adj, s):
    visited = [False]*len(adj)
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        s = q.popleft()
        print(s, end = " ")
        for u in adj[s]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True
    print()
                
            
    
        
v = 4
adj = [[] for i in range(v)]

addEdge(adj,0,1)
addEdge(adj,0,2)
addEdge(adj,1,2)
addEdge(adj,1,3)

printGraph(adj)

bsfVersionOne(adj, 3)