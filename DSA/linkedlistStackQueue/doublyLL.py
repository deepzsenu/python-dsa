
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def printlinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print("")


def insertAtBegin(head, k):
    if head == None:
        j = Node(k)
        j.prev = None
        j.next = None
        return j
    j = Node(k)
    j.prev = None
    j.next = head
    head.prev = j
    return j


def insertAtEnd(head, k):
    temp = Node(k)
    if head == None:
        return temp

    curr = head
    while curr.next != None:
        curr = curr.next

    curr.next = temp
    temp.prev = curr
    return head


def deletHeadofDLL(head):
    if head == None:
        return None
    if head.next == None:
        return None
    head = head.next
    head.prev = None
    return head


def deletingLastNodeOfDll(head):
    if head == None:
        return None
    if head.next == None:
        return None

    curr = head
    while curr.next.next != None:
        curr = curr.next

    curr.next = None
    return head


def reverseDoublyLL(head):
    if head == None:
        return None
    if head.next == None:
        return head

    curr = head
    prev = None
    while curr != None:
        prev = curr
        curr.next, curr.prev = curr.prev, curr.next
        curr = curr.prev

    return prev


def addNodeAtPosition(head, p, data):
    curr = head
    temp = Node(data)
    for i in range(p):
        curr = curr.next

    temp.next = curr.next
    curr.next = temp
    temp.prev = curr
    return head
    """SECOND METHOD"""

    # temp = Node(data)
    # if head == None and p == 1:
    #     return temp

    # if head == None and p>1:
    #     return None
    # curr = head
    # while p:
    #     p-=1
    #     curr = curr.next

    # if curr.next == None:
    #     temp.prev = curr
    #     curr.next = temp
    #     return head

    # temp.next = curr.next
    # curr.next.prev = temp
    # temp.prev = curr
    # curr.next = temp
    # return head


def sortedInsert(head, x):
    temp = Node(x)
    if head == None:
        return temp
    curr = head
    if head.data > x:
        temp.next = head
        head.prev = temp
        return temp
    if head.next == None:
        head.next = temp
        temp.prev = head
        return head

    while curr.next.data < temp.data:
        curr = curr.next
        if curr.next == None:
            break

    if curr.next == None:
        curr.next = temp
        temp.prev = curr
        return head

    else:
        temp.next = curr.next
        curr.next.prev = temp
        temp.prev = curr
        curr.next = temp
        return head


def deleteNodeatK(head, x):
    # Code here
    if head == None or (head.next == None and x == 1):
        return None

    if x == 1:
        head = head.next
        head.prev = None
        return head

    temp = head
    while x-1:
        x -= 1
        temp = temp.next

    if temp.next == None:
        temp.prev.next = None
        return head

    temp.prev.next = temp.next
    temp.next.prev = temp.prev
    return head


head = Node(10)
temp1 = Node(20)
temp2 = Node(30)

head.next = temp1
temp1.prev = head
temp1.next = temp2
temp2.prev = temp1

printlinkedList(head)
j = insertAtBegin(head, 9)
printlinkedList(j)

head = insertAtEnd(j, 34)
printlinkedList(head)


head = deletHeadofDLL(head)
printlinkedList(head)

head = deletingLastNodeOfDll(head)
printlinkedList(head)

head = reverseDoublyLL(head)
printlinkedList(head)
