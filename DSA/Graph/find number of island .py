"""Medium Accuracy: 38.66 Submissions: 100k+ Points: 4
Lamp
This problem is part of GFG SDE Sheet. Click here to view more.   
Given a grid of size n*m (n is number of rows and m is number of columns grid has) consisting of '0's(Water) and '1's(Land). Find the number of islands.
Note: An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.
 

Example 1:

Input:
grid = {{0,1},{1,0},{1,1},{1,0}}
Output:
1
Explanation:
The grid is-
0 1
1 0
1 1
1 0
All lands are connected.
Example 2:

Input:
grid = {{0,1,1,1,0,0,0},{0,0,1,1,0,1,0}}
Output:
2
Expanation:
The grid is-
0 1 1 1 0 0 0
0 0 1 1 0 1 0 
There are two islands one is colored in blue 
and other in orange.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function numIslands() which takes grid as input parameter and returns the total number of islands.
 

Expected Time Compelxity: O(n*m)
Expected Space Compelxity: O(n*m)
 

Constraints:
1 ≤ n, m ≤ 500
    """
    
import sys
sys.setrecursionlimit(10**5)
class Solution:
    def DFS(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return
 
        # mark it as visited
        grid[i][j] = -1
 
        # Recur for 8 neighbours
        self.DFS(i - 1, j - 1, grid)
        self.DFS(i - 1, j, grid)
        self.DFS(i - 1, j + 1, grid)
        self.DFS(i, j - 1, grid)
        self.DFS(i, j + 1, grid)
        self.DFS(i + 1, j - 1,grid)
        self.DFS(i + 1, j, grid)
        self.DFS(i + 1, j + 1, grid)
    # def dfs(self, i,j,grid):
    #     if  i< 0 or j>=len(grid) or j<0 or j>= len(grid[i]) or grid[i][j] != 1:
    #         return 
        
    #     else:
    #         grid[i][j] = -1
        
    #         self.dfs(i-1, j-1, grid)
    #         self.dfs(i-1, j,  grid)
    #         self.dfs(i-1,  j+1,  grid)
    #         self.dfs(i,  j-1, grid)
    #         self.dfs(i,  j+1, grid)
    #         self.dfs(i+1, j-1, grid)
    #         self.dfs(i+1, j, grid)
    #         self.dfs(i+1, j+1, grid)
        
    def numIslands(self,grid):
        col, row  = len(grid[0]), len(grid)
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    self.DFS(i, j, grid)
                    count+=1
        return count
