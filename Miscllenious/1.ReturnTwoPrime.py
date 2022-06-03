"""Given an even number N (greater than 2), 
return two prime numbers whose sum will be equal to given number. 
There are several combinations possible. Print only the pair whose minimum 
value is the smallest among all the minimum values of pairs and print 
the minimum element first.

NOTE: A solution will always exist, read Goldbachs conjecture. 

Example 1:

Input: N = 74
Output: 3 71
Explaination: There are several possibilities 
like 37 37. But the minimum value of this pair 
is 3 which is smallest among all possible 
minimum values of all the pairs.
Example 2:

Input: 4
Output: 2 2
Explaination: This is the only possible 
prtitioning of 4.
Your Task:
You do not need to read input or print anything. 
Your task is to complete the function primeDivision() which takes N as input 
parameter and returns the partition satisfying the condition.

Expected Time Complexity: O(N*log(logN))
Expected Auxiliary Space: O(N)

Constraints:
4 ≤ N ≤ 104 
"""
link = "https://practice.geeksforgeeks.org/problems/return-two-prime-numbers2509/1#"
#User function Template for python3
def isPrime(n):
    if n ==2 or n== 3:
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(5,int(n**(1/2)+1), 6):
        if n%i ==0 or (n)%(i+2) == 0:
            return False
    return True
class Solution:
    def primeDivision(self, N):
        # code here
        for i in range(2,N+1):
            if isPrime(i)== True and isPrime(N-i)== True:
                return (i,N-i)
            