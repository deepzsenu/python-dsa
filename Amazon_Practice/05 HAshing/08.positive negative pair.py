"""8. Positive Negative Pair 
Easy Accuracy: 49.71 Submissions: 19798 Points: 2
Given an array of distinct integers, find all the pairs having both negative and positive values of a
number in the array.


Example 1:

Input:
n = 8
arr[] = {1,3,6,-2,-1,-3,2,7}
Output: -1 1 -3 3 -2 2
Explanation: 1, 3 and 2 are present 
pairwise positive and negative. 6 and 
7 have no pair.
Example 2:

Input:
n = 3
arr[] = {3,2,1}
Output: 0
Explanation: No such pair exists so the 
output is 0.

Your Task:
You do not need to read input or print anything. Complete the function findPairs()
which takes the array A[] and the size of the array, n, as input parameters and returns a 
list of integers denoting the pairs. The pair that appears first(i.e. second element of the pair
appears first) in A[] should appear first in the returning list and within the pair, the negative 
integer should appear before the positive integer. Return an empty integer list if no such pair exists.


Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)


Constraints:
1 <= n <= 106
-106 <= arr[i] <= 106"""

class Solution:
    #Function to return list containing all the pairs having both
    #negative and positive values of a number in the array.
    def findPairs(self,arr,n):
        # code here 
        sp = set()
        sn = set()
        ans = []
        for i in arr:
            if i>0:
                sp.add(i)
            else:
                sn.add(i)
                
        for i in arr:
            if i in sp and -i in sn:
                ans.append(-i)
                ans.append(i)
        return ans
                