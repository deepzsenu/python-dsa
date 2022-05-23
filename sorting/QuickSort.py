class QuickSort:
    def naivePartion(self,arr,p):
        n = len(arr)
        arr[p], arr[n-1] = arr[n-1], arr[p]
        temp = []
        for x in arr:
            if x<=arr[n-1]:
                temp.append(x)
                
        for x in arr:
            if x>arr[n-1]:
                temp.append(x)
                
        for i in range(len(arr)):
            arr[i] = temp[i]
            
    def lomutoPartition(self,arr,l,h):
        pivot = arr[h]
        i = l-1
        for j in range(l,h):
            if arr[j]<pivot:
                i+=1
                arr[i], arr[j] = arr[j], arr[i]
                
        arr[i+1], arr[h] =arr[h], arr[i+1]
        
        return i+1
    
    def hoursePartition(self, arr, l, h):
        pivot = arr[l]
        i = l-1
        j = h+1
        while True:
            i+=1
            while arr[i]<pivot:
                i+=1
            j -=1
            while arr[j]>pivot:
                j-=1
            if i>=j:
                return j
            
            arr[i], arr[j] = arr[j], arr[i]
            
    def quicSortLomuto(self,arr,l,h):
        if l<h:
            p = self.lomutoPartition(arr,l,h)
            self.quicSortLomuto(arr,l,p-1)
            self.quicSortLomuto(arr, p+1, h)
            
    def quicSortHourse(self,arr,l,h):
        if l<h:
            p = self.hoursePartition(arr,l,h)
            self.quicSortHourse(arr,l,p)
            self.quicSortHourse(arr, p+1, h)
            
    def quicSortHourseTailcall(self,arr,l,h):
        while l<h:
            p = self.hoursePartition(arr,l,h)
            self.quicSortHourse(arr,l,p)
            l = p+1
            
            
ob = QuickSort()
arr = [3,5,2,21,4,2,8,7,65,4,4,3,12]
p = len(arr)//2
ob.naivePartion(arr,p)
print(arr)

arr = [3,5,2,21,4,2,8,7,65,4,4,3,12]
l = 0
h = len(arr)-1
f = ob.lomutoPartition(arr,l,h)#index of pivot
print(arr,f)
print("\n")
            
            
arr = [15,5,2,21,4,2,8,7,65,4,4,3,12]
l = 0
h = len(arr)-1
f = ob.hoursePartition(arr,l,h)#index of pivot
print(arr,f)

arr = [15,5,2,21,4,2,8,7,65,4,4,3,12]
l = 0
h = len(arr)-1
ob.quicSortLomuto(arr,l,h)
print("\nQuick Sort Lumoto")
print(arr)

arr = [15,5,2,21,4,2,8,7,65,4,4,3,12]
l = 0
h = len(arr)-1
ob.quicSortHourse(arr,l,h)
print("\nQuick Sort Hoarse")
print(arr)

arr = [15,5,2,21,4,2,8,7,65,4,4,3,12]
l = 0
h = len(arr)-1
ob.quicSortHourseTailcall(arr,l,h)
print("\nQuick Sort Hoarse tail call elimination")
print(arr)

