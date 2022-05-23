def insertionSort(alist):
    for i in range(1, len(alist)):
            j = i-1
            x = alist[i]
            
            while j>=0 and x<alist[j]:
                alist[j+1] = alist[j]
                j = j-1
            alist[j+1] = x
    

arr = [2,1,5,4,3,7,8,9]
insertionSort(arr)
print(arr)