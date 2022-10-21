"""



Is Array Sorted
EasyAccuracy: 31.45%Submissions: 17047Points: 2
Given an array a[ ] of size N. The task is to check if array is sorted or not. A sorted array can either be increasingly sorted or decreasingly sorted. Also consider duplicate elements to be sorted.

Example 1:

Input:
N = 5
a[] = {1 1 2 2 3}
Output: 1
Example 2:

Input:
N = 2
a[] = {4 2}
Output: 1
Your Task:
You just need to complete the function isSorted() that takes arr and n as parameters and returns 0 if arr is unsorted and returns 1 if arr is sorted.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 106
1 <= a[i] <= 106"""

class Solution:
    def isSorted(self,arr,n):
        #code here
        i = 1
        c1 = 0
        c2 = 0
        while(i<n):
            if arr[i-1] >= arr[i]:
                c1+=1
            if arr[i-1] <= arr[i]:
                c2+=1
            i+=1
        return int(c1 ==n-1 or c2 == n-1)