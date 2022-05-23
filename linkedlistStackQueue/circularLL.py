
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
    
def printCircularlinkedList( head):
    if head == None:
        print()
    print(head.key, end =" ")
    curr  =  head.next
    while curr != head:
        print(curr.key, end = " ")
        curr = curr.next
    print("")
    
def circularLinkedList(head):
    curr  = head
    while curr.next != None:
        curr = curr.next
    curr.next = head
    return head

def insertAtBeg(head, k):
    if head == None:
        head = Node(k)
        head.next = head
        return head
    curr  = head
    while curr.next != head:
        curr = curr.head
        
    temp = Node(k)
    curr.next = temp
    temp.next = head
    return temp
def insertAtBEdConstantTime(head, k):
    temp = Node(k)
    if head == None:
        temp.next = temp
        return temp
    else:
        temp.next = head.Next
        head.next = temp 
        head.key, temp.key = temp.key, head.key
        return head
    
def insertAtEnd(head, k):
    if head == None:
        head = Node(k)
        head.next = head
        return head
    curr  = head
    while curr.next != head:
        curr = curr.head
        
    temp = Node(k)
    curr.next = temp
    temp.next = head
    return head

def insertAtEndConstantTime(head, k):
    temp = Node(k)
    if head == None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next
        head.next = temp 
        head.key, temp.key = temp.key, head.key
        return temp
    
def DeleteHead(head):
    if head == None:
        return None
    if head.next == head:
        return None
    
    curr = head
    while curr.next!= head:
        curr = curr.next
                
    curr.next  =  head.next
    return curr.next

def deletHeadConstantTime(head):
    if head == None:
        return None
    if head.next == head:
        return None
    
    head.key = head.next.key
    head.next = head.next.next
    return head

def deleteKthNode(head, k):
    if head == None:
        return None
    if k == 1:
        return deletHeadConstantTime(head)
    curr = head
    for i in range(k-2):
        curr = curr.next
    curr.next = curr.next.next
    return head      
    
    

    
head = Node(10)
head.next= Node(20)
head.next.next = Node(5)
head.next.next.next  = Node(15)
printlinkedList(head)

h = circularLinkedList(head)

printCircularlinkedList(h)