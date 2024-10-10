class Node:
    def __init__(self, k):
        self.key = k
        self.next = None
        
def printlinkedList(self, head):
    curr  =  head
    while curr != None:
        print(curr.key, end = " ")
        curr = curr.next
            
            
            
head = Node(10)
head.next= Node(20)
head.next.next = Node(5)
head.next.next.next  = Node(15)

printlinkedList(head)


        