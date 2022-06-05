"""Medium Accuracy: 52.21 Submissions: 100k+ Points: 4
Given an integer x, find the square root of x.
If x is not a perfect square, then return floor(√x).

 

Example 1:

Input:
x = 5
Output: 2
Explanation: Since, 5 is not a perfect 
square, floor of square_root of 5 is 2.
Example 2:

Input:
x = 4
Output: 2
Explanation: Since, 4 is a perfect 
square, so its square root is 2.
 

Your Task:
You don't need to read input or print anything. The task is to complete the function floorSqrt() which takes x as the input parameter and return its square root.
Note: Try Solving the question without using sqrt Function.

 

Expected Time Complexity: O(log N)
Expected Auxiliary Space: O(1)

 

Constraints:
1 ≤ x ≤ 107"""

"""Using BAsic MAths Calculation"""
class Solution:
    def floorSqrt(self, x): 
    #Your code here
        return int(x**(1/2))
    
    
"""Using Binary Search"""
class Solution:
    def floorSqrt(self, x):
        l = 1
        h = x
        ans = 0 
        while(l<=h):
            mid = (l+h)//2
            if (mid*mid)<=x:
                ans = mid
                l = mid+1
            else:
                h = mid-1                
        return ans
    
"""One more easy approach with time complexity logn"""

class Solution:
    def floorSqrt(self, x): 
        a =1
        while(a*a<=x):
            a+=1
        return a-1