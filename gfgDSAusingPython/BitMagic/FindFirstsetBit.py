"""
Find first set bit
EasyAccuracy: 46.89%Submissions: 95005Points: 2
Lamp
This problem is part of GFG SDE Sheet. Click here to view more.  

Given an integer an N. The task is to return the position of first set bit found from the right side in the binary representation of the number.
Note: If there is no set bit in the integer N, then return 0 from the function.  

Example 1:

Input: N = 18
Output: 2
Explanation: Binary representation of 
18 is 010010,the first set bit from the 
right side is at position 2.
Example 2:

Input: N = 12 
Output: 3 
Explanation: Binary representation 
of  12 is 1100, the first set bit 
from the right side is at position 3.
Your Task:
The task is to complete the function getFirstSetBit() that takes an integer n as a parameter and returns the position of first set bit.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
0 <= N <= 108"""

#naive Approach

class Solution:
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        #Your code here
        if  n == 0 :
            return 0
        l= ""
        while n>0:
            b = n%2
            l += str(b)
            n = n//2

        for i in range(len(l)):
            if l[i] == '1':
                return i+1


#second method :  Using Bitwise right shift
class Solution:

    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        #Your code here
        l = 0
        while n>0:
            l+=1
            if n%2 ==1:
                return l
            n = n>>1
        return l


