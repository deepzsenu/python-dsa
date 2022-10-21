"""



Exactly 3 Divisors
EasyAccuracy: 22.85%Submissions: 87992Points: 2
Given a positive integer value N. The task is to find how many numbers less than or equal to N have numbers of divisors exactly equal to 3.

 

Example 1:

Input:
N = 6
Output: 1
Explanation: The only number less than 6 with 
3 divisors is 4.
Example 2:

Input:
N = 10
Output: 2
Explanation: 4 and 9 have 3 divisors.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function exactly3Divisors() that takes N as input parameter and returns count of numbers less than or equal to N with exactly 3 divisors.

 

Expected Time Complexity : O(N1/2 * N1/4)
Expected Auxilliary Space :  O(1)

 

Constraints :
1 <= N <= 109"""

class Solution:
    def isPrime(self,N):
        # code here
        if N < 2 : 
            return False
        if N <= 3 : 
            return True 
        if N % 2 == 0 or N % 3 == 0 : 
            return False
        for i in range(5,(int(math.sqrt(N)))+1):
            if N % i == 0 :
                return False
        return True
    def exactly3Divisors(self,N):
        # code here
       i = 2
       c=0

       while i * i <= N:
            if (self.isPrime(i)):
                if (i * i <= N):
                    c+=1
            i += 1

       return c