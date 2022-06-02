import math


class MyMinHeap:
    def __init__(self):
        self.arr = []

    def parent(self, i):
        return (i-1)//2

    def leftChild(self, i):
        return (2*i)+1

    def rightChild(self, i):
        return (2*i)+2

    def insert(self, x):
        arr = self.arr
        arr.append(x)
        l = len(arr)
        while l >= 0 and arr[l] < arr[self.parent(l)]:
            p = self.parent(l)
            arr[l], arr[p] = arr[p], arr[l]
            l = p

    def minHeapify(self, i):
        arr = self.arr
        lt = self.leftChild(i)
        rt = self.rightChild(i)
        smallest = i
        n = len(arr)
        if lt < n and arr[lt] < arr[smallest]:
            smallest = lt
        if rt < n and arr[rt] < arr[smallest]:
            smallest = rt
        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.minHeapify(smallest)

    def extractMIn(self):
        arr = self.arr
        n = len(arr)
        if n == 0:
            return math.inf
        res = arr[0]
        arr[0] = arr[n-1]
        arr.pop()
        self.minHeapify(0)
        return res

    def decreaseKey(self, i, x):
        pass

    def delet(self, i):
        pass
