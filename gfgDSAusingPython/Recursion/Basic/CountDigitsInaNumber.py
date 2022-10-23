"""

Count Total Digits in a Number
EasyAccuracy: 42.13%Submissions: 60167Points: 2
You are given a number n. You need to find the count of digits in n.

Example 1:

Input:
n = 1
Output: 1
Explanation: Number of digit in 1 is 1.
Example 2:

Input:
n  = 99999
Output: 5
Explanation:Number of digit in 99999 is 5
Your Task:
You don't need to read input or print anything. Your task is to complete the function countDigits() that takes n as parameter and returns the count of digits in n.

Expected Time Complexity: O(Logn).
Expected Auxiliary Space: O(Logn).

Constraints:"""

class Solution:
    def countDigits(self, n):
        '''
        :param n: given number
        :return: count of digits of n.
        '''
        # code here
        if n <10:
            return 1

        return 1+self.countDigits(n//10)