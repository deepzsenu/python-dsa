"""Digits In Factorial
EasyAccuracy: 29.7%Submissions: 97713Points: 2
Given an integer N. Find the number of digits that appear in its factorial. 
Factorial is defined as, factorial(n) = 1*2*3*4……..*N and factorial(0) = 1.
 

Example 1:

Input: N = 5
Output: 3
Explanation: Factorial of 5 is 120.
Number of digits in 120 is 3 (1, 2, and 0)
 

Example 2:

Input: N = 120
Output: 199
Explanation: The number of digits in
120! is 199

Your Task:
You don't need to read input or print anything. Your task is to complete the function digitsInFactorial() that takes N as input parameter and returns number of digits in factorial of N.


Expected Time Complexity : O(N)
Expected Auxilliary Space : O(1)



C"""

#method 1 will though runtime error for larger input

def countdig(n):
    c  = 0

    while n>0:
        rem = n%10
        c+=1
        n = n//10

    return c

class Solution:
    def digitsInFactorial(self,N):

        #Your code here
        s =1
        for i in range(1, N+1):
            s*=i
        return countdig(s)

#method 2 with complexity will pass some more cases

def count(s):
    return len(str(s))

class Solution:
    def digitsInFactorial(self,N):

        #Your code here
        s =1
        for i in range(1, N+1):
            s*=i
        return count(s)


# method 3  with comlpexity n:
import math
class Solution:
    def digitsInFactorial(self,N):
        res=0

        for i in range(2,N+1):

            res+=math.log10(i)

        return int(math.floor(res)+1)