"""Recursively Sum N Numbers
EasyAccuracy: 67.33%Submissions: 7975Points: 2
You are given a number n. You need to recursively sum the numbers from 1 to n and return the sum.

Example 1:

Input:
n = 5
Output: 15
Example 2:

Input:
n = 4
Output: 10
Your Task:

Complete the function recursiveSum that takes n as paramenter and return the sum.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N) (Recursive).

Constraints:
0 <= n <= 100"""

class Solution:
    def recursiveSum(self,n):
        #code here
        if n == 0:
            return 0
        return n+self.recursiveSum(n-1)