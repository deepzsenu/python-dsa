"""Quick Sort is a Divide and Conquer algorithm. It picks an element as 
pivot and partitions the given array around the picked pivot.
Given an array arr[], its starting position low and its ending position high.

Implement the partition() and quickSort() functions to sort the array.

"""


class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,l,h):
        # code here
        while l<h:
            p = self.partition(arr, l , h)
            self.quickSort(arr,l,p)
            l = p+1
    
    def partition(self,arr,l,h):
        # code here
        pivot = arr[l]
        i = l-1
        j = h+1
        while True:
            i += 1
            while(arr[i]<pivot):
                i +=1
                
            j -=1
            while(arr[j]>pivot):
                j-=1
            if i>=j:
                return j
                
            arr[i], arr[j] = arr[j], arr[i]
            
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends