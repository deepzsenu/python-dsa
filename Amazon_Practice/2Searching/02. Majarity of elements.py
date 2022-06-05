"""Medium Accuracy: 48.6 Submissions: 100k+ Points: 4
Given an array A of N elements. Find the majority element in the array.
A majority element in an array A of size N 
is an element that appears more than N/2 times in the array.
 

Example 1:

Input:
N = 3 
A[] = {1,2,3} 
Output:
-1
Explanation:
Since, each element in 
{1,2,3} appears only once so there 
is no majority element.
Example 2:

Input:
N = 5 
A[] = {3,1,3,3,2} 
Output:
3
Explanation:
Since, 3 is present more
than N/2 times, so it is 
the majority element.

Your Task:
The task is to complete the function majorityElement()
which returns the majority element in the array.
If no majority exists, return -1.
 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 

Constraints:
1 ≤ N ≤ 107
0 ≤ Ai ≤ 106"""

"""Using hashmap or Counter in python"""


from collections import Counter
class Solution:
    def majorityElement(self, A, N):
        #Your code here
        cnt = Counter(A)
        
        ma = max(cnt.values())
        su  = 0
        co = 0
        for i,v in cnt.items():
            if su < v:
                su = v
                co = i
                
        if su>(N//2):
            return co
            
        else:
            return -1