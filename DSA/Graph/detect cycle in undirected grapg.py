"""6. Detect cycle in a directed graph 
Medium Accuracy: 30.19 Submissions: 100k+ Points: 4
Lamp
This problem is part of GFG SDE Sheet. Click here to view more.   
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.


Example 1:

Input:



Output: 1
Explanation: 3 -> 3 is a cycle

Example 2:

Input:


Output: 0
Explanation: no cycle in the graph

Your task:
You dont need to read input or print anything. Your task is to complete the function isCyclic() which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns a boolean value denoting if the given directed graph contains a cycle or not.


Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)"""


#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def dfs(self,i,visited,dfsv,V,adj):
        visited[i] = 1
        dfsv[i] = 1
        for j in adj[i]:
            if visited[j] == 0: #not visited
                if self.dfs(j,visited,dfsv,V,adj):
                    return True
            elif dfsv[j]==1: #i.e, both visited and dfsv are visited
                return True
                    
        dfsv[i] = 0
        return False
    def isCyclic(self, V, adj):
        visited = [0 for _ in range(V)]
        dfsv = [0 for _ in range(V)] #dfs visited
        for i in range(V):
            if visited[i] == 0:
                if self.dfs(i,visited,dfsv,V,adj):
                    return True
        return False
