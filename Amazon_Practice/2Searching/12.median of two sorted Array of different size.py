"""12. Median of 2 Sorted Arrays of Different Sizes 
Hard Accuracy: 50.0 Submissions: 32789 Points: 8
Given two sorted arrays array1 and array2 of size m and n respectively.
Find the median of the two sorted arrays.

Example 1:

Input:
m = 3, n = 4
array1[] = {1,5,9}
array2[] = {2,3,6,7}
Output: 5
Explanation: The middle element for
{1,2,3,5,6,7,9} is 5
Example 2:

Input:
m = 2, n = 4
array1[] = {4,6}
array2[] = {1,2,3,5}
Output: 3.5
Your Task:
The task is to complete the function MedianOfArrays() 
that takes array1 and array2 as input and returns their median. 

Can you solve the problem in expected time complexity?

Expected Time Complexity: O(min(log n, log m)).
Expected Auxiliary Space: O((n+m)/2).

Constraints: 
0 ≤ m,n ≤ 104
1 ≤ array1[i], array2[i] ≤ 105"""



"""Naive Approach"""
class Solution:
    def MedianOfArrays(self, arr1, arr2):
            #code here
       j = arr1+arr2
       j.sort()
       idx =0 
       
       if len(j)%2!=0:
           idx = (len(j)//2)
           return j[idx]
           
       else:
            i1 = len(j)//2-1
            i2 = i1+1
            ans  = (j[i1]+j[i2])/2
            if ans == (j[i1]+j[i2])//2:
                return (j[i1]+j[i2])//2
            else:
                return ans