"""Multiplication Under Modulo
BasicAccuracy: 83.95%Submissions: 19330Points: 1
You are given two numbers a and b. You need to find the multiplication of a and b under modulo M (M as 109+7).

Example 1:

Input:
a = 92233720368547758
b = 92233720368547758
Output: 484266119
Explanation: Multiplication of a and b 
under modulo M will be 484266119.
Example 2:

Input:
a = 1000000007
b = 1000000007
Output: 0
Explanation: Multiplication of a and b
under modulo M is 0.
Your Task:
You don't need to read input or print anything. Your task is to complete the function multiplicationUnderModulo() that takes a and b as parameters and returns multiplication of a and b under modulo M.

Expected Time Complexity : O(1)
Expected Auxilliary Space :  O(1)

Constraints:
1 <= a,b <= 263-1"""
class Solution:
    def multiplicationUnderModulo(self,a,b):
        '''
        :param a: given value of a
        :param b: given value of b
        :return: Integer , sum under modulo
        '''
        # code here
        mod = 10**9+7
        a = a%mod
        b = b%mod
        return (a*b)%mod