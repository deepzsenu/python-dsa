"""Given a positive integer N.
You have to find Nth natural number after 
removing all the numbers containing digit 9.

Example 1:

Input:
N = 8
Output:
8
Explanation:
After removing natural numbers which contains
digit 9, first 8 numbers are 1,2,3,4,5,6,7,8
and 8th number is 8
"""
class Solution:
    def findNth(self,N,m:int=9):
        #code here
        a , b = 0,1
        
        while N>0:
            a+=(b*(int(N)%m))
            N/=m
            b*=10
        return a