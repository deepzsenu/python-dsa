"""y Accuracy: 50.0 Submissions: 25369 Points: 2
Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element K. The task is to find the index of the given element K in the array A.

Example 1:

Input:
N = 9
A[] = {5 6,7,8,9,10,1,2,3}
K = 10
Output: 5
Explanation: 10 is found at index 5.
Example 1:

Input:
N = 3
A[] = {3,1,2}
K = 1
Output: 1
User Task:
Complete Search() function and return the index of the element K if found in the array. If the element is not present, then return -1.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1)
"""

"""NAive approach"""
def Search(arr,n,k):
    #code here
    for i in range(n):
        if arr[i] == k:
            return i
            
    return -1

"""using binary search"""


def Search(arr,n,k):
    #code here
    l = 0
    h = n-1
    while l<=h:
        mid = (l+h)//2
        if arr[mid] == k:
            return mid
        elif arr[l]<=arr[mid]:
            if k<arr[mid] and k>= arr[l]:
                h = mid-1
            else:
                l = mid+1
        else:
            if k<arr[h] and k>arr[mid]:
                l = mid+1
            else:
                h = mid-1
    return -1
    