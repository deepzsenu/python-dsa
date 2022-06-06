"""Easy Accuracy: 20.69 ubmissions: 100k+ Points: 2
Given an array a[] of size N which contains elements 
from 0 to N-1, you need to find all the elements
occurring more than once in the given array.

Example 1:

Input:
N = 4
a[] = {0,3,1,2}
Output: -1
Explanation: N=4 and all elements from 0
to (N-1 = 3) are present in the given
array. Therefore output is -1.
Example 2:

Input:
N = 5
a[] = {2,3,1,2,3}
Output: 2 3 
Explanation: 2 and 3 occur more than once
in the given array.
Your Task:
Complete the function duplicates() which takes array a[] and n as input as parameters and returns a list of elements that occur more than once in the given array in sorted manner. If no such element is found, return list containing [-1]. 

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).
Note : The extra space is only for the array to be returned.
Try and perform all operation withing the provided array. 

Constraints:
1 <= N <= 105
0 <= A[i] <= N-1, for each valid """


"""Below solution didn't not allowed beacuse we of nlog(n) time complexity But it works """




from collections import Counter as cnt
class Solution:
    def duplicates(self, arr, n):
        # code here
        j = cnt(arr)
        sol = []
        for i in j:
            if j[i] > 1:
                sol.append(i)
        sol.sort()
        if len(sol) > 0:
            return sol
        else:
            return [-1]


"""Second approach the better one"""


class Solution:
    def duplicates(self, arr, n):
        # code here
        a = [0]*(n+1)
        for i in range(n):
            a[arr[i]] += 1

        j = []
        for i in range(n+1):
            if a[i] > 1:
                j.append(i)

        if len(j) < 1:
            return [-1]
        else:
            return j
        
        

