class Node:
    def __init__(self, k):
        self.key = k
        self.next = None
        
def printlinkedList( head):
    curr  =  head
    while curr != None:
        print(curr.key, end = " ")
        curr = curr.next
    print("")
            
def searchAnElement(head, n):
    curr = head
    idx = 0
    while curr!= None:
        if curr.key == n:
            return idx, curr.key
        
        idx+=1
        curr = curr.next
        
def insertAtBegining(head, k):
    temp = Node(k)
    temp.next = head
    return temp

def insertAtEnd(head, key):
    if head == None:
        return Node(key)
    curr = head
    while curr.next != None:
        curr =curr.next        
    curr.next = Node(key)
    return head

def insertAtPosition(head, pos, k):
    temp = Node(k)
    if pos == 1:
        temp.next = head
        return temp
    
    curr = head
    idx = 1    
    while(idx < pos-1):
        curr = curr.next
        if curr == None:
            return head
        idx+=1
    temp.next = curr.next
    curr.next =temp
    return head

def insertAtPositioGFG(head,pos,k):
    #code here
    temp = Node(k)
    size = 0
    while(head!=None):
        size+=1
        if size == pos:
            temp.next = head.next
            head.next = temp
            return 
        head = head.next        
    return head

def  deleteFirst(head):
    if head == None:
        return None
    else:
        return head.next
        
def deletLastNode(head):
    if head == None:
        return None
    if head.next == None:
        return None
    curr = head
    while(curr.next.next != None):
        curr = curr.next
        
    curr.next = None
    return head  

def inserForSortedLL(head, x):
    temp = Node(x)
    if head == None:
        return temp
    elif x < head.key:
        temp.next = head
        return temp
    else:
        curr = head
        while (curr.next != None) and (curr.next.key<x):
            curr = curr.next
            
        temp.next = curr.next
        curr.next = temp
        return head
    
def reverseLinkedListNaive(head):
    stk = []
    curr =head
    while curr is not None:
        stk.append(curr.key)
        curr = curr.next
    curr  = head
    while curr is not None:
        curr.key = stk.pop()
        curr = curr.next        
    return head  

def reverseUsingReversalLinks(head):
    curr = head
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        
    return prev 

def reverseRecuresivelyMedthodOne(head):
    if head == None:
        return head
    if head.next == None:
        return head
    rest_head = reverseUsingReversalLinks(head.next)
    rest_tail = head.next
    rest_tail.next = head
    head.next = None
    return rest_head

def reverseRecuresivelyMedthodTwo(curr, prev = None):
    if curr == None:
        return prev
    n = curr.next
    curr.next = prev    
    return reverseRecuresivelyMedthodTwo(n, curr)
         
    
         

        
            
head = Node(10)
head.next= Node(20)
head.next.next = Node(5)
head.next.next.next  = Node(15)

printlinkedList(head)
print(searchAnElement(head, 5))
head = insertAtBegining(head,23)
printlinkedList(head)

h = insertAtEnd(head, 45)
printlinkedList(h)

ha = insertAtPosition(head,3,67)
printlinkedList(ha)

f = deleteFirst(head)
printlinkedList(f)

g = deletLastNode(f)
printlinkedList(f)

head = inserForSortedLL(g, 25)
printlinkedList(head)

head = reverseLinkedListNaive(head)
printlinkedList(head)


head = reverseUsingReversalLinks(head)
printlinkedList(head)

head = reverseRecuresivelyMedthodOne(head)
printlinkedList(head)

head = reverseRecuresivelyMedthodTwo(head, None)
printlinkedList(head)


        