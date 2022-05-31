"""Three methods of reversing an array
    """

def reverseSlicingMethod(arr):
    return arr[::-1]

def reverseArraySwaping(arr):
    l = 0
    h = len(arr)-1
    while(l<=h):
        arr[l], arr[h] = arr[h], arr[l]
        l+=1
        h-=1
        
def reverseRecursion(arr, l, h):
    if l>=h:
        return
    arr[l] , arr[h] = arr[h], arr[l]
    reverseRecursion(arr, l+1, h-1)
    
arr = [1,2,3,4,5,6,7,8,9]
print(reverseSlicingMethod(arr))
reverseArraySwaping(arr)
print(arr)
l = 0
h = len(arr)-1
(reverseRecursion(arr, l, h))
print(arr)

    
        
    