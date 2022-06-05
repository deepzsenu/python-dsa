"""Easy Accuracy: 48.41% Submissions: 100k+ Points: 2
An element is called a peak element if its value is not smaller than the value
of its adjacent elements(if they exists).
Given an array arr[] of size N, find the index of any one of its peak elements.
Note: The generated output will always be 1 if the index that you return is correct.
Otherwise output will be 0. 


Example 1:

Input:
N = 3
arr[] = {1,2,3}
Output: 2
Explanation: index 2 is 3.
It is the peak element as it is 
greater than its neighbour 2.
Example 2:

Input:
N = 2
arr[] = {3,4}
Output: 1
Explanation: 4 (at index 1) is the 
peak element as it is greater than 
its only neighbour element 3.
 

Your Task:
You don't have to read input or print anything.
Complete the function peakElement() which takes the array arr[]
and its size N as input parameters and return the index of any one of its peak elements.

Can you solve the problem in expected time complexity?

 

Expected Time Complexity: O(log N)
Expected Auxiliary Space: O(1)"""

class Solution:   
    def peakElement(self,arr, n):
        # Code here
        l =0
        h = n-1
        while(l<h):
            mid = l+(h-l)//2
            if  arr[mid+1]>arr[mid]:
                l = mid+1
            else:
                h = mid
                
        return l
        """SECOND APPROACH"""
        ma = max(arr)
        idx = 0
        for i in range(n):
            if(ma==arr[i] ):
                idx = i
        return idx
        
        """THIRD APPROACH """
        
        l = 0
        h =n-1
        while(l<=h):
            mid = (l+h)//2
            if arr[mid] < arr[mid-1]:
                h = mid-1
            else:
                l = mid+1
        return h