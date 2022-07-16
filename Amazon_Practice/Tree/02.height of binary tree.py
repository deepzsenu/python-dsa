"""2. Height of Binary Tree 
Medium Accuracy: 65.76% Submissions: 100k+ Points: 4
Lamp
This problem is part of GFG SDE Sheet. Click here to view more.   
Given a binary tree, find its height.


Example 1:

Input:
     1
    /  \
   2    3
Output: 2
Example 2:

Input:
  2
   \
    1
   /
 3
Output: 3   

Your Task:
You don't need to read input or print anything. Your task is to complete the function height() which takes root node of the tree as input parameter and returns an integer denoting the height of the tree. If the tree is empty, return 0. 


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)


Constraints:
1 <= Number of nodes <= 105
1 <= Data of a node <= 105"""

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if root  == None:
            return 0
        return max(self.height(root.left),self.height(root.right))+1
