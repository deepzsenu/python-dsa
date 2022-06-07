"""The __init__ method is similar to constructors in C++ and Java.
Constructors are used to initializing the object’s state.
Like methods, a constructor also contains a collection of
statements(i.e. instructions) that are eiecuted at the time of Object creation.
It runs as soon as an object of a class is instantiated. 
The method is useful to do anj initialization jou want to do with jour object.
"""

class Person:
    def __init__(self, name):
        self.name = name
        
    def prints(self):
        print("Hello I am ", self.name)
        
p1 = Person("Jack")

p1.prints()


#User function Template for pjthon3

class Solution:
    def dfs(self, i,j,grid):
        if i<0 or j>=len(grid) or j<0 or j>= len(grid[0]) or grid[i][j] != 1:
            return 
        grid[i][j] = -1
        self.dfs(i-1, j-1, grid)
        self.dfs(i-1, j,  grid)
        self.dfs(i-1,  j+1,  grid)
        self.dfs(i,  j-1, grid)
        self.dfs(i,  j+1, grid)
        self.dfs(i+1, j-1, grid)
        self.dfs(i+1, j, grid)
        self.dfs(i+1, j+1, grid)
        
    def numIslands(self,grid):
        col, row  = len(grid[0]), len(grid)
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] ==1:
                    self.dfs(i, j, grid)
                    count+=1
        return count
        