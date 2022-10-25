"""Left Index
EasyAccuracy: 51.44%Submissions: 385Points: 2
Given a sorted array of integers of size N and a number X. Find the leftmost index of X in the array arr[].

Example 1:

Input:
N = 10
arr[] = {1, 1, 2, 2, 3, 4, 5, 5, 6, 7}
X = 1
Output: 0 
Explanation: Because the element 1   
appears twice and its left most 
occurrence is at index 0.

Example 2:

Input:
N = 5
arr[] = {2, 2, 3, 3, 4}
X = 4
Output: 4
Explanation: Because element 4 appears
only once at index 4.

Your Task:
You don't need to read input or print anything. Your task is to complete the function leftIndex() which takes the array arr[], its size N and an integer X as input parameters and returns the leftmost occurrence of X in arr[]. If X is not present in the array, return -1.

Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 106
-105 <= arr[i] <= 105
Array may contain duplicate elements. """


class Solution:
    def leftIndex (self, N, arr, X):
        # code here
        l = 0
        h = len(arr)-1
        while(l<=h):
            m = (l+h)//2
            if arr[m]>X:
                h = m-1
            elif arr[m]<X:
                l = m+1
            else:
                if m == 0 or arr[m-1] != arr[m]:
                    return m
                else:
                    h = m-1
        return -1

