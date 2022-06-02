"""Given an array arr[] of size N of positive integers which may have duplicates.
The task is to find the maximum and second maximum from the array, and both of them 
should be different from each other, so If no second max exists,
then the second max will be -1.

Example 1:

Input:
N = 3
arr[] = {2,1,2}
Output: 2 1
Explanation: From the given array 
elements, 2 is the largest and 1 
is the second largest.
"""


class Solution:
    # Function to find largest and second largest element in the array
    def largestAndSecondLargest(self, n, arr):
        
        
        # Your code here'''
        # Function should return a list containing two elements'''
        # li = [maximum, second_maximum]
        maxi = arr[0]
        secmax = -1
        for i in range(n):
            if arr[i]>maxi:
                secmax = maxi
                maxi = arr[i]
                
            elif arr[i]>secmax and arr[i]<maxi:
                secmax = arr[i]
        j = []
        j.append(maxi)
        j.append(secmax)
        return j
    
"""for more solutions refer to solution no 2"""
