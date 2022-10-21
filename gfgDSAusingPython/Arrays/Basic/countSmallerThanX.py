"""

Count Smaller Than X
EasyAccuracy: 78.91%Submissions: 8698Points: 2
Given an unsorted array arr[] of size N containing non-negative integers. You will also be given an integer X, the task is to count the number of elements which are strictly smaller than X. The given integer may or not be present in the array given.

Example 1:

Input:
N = 5
arr[] = {4 5 3 1 2}
X = 3
Output: 2
Explanation: Here X = 3, and elements that
are smaller than X are 1 and 2.
Example 2:

Input:
N = 6
arr[] = {2 2 2 2 2 2}
X = 3
Output: 6
Explanation: Here X = 3, and elements that
are smaller than X are 2 2 2 2 2 2.
Your Task:
Since this is a functional problem you don't have to worry about the input, you just have to complete the given function smallerThanX() which takes 3 arguments(array arr, N, and X) and returns the count of elements smaller than X. The printing is done by the driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 106

1 <= arr[i], X <= 105  """


class Solution:
    def smallerThanX(self,arr,n,x):
        #return required ans
        #code here
        c = 0
        for i in arr:
            if i<x:
                c+=1
        return c
