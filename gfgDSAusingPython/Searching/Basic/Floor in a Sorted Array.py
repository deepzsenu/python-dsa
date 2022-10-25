"""Floor in a Sorted Array
EasyAccuracy: 33.75%Submissions: 100k+Points: 2
Given a sorted array arr[] of size N without duplicates, and given a value x. Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x. Find the index of K(0-based indexing).

Example 1:

Input:
N = 7, x = 0
arr[] = {1,2,8,10,11,12,19}
Output: -1
Explanation: No element less
than 0 is found. So output
is "-1".
Example 2:

Input:
N = 7, x = 5
arr[] = {1,2,8,10,11,12,19}
Output: 1
Explanation: Largest Number less than 5 is
2 (i.e K = 2), whose index is 1(0-based
indexing).
Your Task:
The task is to complete the function findFloor() which returns an integer denoting the index value of K or return -1 if there isn't any such number.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 107
1 ≤ arr[i] ≤ 1018
0 ≤ X ≤ arr[n-1]"""

class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        if A[0]>X:
            return -1
        if A[N-1]<=X:
            return N-1
        l = 0
        h = N-1
        while l<=h:
            mid = (l+h)//2
            
            if A[mid] <X:
                l = mid+1
            elif A[mid]>X:
                h = mid-1
            else:
                return mid
        return l-1