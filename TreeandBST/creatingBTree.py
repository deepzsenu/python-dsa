# linked repersentation of Binary tree

from re import search


class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k
        
def inOrder( root):
    if root != None:
        inOrder(root.left)
        print(root.key, end = " ")
        inOrder(root.right)
        
def preOrder(root):
    if root != None:
        print(root.key, end  = " ")
        preOrder(root.left)
        preOrder(root.right)
def postOrder(root):
    if root!=None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.key, end = " ")
def sizeOfBT(root):
    if root == None:
        return 0
    ls = sizeOfBT(root.left)
    rs = sizeOfBT(root.right)
    return ls+rs+1        
def findMax(root):
    if root  == None:
        return 0     
    return max(findMax(root.left), root.key, findMax(root.right)) 

def searchInBT(root, k):
    if root == None:
        return False
    elif root.key == k:
        return True
    elif searchInBT(root.left, k) == True:
        return True
    else:
        return searchInBT(root.right, k)
    
def heightOfBT(root):
    #using longest path of subtreees
    if root  == None:
        return 0
    return max(heightOfBT(root.left),heightOfBT(root.right))+1

def inOrderIterative(root):
    if root  == None:
        return
    st = []
    curr  = root
    while curr != None:
        st.append(curr)
        curr = curr.left
    while len(st)>0:
        curr  = st.pop()
        print(curr.key, end = " ")
        curr  = curr.right
        while curr!= None:
            st.append(curr)
            curr = curr.left
            
from collections import deque
def levelOrder(root):
    #code here 
    j = []
    if root == None:
        return []
    q = deque()
    q.append(root)
    while len(q)>0:
        node = q.popleft()
        j.append(node.val)
        if node.left != None:
            q.append(node.left)
        if node.right != None:
            q.append(node.right)
            
    return j
            
def preOrderIterative(root):
    if root  == None:
        return
    st = [root]
    while len(st)>0:
        curr = st.pop()
        print(curr.key, end = ' ')
        if curr.right!=None:
            st.append(curr.right)
        if curr.left != None:
            st.append(curr.left)                
        
root  = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
root.left.left.left = Node(23)
print("inordeer")
(inOrder(root))
print("\n\npreordeer")
preOrder(root)

print("\n\npostordeer")
postOrder(root)
print("\n\ntotal no of elements ")
print("size of binary tree = ", end = " ")
print(sizeOfBT(root))
print(findMax(root))

print("check for values or search")

print("checking for 90 = ",searchInBT(root, 90))
print("checking for 70 = ",searchInBT(root, 70))
print("checking for 800 = ",searchInBT(root, 800))
print("checking for 10 = ",searchInBT(root, 10))

print("\n\n hieght of tree = ", heightOfBT(root))

print("\n\nInorder traversing Iterative way")
inOrderIterative(root)
print("\n\npreorder traversing Iterative way")
preOrderIterative(root)

        
