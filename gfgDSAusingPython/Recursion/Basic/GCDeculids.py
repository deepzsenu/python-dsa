"""GCD Euclid
BasicAccuracy: 77.25%Submissions: 4940Points: 1
You are given a two numbers a and b. Find their GCD using recursion.

Example 1:

Input:
a = 7, b = 8
Output: 1
Example 2:

Input:
a = 2, b = 4
Output: 2
Your Task:

Complete the function GCD that takes a and b as parameters and returns the GCD.

Expected Time Complexity: O(Log(N)).
Expected Auxiliary Space: O(Log(N)) (Recursive).

Constraints:
1 <= a, b <= 100"""
class Solution:
    def GCD(self,a,b):
        #code here
        l = None
        if a>b:
            l = a
        else:
            l = b
        s = a+b - l
        if l%s ==0:
            return s
        return self.GCD(l%s, s)