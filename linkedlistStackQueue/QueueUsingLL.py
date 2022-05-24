class Node:
    def __init__(self,k):
        self.key = k
        self.next = None
        
class MyQueue:
    def __init__(self) :
        self.front = None
        self.rear = None
        self.sz = 0
        
    def size(self):
        return self.sz
    
    def isEmpty(self):
        return (self.sz == 0)
    
    def getFront(self):
        if self.front == None:
            return None
        else:
            return self.front.key
    
    def getRear(self):
        if self.rear == None:
            return None
        else:
            return self.rear.key
    
    def enqueue(self, x):
        temp =  Node(x)
        
        if self.rear == None:
            self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp
        self.sz +=1
            
    def deQueue(self):
        if self.front == None:
            return None
        else:
            res = self.front.key
            self.front - self.front.next
            
            if self.front  == None:
                self.rear = None
            self.sz -=1    
            return res        
        
        
        

Q = MyQueue()

Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.enqueue(40)
Q.enqueue(50)

j = Q.getFront()
h = Q.getRear()
print(j,h, Q.size())