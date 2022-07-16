"""acy: 52.13% Submissions: 18603 Points: 2
Given a Binary Tree. Check whether the Binary tree is a full binary tree or not.

Example 1:

Input:
          1
       /    \
      2      3
    /   \
   4     5
Output: 1
Explanation: Every node except leaf node
has two children so it is a full tree.
Example 2:

Input:
          1
       /    \
      2      3
    /   
   4     
Output: 0
Explanation: Node 2 has only one child
so this is not a full tree.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function isFullTree() which takes the root node of the tree as input and returns True if the given Binary Tree is full. Else, it returns False. (The driver code will print 1 if the returned value is true, otherwise 0).

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1<=Number of nodes<=1000

Note:The Input/Ouput format and Example given are used for system's internal purpose,
and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code"""

#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
        
# Return True if the given Binary Tree is a Full Binary Tree. Else return False
def isFullTree(root):
    #code here
    if (root.left and root.right):
        return isFullTree(root.left) and isFullTree(root.right)
        
    elif root.left==None and root.right == None:
        return True
    else:
        return False