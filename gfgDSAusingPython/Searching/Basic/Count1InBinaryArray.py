"""Count 1's in binary array
EasyAccuracy: 49.3%Submissions: 36807Points: 2
Given a binary sorted non-increasing array of 1s and 0s. You need to print the count of 1s in the binary array.

Example 1:

Input:
N = 8
arr[] = {1,1,1,1,1,0,0,0}
Output: 5
Explanation: Number of 1's in given
binary array : 1 1 1 1 1 0 0 0 is 5.
Example 2:

Input:
N = 8
arr[] = {1,1,0,0,0,0,0,0}
Output: 2
Explanation: Number of 1's in given
binary array : 1 1 0 0 0 0 0 0 is 2.
Your Task:
The task is to complete the function countOne() which takes the array arr[] and its size N as inputs and returns the count of 1s in the input array.

Expected Time Complexity: O(LogN).
Expected Auxiliary Space: O(1).

Constraint:
1 <= N <= 5*106
arr[i] = 0,1"""
#nave approach: (n)
def fum(Arr):
    c = 0
    for i in Arr:
        if i == 1:
            c+=1
    return c


# using Binary search (logn)
class Solution:
    ##Complete this code
    def countOnes(self,arr, N):
        #Your code here
        if N == 0:
            return 0
        if N == 1:
            if arr[0] == 1:
                return 1
            else:
                return 0
        low = 0
        end  = N-1
        while (low <=end):
            mid = (low+end)//2
            if arr[mid] == 0:
                end  = end-1
            else:
                low  = mid+1
        return low


