"""Maximum and Minimum In Array
BasicAccuracy: 66.71%Submissions: 9385Points: 1
Given an array arr of size n, find maximum and minimum elements in the array.

Example 1:

Input:
N = 4
arr[] = {5 4 2 1}
Output: 5 1
Example 2:

Input:
N = 1
arr[] = {8}
Output: 8 8
 

Your Task:
You only need to complete the provided functions maximumElement() and minimumElement() which takes 2 arguments(array arr and n) and returns the corresponding answers. The printing is done by the driver code.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ n ≤ 103
0 ≤ arr < 106"""

def maximumElement(arr,n,):
    #return required result
    m = arr[0]
    for i in arr:
        if i> m:
            m = i
    return m

def minimumElement(arr,n):
    #return required result
    m = arr[0]
    for i in arr:
        if i<m:
            m = i
    return m
