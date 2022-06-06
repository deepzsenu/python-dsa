"""23. Max Circular Subarray Sum 
Hard Accuracy: 45.16 Submissions: 49714 Points: 8
Given an array arr[] of N integers arranged in a circular fashion. 
Your task is to find the maximum contiguous subarray sum.


Example 1:

Input:
N = 7
arr[] = {8,-8,9,-9,10,-11,12}
Output:
22
Explanation:
Starting from the last element
of the array, i.e, 12, and 
moving in a circular fashion, we 
have max subarray as 12, 8, -8, 9, 
-9, 10, which gives maximum sum 
as 22.
Example 2:

Input:
N = 8
arr[] = {10,-3,-4,7,6,5,-4,-1}
Output:
23
Explanation: Sum of the circular 
subarray with maximum sum is 23

Your Task:
The task is to complete the function circularSubarraySum() 
which returns a sum of the circular subarray with maximum sum.


Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1)."""

"""Kadanes algo not valid for circular array"""
"""
def circularSubarraySum(arr,n):
    ##Your code here
    min_ = 1000
    min_curr = 0
    for i in range(n):
        
        min_curr = min(arr[i], min_curr+arr[i])
        min_ = min(min_, min_curr)
            
    tot = sum(arr)
    return tot - min_
"""

"""other option"""


def circularSubarraySum(arr,n):
    ##Your code here
    if n == 1:
        return arr[0]
        
    maxSum = arr[0]
    currSum = 0
    found = True
    mn = arr[0]
    
    for i in range(n):
        mn = min(mn, arr[0])
        if arr[i]>=0:
            found = False
            
    if found:
        return mn
        
    for i in range(n):
        if currSum<0:
            currSum = arr[i]
        else:
            currSum+=arr[i]
            
        maxSum = max(maxSum, currSum)
                
    total = 0
    currSum = 0
    minsum= arr[0]
    
    for i in range(n):
        total+=arr[i]
        if currSum>0:
            currSum = arr[i]
        else:
            currSum+=arr[i]
        minsum = min(minsum, currSum)
        
        
    return max(maxSum, total-minsum)