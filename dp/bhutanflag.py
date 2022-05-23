"""creat 1111 0000 2222 from the given array"""

def bhutanFlag(arr):
    n = len(arr)
    l = 0 
    m = 0
    h = n-1    
    while (m<=h):        
        if arr[m] == 1:
            arr[m], arr[l] = arr[l], arr[m]            
            m+=1
            l+=1        
        elif arr[m] == 0:
            m+=1
        elif arr[m] == 2:
            arr[m],arr[h] = arr[h], arr[m]
            h-=1            
    
arr = [1,2,0,1,2,0,1,1,0,0,2,2]
bhutanFlag(arr)
print(arr)
arr = [1,2,0,0,2,1,2,0,1]
bhutanFlag(arr)
print(arr)
    
            
    
    
    