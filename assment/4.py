def removeBackwards(arr, ind, h):
    j = []
    
    for i in range(len(arr)):
        if i<ind-1 :
            j.append(arr[i])
    if h<len(arr):
        j = j+arr[ind+h-1:]
 
    return j

a = ["hello " , " world" , "is", "my", "frist", "program"]
print(removeBackwards(a,4,2))
            
    