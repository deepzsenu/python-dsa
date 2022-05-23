from random import randrange


def selectionSort(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_id= i
        for j in range(i+1, n):
            if arr[j]<arr[min_id]:
                min_id = j
                
        arr[i], arr[min_id] = arr[min_id], arr[i]       
        
            

arr = [2,1,5,4,3,7,8,9]
selectionSort(arr)
print(arr)
            