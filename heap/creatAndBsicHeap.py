class MyMinHeap:
    def __init__(self):
        self.arr = []
        
    def parent(self, i):
        return (i-1)//2
    def leftChild(self, i):
        return (2*i)+1
    def rightChild(self, i):
        return (2*i)+2
    
    def insert(self,x):
        pass
    def minHeapify(self,x):
        pass
    def extractMIn(self):
        pass
    def decreaseKey(self, i, x):
        pass
    
    def delet(self, i):
        pass       