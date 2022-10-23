"""Sum of Digits of a Number
BasicAccuracy: 73.02%Submissions: 37919Points: 1
You are given a number n. You need to find the sum of digits of n.

Example 1:

Input:
n = 1
Output: 1
Explanation: Sum of digit of 1 is 1.
Example 2:

Input:
n = 99999
Output: 45
Explanation: Sum of digit of 99999 is 45.
Your Task:
You don't need to read input or print anything. Your task is to complete the function sumOfDigits() that takes n as parameter and returns the sum of digits of n.

Expected Time Complexity: O(Logn).
Expected Auxiliary Space: O(Logn) (Recursive).

Constraints:
1 <= n <= 107"""

class Solution:
    def sumOfDigits(self, n):
        '''
        :param n: given number
        :return: sum of digits of n.
        '''
        # code here
        if n == 0:
            return 0
        return n%10+self.sumOfDigits(n//10)