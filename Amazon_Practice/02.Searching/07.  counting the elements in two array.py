"""Easy Accuracy: 47.9 Submissions: 36921 Points: 2
Given two unsorted arrays arr1[] and arr2[]. 
They may contain duplicates. For each element in arr1[]
count elements less than or equal to it in array arr2[].

Example 1:

Input:
m = 6, n = 6
arr1[] = {1,2,3,4,7,9}
arr2[] = {0,1,2,1,1,4}
Output: 4 5 5 6 6 6
Explanation: Number of elements less than
or equal to 1, 2, 3, 4, 7, and 9 in the
second array are respectively 4,5,5,6,6,6
Example 2:

Input:
m = 5, n = 7
arr1[] = {4 ,8, 7, 5, 1}
arr2[] = {4,48,3,0,1,1,5}
Output: 5 6 6 6 3
Your Task :
Complete the function countEleLessThanOrEqual() 
that takes two array arr1[], arr2[],  m, and n as 
input and returns an array containing the required 
results(the count of elements less than or equal to
it in arr2 for each element in arr1 where ith output
represents the count for ith element in arr1.)

Expected Time Complexity: O((m + n) * log n).
Expected Auxiliary Space: O(1).

Constraints:
1<=m,n<=10^5

1<=arr1[i],arr2[j]<=10^5"""

"""Brute Force approach with TLE"""


class Solution:
    def countEleLessThanOrEqual(self,arr1,n1,arr2,n2):
        #returns the required output
        jim = []
        
        for i in range(len(arr1)):
            s = 0
            for j in range(len(arr2)):
                if arr1[i]>=arr2[j]:
                    s+=1
            jim.append(s)
            
        return jim
    
"""optimised approach using BInary search"""

class Solution:
    def countEleLessThanOrEqual(self,arr1,n1,arr2,n2):
        #returns the required output
        ans= []
        arr2.sort()
        for i in range(len(arr1)):
            
            if arr1[i]>=arr2[n2-1]:
                ans.append(n2)
            elif arr1[i]<arr2[0]:
                ans.append(0)
                
            else:
                lo = 0
                h = n2-1
                cnt = 0
                while (lo<h):
                    mid = lo+((h-lo)//2)
                    if arr2[mid]<= arr1[i]:
                        cnt = max(cnt, mid+1)
                        lo = mid+1
                    else:
                        h = mid
                ans.append(cnt)
            
        return ans