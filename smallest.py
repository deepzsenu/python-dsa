class Solution:
    def findMissing(self,arr, size): 
    
        mini = 1
        for i in range(size):
            if arr[i]>0:
                p = (arr[i]-1)%size
                if arr[p]>arr[i] or arr[p]<=0:
                    arr[p], arr[i] = arr[i], arr[p]
                    
        for i in range(size):
            if arr[i] == mini:
                mini+=1
        return mini

ob = Solution()
arr = [2,1,5,4,3,7,8,9]
size = len(arr)
j = ob.findMissing(arr,size)
print(j)
print(arr)
