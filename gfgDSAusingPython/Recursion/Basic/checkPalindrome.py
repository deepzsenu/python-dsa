"""

Check Palindrome
EasyAccuracy: 43.33%Submissions: 8547Points: 2
You are given a number n. You need to see if the number is a palindrome or not (recursively)

Example 1:

Input:
n = 100
Output: 0
Example 2:

Input:
n = 101
Output: 1
Your Task:

Complete the function isPalin that takes n as parameter and returns true or false . (In case of true, 1 will be printed by the driver code, otherwise 0)

Expected Time Complexity: O(Log(N)).
Expected Auxiliary Space: O(Log(N)) (Recursive).

Constraints:
1 <= n <= 108
"""


class Solution:
    def isPalin(self,N):
        #code here
        n = str(N)
        if (len(n)<=1):
            return 1
        else:
            if n[0] == n[-1]:
                return self.isPalin(n[1:-1])

            else:
                return 0