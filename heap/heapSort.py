
class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        lar = i
        l = 2*i+1
        r = 2*i+2
        if l<n and arr[l]>arr[lar]:
            lar = l
        if r <n and arr[r]>arr[lar]:
            lar = r
        if lar != i:
            arr[i], arr[lar] = arr[lar], arr[i]
            self.heapify(arr, n, lar)
            
            
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        idx= n//2 -1
        for i in range(idx , -1, -1):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
            