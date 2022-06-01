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

def getSucc(curr):
    while curr != None:
        curr = curr.left
    return curr

def deleteInBST(root, k):
    if root == None:
        return
    elif root.data > k :
        root.left = deleteInBST(root.left, k)
        
    elif root.data<k :
        root.right = deleteInBST(root.right, k)
        
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            succ = getSucc(root.right)
            root.data = succ
            root.right = deleteInBST(root.right, succ)
    return root
        



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

deleteInBST(root, 55)
print()
inOrder(root)
