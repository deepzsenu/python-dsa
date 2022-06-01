from platform import node


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def SearchInBSTrecursive(root, k):  # complexit : time = O(h) space O(h)
    if root == None:
        return False
    if root.data == k:
        return True
    if k > root.data:
        return SearchInBSTrecursive(root.right, k)
    else:
        return SearchInBSTrecursive(root.left, k)


def searchInBSTIterative(root, k):  # complexit : time = O(h) space O(1)
    while root != None:
        if root.data == k:
            return True
        elif root.data > k:
            root = root.left
        else:
            root = root.right
    return False


def insertInBSTrecursive(root, k):
    if root == None:
        return Node(k)
    elif root.data == k:
        return root
    elif root.data < k:
        root.right = insertInBSTrecursive(root.right, k)
    else:
        root.left = insertInBSTrecursive(root.left, k)

    return root


def insertInBSTiterative(root, k):
    parent = None
    curr = root
    while curr != None:
        parent = curr
        if curr.data == k:
            return root
        elif curr.data > k:
            curr = curr.left
        else:
            curr = curr.right

    if parent == None:
        return Node(k)
    elif parent.data > k:
        parent.left = Node(k)
    else:
        parent.right = Node(k)

    return root


def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left

    return current

# Given a binary search tree and a key, this function
# delete the key and returns the new root


def deleteNode(root, key):

    # Base Case
    if root is None:
        return root

    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in  left subtree
    if key < root.data:
        root.left = deleteNode(root.left, key)

    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif(key > root.data):
        root.right = deleteNode(root.right, key)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's
        # content to this node
        root.data = temp.data

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.data)

    return root


def deleteInBST(root, k):
    if root == None:
        return
    else:
        if root.data > k:
            root.left = deleteInBST(root.left, k)

        elif root.data < k:
            root.right = deleteInBST(root.right, k)

        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                succ = minValueNode(root.right)
                root.data = succ
                root.right = deleteInBST(root.right, succ.data)
    return root
def floorCeilBSTHelper(root, key):
     
    global floor, ceil
 
    while (root):
        if (root.data == key):
            ceil = root.data
            floor = root.data
            return
        if (key > root.data):
            floor = root.data
            root = root.right
        else:
            ceil = root.data
            root = root.left
            
def floorCeilBST(root, key):
     
    global floor, ceil
 
    # Variables 'floor' and 'ceil'
    # are passed by reference
    floor = -1
    ceil = -1
 
    floorCeilBSTHelper(root, key)
 
    print(key, floor, ceil)
    
               
def cielInBST(root, x):
    res = None
    while root!=None:
        if root.data == x:
            return root
        elif root.data < x:
            root = root.right           
        else:
            root = root.left
            res = root          
            
    return res

def floorInBST(root, x):
    res = None
    while root!=None:
        if root.data == x:
            return root
        elif root.data<x:
            root = root.left           
        else:
            res = root
            root = root.left
            
    return res
            


def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)


def preOrder(root):
    if root != None:
        print(root.data, end=" ")
        preOrder(root.left)
        preOrder(root.right)


def postOrder(root):
    if root != None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")


j = [50, 10, 20, 15, 27, 45, 80, 60, 70]
root = Node(55)
for i in j:
    insertInBSTrecursive(root, i)

inOrder(root)
print()
preOrder(root)
print()
postOrder(root)


j = [50, 10, 20, 15, 27, 45, 80, 60, 70]
root = Node(55)
for i in j:
    insertInBSTiterative(root, i)
print()
inOrder(root)
print()
preOrder(root)
print()

postOrder(root)
print()
print()

print("floor  of 52")
j  = floorInBST(root,52)
print(j.data)
print("ceil of 52")
j  = cielInBST(root,51)
print(j.data)

print("floor and ceil of 52")
floorCeilBST(root, 52)

deleteNode(root, 55)
print()
inOrder(root)

deleteInBST(root, 50)
print()
inOrder(root)
