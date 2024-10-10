"""5. Detect cycle in an undirected graph 
Medium Accuracy: 35.66% Submissions: 100k+ Points: 4
Lamp
This problem is part of GFG SDE Sheet. Click here to view more.   
Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not. 

Example 1:

Input:   

Output: 1
Explanation: 1->2->3->4->1 is a cycle.
Example 2:

Input: 

Output: 0
Explanation: No cycle in the graph.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function isCycle() which takes V denoting the number of vertices and adjacency list as input parameters and returns a boolean value denoting if the undirected graph contains any cycle or not, return 1 if a cycle is present else return 0.

NOTE: The adjacency list denotes the edges of the graph where edges[i][0] and edges[i][1] represent an edge.

 

Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)"""


class Solution:

    # Function to detect cycle in an undirected graph.

    def isCycle(self, V, adj):
        # Code here
        visited = [False]*(V+1)
        k = []

        def checkcycle(Node):
            visited[Node] = True
            k.append([Node, -1])
            while k:
                m = k.pop(0)
                curr = m[0]
                par = m[1]
                for i in adj[curr]:
                    if not visited[i]:
                        visited[i] = True
                        k.append([i, curr])
                    elif i != par:
                        return True
            return False
        for i in range(0, V):
            if not visited[i]:
                if checkcycle(i):
                    return True
        return False
