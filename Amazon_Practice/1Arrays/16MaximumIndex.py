"""_summary_
Medium Accuracy: 42.72 Submissions: 84969 Points: 4
Given an array A[] of N positive integers. The task is to find the maximum of j - i
subjected to the constraint of A[i] < A[j] and i < j.
 

Example 1:

Input:
N = 2
A[] = {1, 10}
Output:
1
Explanation:
A[0]<A[1] so (j-i) is 1-0 = 1.
Example 2:

Input:
N = 9
A[] = {34, 8, 10, 3, 2, 80, 30, 33, 1}
Output:
6
Explanation:
In the given array A[1] < A[7]
satisfying the required 
condition(A[i] < A[j]) thus giving 
the maximum difference of j - i 
which is 6(7-1).
 

Your Task:
The task is to complete the function maxIndexDiff() 
which finds and returns maximum index difference.

Printing the output will be handled by driver code. Return -1 in case no such index is found.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 107
0 ≤ A[i] ≤ 109
    """
    
"""Naive Approach"""

class Solution:
    #Complete this function
    # Function to find the maximum index difference. 
    def maxIndexDiff(self,arr, n): 
        
        ##Your code here
        if n <2:
            return -1
            
        maxd = 0
        for i in range(0, n-1):
            for j in range(n-1, i, -1):
                if arr[i]<=arr[j]:
                    maxd = max(maxd, j-i)
                    
                    break
        return maxd
    
"""OPTIMAL SOLUTION"""


class Solution:
    #Complete this function
    def maxIndexDiff(self,arr, n): 
        
        ##Your code here
        if n <2:
            return -1
            
        lmin = [0]*n
        rmax = [0]*n
        lmin[0] = arr[0]
        for i in range(1,n):
            lmin[i] = min(arr[i], lmin[i-1])
            
        rmax[n-1] = arr[n-1]
        
        for i in range(n-2, -1, -1):
            rmax[i] = max(arr[i], rmax[i+1])
        
        i =0
        j =0
        res = -1
        while i<n and j<n:
            if lmin[i]<=rmax[j]:
                res = max(res, j-i)
                j+=1
            else:
                i+=1
        return res