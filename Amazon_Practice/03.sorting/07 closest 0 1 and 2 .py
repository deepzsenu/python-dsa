"""
Given an array of 0s, 1s, and 2s. Arrange the array elements 
such that all 0s come first, followed by all the 1s and then, all the 2s.

Note: Do not use the inbuilt sort function.
 

Example 1:

Input: N = 5, arr[] = {0, 2, 1, 2, 0}
Output: 0 0 1 2 2
Example 2:

Input: N = 3, arr[] = {0, 1, 0}
Output: 0 0 1
Your Task:
You don't need to read input or print anything. 
Your task is to complete the function segragate012() which takes the array arr[]
and the size of the array as inputs and updates the array arr[] such that all
the 0s come before the 1s and all the 1s come before the 2s.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1)"""

class Solution:
    # arr[]: Input Array
    # N: Size of the Array arr[]
    #Function to segregate 0s, 1s and 2s in sorted increasing order.
    def segragate012(self,arr, N):
        # Your Code Here
        l = 0 
        m = 0
        h = N-1
        while m<=h:
            if arr[m] == 0:
                
                arr[l], arr[m] = arr[m], arr[l]
                l+=1
                m+=1
            elif arr[m] == 1:
                m+=1
            elif arr[m] == 2:
                arr[m], arr[h] = arr[h], arr[m]
                h-=1
                