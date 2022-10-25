"""

Searching an element in a sorted array
BasicAccuracy: 48.03%Submissions: 100k+Points: 1
Given an array arr[] sorted in ascending order of size N and an integer K. Check if K is present in the array or not.


Example 1:

Input:
N = 5, K = 6
arr[] = {1,2,3,4,6}
Output: 1
Exlpanation: Since, 6 is present in 
the array at index 4 (0-based indexing),
output is 1.
 

Example 2:

Input:
N = 5, K = 2
arr[] = {1,3,4,5,6}
Output: -1
Exlpanation: Since, 2 is not present 
in the array, output is -1.
 

Your Task:
You don't need to read input or print anything. Complete the function searchInSorted() which takes the sorted array arr[], its size N and the element K as input parameters and returns 1 if K is present in the array, else it returns -1. 


Expected Time Complexity: O(Log N)
Expected Auxiliary Space: O(1)"""



class Solution:
    ##Complete this function
        ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        s = 0
        end = N-1

        while(s<=end):
            mid = (s+end)//2
            if arr[mid] == K:
                return 1

            elif arr[mid]>K:
                end = mid-1
            elif arr[mid]<K:
                s = mid+1
        return -1