#simple linear search
def minMaxSLS(arr):
    min_ = arr[0]
    max_ = arr[0]
    for i in range(1,len(arr)-1):
        if arr[i]<min_:
            min_ = arr[i]
        if arr[i]>max_:
            max_ = arr[i]
            
    return min_, max_
#compare in pairs
def minMaxCIP(arr):
    min_ = 0
    pass


    