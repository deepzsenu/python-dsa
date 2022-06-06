"""
Given two sorted arrays A and B of size M and N respectively. 
Each array may have some elements in common with the other array.
Find the maximum sum of a path from the beginning of any array to
the end of any of the two arrays. We can switch from one array to another 
array only at the common elements.Both the arrays are sorted.
Note: Only one repeated value is considered in the valid path sum.


Example 1:

Input:
M = 5, N = 4
A[] = {2,3,7,10,12}
B[] = {1,5,7,8}
Output: 35
Explanation: The path will be 1+5+7+10+12
= 35."""


#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxSumPath(self, arr1, arr2, m, n):
        #code here
        i =0
        j = 0
        result, sum1, sum2 = 0,0,0
        
        while i<m and j<n:
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i+=1
            elif arr1[i]>arr2[j]:
                sum2 += arr2[j]
                j+=1
            else:
                result += max(sum1,sum2)+arr1[i]
                sum1 = 0
                sum2 = 0
                i+=1
                j+=1
                
        while i<m:
            sum1+=arr1[i]
            i+=1
        while j<n:
            sum2+=arr2[j]
            j+=1
            
        result+= max(sum1,sum2)
        
        return result
                