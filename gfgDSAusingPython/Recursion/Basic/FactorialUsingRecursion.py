"""Factorial Using Recursion
EasyAccuracy: 73.28%Submissions: 7939Points: 2
You are given a number n. You need to recursively find the factorial of n and return it.

Example 1:

Input:
n = 5
Output: 120
Example 2:

Input:
n = 0
Output: 1
Your Task:

Complete the function factorial that takes n as parameter and returns the factorial. 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N) (Recursive).

Constraints:
0 <= n <= 10"""

class Solution:
    def factorial(self,n):
        #code here
        if n == 0:
            return 1
        return self.factorial(n-1)*n