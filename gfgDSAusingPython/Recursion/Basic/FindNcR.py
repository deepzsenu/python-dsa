"""

Find nCr
EasyAccuracy: 54.62%Submissions: 7961Points: 2
You are given two numbers n and r. You need to find nCr.
nCr = (n!) / ((n-r)!*(r!))
In recursive way, we can write nCr as nCr = (n-1)C(r-1) + (n-1)Cr

Example 1:

Input:
n = 5, r = 2
Output: 10
Example 2:

Input:
n = 4, r = 1
Output: 4
Your Task:
You only need to complete the function nCr that takes n and r as parameters and returns the nCr.

Expected Time Complexity: O(2N).
Expected Auxiliary Space: O(2N) (Recursive).

Constraints:
1 <= r <= n <= 30"""


def nCr(n,r):
    #code here
    if n == r or r ==0 :
        return 1;
    return nCr(n-1, r-1)+nCr(n-1,r)