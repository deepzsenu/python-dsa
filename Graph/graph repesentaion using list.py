def addEdge(adj, u, v):
    #undirected graph
    adj[u].append(v)
    adj[v].append(u)
    
def printGraph(adj):
    for e in adj:
        print(e)
        
        
from  collections import deque
# for cyclic and connected undirected graph        
def bfsVersionOne(adj, s):
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
    
def bfs(adj, s, visited):
    
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
                
                
# for disconnected graphs
def Bfsin(adj):
    visited = [False]*len(adj)
    for u in range(len(adj)):
        if visited[u] == False:
            bfs(adj,u,visited)            
    print()
                
            
    
        
v = 4
adj = [[] for i in range(v)]

addEdge(adj,0,1)
addEdge(adj,0,2)
addEdge(adj,1,2)
addEdge(adj,1,3)

printGraph(adj)

bfsVersionOne(adj, 3)
Bfsin(adj)