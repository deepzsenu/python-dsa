"""_summary_
Given an array arr[], its starting position l and its ending position r. Sort the array using merge sort algorithm.
Example 1:

Input:
N = 5
arr[] = {4, 1 3 9 7}
Output:
1 3 4 7 9
    """
    

class Solution:
    def merge(self,a, l, m, h): 
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
        # code here
    def mergeSort(self,arr, l, h):
        #code here
        if h>l:
            m = (h+l)//2
            self.mergeSort(arr,l, m)
            self.mergeSort(arr, m+1, h)
            self.merge(arr,l,m,h)


#{ 
#  Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends