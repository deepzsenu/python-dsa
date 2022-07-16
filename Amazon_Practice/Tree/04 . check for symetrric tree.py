"""asy Accuracy: 50.54% Submissions: 74362 Points: 2
Lamp
This problem is part of GFG SDE Sheet. Click here to view more.   
Given a Binary Tree. Check whether it is Symmetric or not, i.e. whether the binary tree is a Mirror image of itself or not.

Example 1:

Input:
         5
       /   \
      1     1
     /       \
    2         2
Output: True
Explanation: Tree is mirror image of
itself i.e. tree is symmetric
Example 2:

Input:
         5
       /   \
      10     10
     /  \     \
    20  20     30
Output: False
Your Task:
You don't need to read input or print anything. Your task is to complete the function isSymmetric() which takes the root of the Binary Tree as its input and returns True if the given Binary Tree is a same as the Mirror image of itself. Else, it returns False.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
0<=Number of nodes<=100

Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code."""

def checkSy(l,r):
    if l == None and r == None:
        return True
    if l == None or r == None:
        return False
    if l.data != r.data:
        return False
    return checkSy(l.left, r.right) and checkSy(r.left, l.right)
        
class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def isSymmetric(self, root):
        # Your Code Here
        if root == None:
            return True
        return checkSy(root.left , root.right)