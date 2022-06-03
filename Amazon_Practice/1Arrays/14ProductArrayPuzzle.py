"""y: 47.32 ubmissions: 79005 Points: 2
Given an array nums[] of size n, construct a
Product Array P (of same size n) such that P[i] is 
equal to the product of all the elements of nums except nums[i].

 

Example 1:

Input:
n = 5
nums[] = {10, 3, 5, 6, 2}
Output:
180 600 360 300 900
Explanation: 
For i=0, P[i] = 3*5*6*2 = 180.
For i=1, P[i] = 10*5*6*2 = 600.
For i=2, P[i] = 10*3*6*2 = 360.
For i=3, P[i] = 10*3*5*2 = 300.
For i=4, P[i] = 10*3*5*6 = 900.
Example 2:

Input:
n = 2
nums[] = {12,0}
Output:
0 12

Your Task:
You do not have to read input. Your task is to complete 
the function productExceptSelf() that takes array nums[]
and n as input parameters and returns a list of n integers
denoting the product array P. If the array has only one element
the returned list should should contains one value i.e 
Note: Try to solve this problem without using the division operation.
 

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)
"""

"""Naive approach"""

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        p = []
        for i in range(n):
            pro = 1
            for j in range(n):
                if i == j:
                    pro*=1
                else:
                    pro*=nums[j]
            p.append(pro)
        return p
    
"""Optimized code"""


class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        real_pro = 1
        ans = [0]*n
        count = 0
        store = 0
        
        for i in range(n):
            if nums[i]>0:
                real_pro*=nums[i]
            else:
                count+=1
                store = i
                if count>1:
                    return ans
        if count == 1:
            ans[store] = real_pro
            return ans
            
        for i in range(n):
            ans[i] = real_pro//nums[i]
        return ans