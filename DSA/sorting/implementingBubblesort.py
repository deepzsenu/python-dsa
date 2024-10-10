def bubbleSort(arr):
    
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
                
                
def bubbleSortOptimize(arr):
    
    for i in range(len(arr)-1):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
                swap = True
        if swap == False:
            return
                
    
                
    
                
arr = [2,1,5,4,3,7,8,9]
bubbleSort(arr)
print(arr)

arr = [9,1 , 2 ,3,4,5,6,7,8]
bubbleSortOptimize(arr)
print(arr)
            
            
    
    