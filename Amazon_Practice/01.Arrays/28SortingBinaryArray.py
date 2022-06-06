"""Given a binary array A[] of size N. The task is to arrange the array in increasing order.

Note: The binary array contains only 0  and 1.

Example 1:

Input:
N = 5
A[] = {1,0,1,1,0}
Output: 0 0 1 1 1

"""
"""Dutch national flag using two pointers"""
class Solution:
    def sortBinaryArray (self, arr, n):
        # Your code here
        low = 0
        high = n-1
        while(low<high):
            if arr[low] == 0:
                low+=1
            if arr[low] == 1:
                arr[low], arr[high] = arr[high], arr[low]
                high-=1
        return arr
    