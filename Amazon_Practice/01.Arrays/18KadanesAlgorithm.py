"""Medium Accuracy: 51.0% Submissions: 100k+ Points: 4
Lamp
This problem is part of GFG SDE Sheet. Click here to view more.   
Given an array Arr[] of N integers.
Find the contiguous sub-array(containing at least one number)
which has the maximum sum and return its sum.


Example 1:

Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
Example 2:

Input:
N = 4
Arr[] = {-1,-2,-3,-4}
Output:
-1
Explanation:
Max subarray sum is -1 
of element (-1)

Your Task:
You don't need to read input or print anything. 
The task is to complete the function maxSubarraySum() 
which takes Arr[] and N as input parameters and returns 
the sum of subarray with maximum sum.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 106
-107 ≤ A[i] ≤ 107"""

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,n):
        ##Your code here
        sum_ =0
        maxsum = -10000000000
        for i in range(n):
            sum_ +=arr[i]
            if sum_>=maxsum:
                maxsum = sum_
            if sum_<0:
                sum_ = 0
        return maxsum
    
"""Second Approach"""
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,n):
        ##Your code here
        max_curr = arr[0]
        max_all = arr[0]
        for i in range(n):
            max_curr = max(arr[i], max_curr+arr[i])
            max_all = max(max_all, max_curr)
        return max_all