class MergeSort:
    def mergeTwoSortedList(self,a,b):
        i = 0
        j = 0        
        l = 0
        
        if len(a)<=len(b):
            l = len(a)
        else:
            l = len(b) 
            
        arr = []       
        while(i<l and j<l):
            if a[i]<b[j]:
                arr.append(a[i])
                i+=1
            elif (a[i]>b[j]):
                arr.append(b[j])
                j+=1
        
        if i < len(a):
            for k in range(i,len(a)):
                arr.append(a[k])
                
        if j<len(b):
            for k in range(j, len(b)):
                arr.append(b[k])
                
        return arr
    
    def mergeSubArray(self, a, l, m, h):
        le = a[l:m+1]
        ri = a[m+1:h+1]
        i = 0
        j =0
        k =l
        
        while(i<len(le) and j < len(ri)):
            
            if le[i]<= ri[j]:
                a[k] = le[i]
                k+=1
                i+=1
            else:
                a[k] = ri[j]
                k+=1
                j+=1
                
        while(i<len(le)):
            a[k] = le[i]
            i+=1
            k+=1
            
        while(j<len(ri)):
            a[k] = ri[j]
            j+=1
            k+=1
    
    def mergeSort(self, arr, l, h):
        if h>l:
            m = (h+l)//2
            self.mergeSort(arr,l, m)
            self.mergeSort(arr, m+1, h)
            self.mergeSubArray(arr, l,m,h)
                
        
    
a = [1,2,3,8,9]
b = [4,5,6,7,10]

j = MergeSort()
arr = j.mergeTwoSortedList(a,b)
print(arr)

a = [1,2,3,8,9,4,5,6,7,10]
l =0
m = 4
h = len(a)
j.mergeSubArray(a,l,m,h)
print(a)


a = [1,4,2,6,8,9,3,4]
h = len(a)-1
j.mergeSort(a,l,h)
print(a)
a = [4 ,1, 3, 9, 7]
l = 0
h = len(a)-1
j.mergeSort(a,l,h)

print(a)
