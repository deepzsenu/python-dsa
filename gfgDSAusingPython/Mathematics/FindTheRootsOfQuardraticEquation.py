
"""Quadratic Equation Roots
BasicAccuracy: 12.78%Submissions: 100k+Points: 1
Given a quadratic equation in the form ax2 + bx + c. Find its roots.

Note: Return the maximum root followed by the minimum root.

Example 1:

Input:
a = 1
b = -2
c = 1
Output: 1 1
Explanation:
Roots of equation x2-2x+1 are 1 and 1.

Example 2:

Input:
a = 1
b = -7
c = 12
Output: 4 3
Explanation: Roots of equation 
x2 - 7x + 12 are 4 and 3.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function quadraticRoots() which takes a, b, c as input parameters and returns a list of two integers containing the floor value of its roots in decreasing order. If roots are imaginary, the returning list should contain only 1 integer ie -1. Always return the greatest integer smaller than or equal to the result.
Note: If roots are imaginary, the generated output will display "Imaginary".

 

Expected Time Complexity: O(1)
Expected Auxiliary Space : O(1)

 

Constraints:
-103 <= a,b,c <= 103


"""



import math
class Solution:
    def quadraticRoots(self, a, b, c):
        # code here
        l = []
        d = (b*b) - (4*a*c)
        if d<0:
            l.append(-1)
            return l
        else:
            d = math.sqrt(d)
            res1 = int(((-b)+d)//(2*a))
            res2 = int(((-b)-d)//(2*a))
            l.append(max(res1, res2))
            l.append(min(res1, res2))
            return l

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        abc=[int(x) for x in input().strip().split()]
        a=abc[0]
        b=abc[1]
        c=abc[2]
        ob = Solution()
        ans = ob.quadraticRoots(a,b,c)
        if len(ans)==1 and ans[0]==-1:
            print("Imaginary")
        else:
            for i in range(len(ans)):
                print(ans[i], end=" ")
            print()
