"""5. Count distinct elements in every window 
Easy Accuracy: 44.16 Submissions: 83026 Points: 2
Lamp
This problem is part of GFG SDE Sheet. Click here to view more.   
Given an array of integers and a number K. Find the count of distinct elements in every
window of size K in the array.

Example 1:

Input:
N = 7, K = 4
A[] = {1,2,1,3,4,2,3}
Output: 3 4 4 3
Explanation: Window 1 of size k = 4 is
1 2 1 3. Number of distinct elements in
this window are 3. 
Window 2 of size k = 4 is 2 1 3 4. Number
of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number
of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number
of distinct elements in this window are 3.
Example 2:

Input:
N = 3, K = 2
A[] = {4,1,1}
Output: 2 1
Your Task:
Your task is to complete the function countDistinct() which takes the array A[], 
the size of the array(N) and the window size(K) as inputs and returns an array containing the
count of distinct elements in every contiguous window of size K in the array A[].

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= K <= N <= 105
1 <= A[i] <= 105 , for each valid i"""

from collections import  Counter as cn
"""Complexity O(N-k)*K """
def count(arr, n, k):
    ans  = []
    for i in range((n-k)+1):
        m = arr[i:i+k]
        # print(m)
        mas = cn(m)
        # print(mas, len(mas))
        ans.append(len(mas))
        
    return ans
        
arr = [1,2,1,3,4,2,3]
n = 7
k = 4
print(count(arr, n,k))
"""Optimal solution with O(N)"""
class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        ans  = []
        dis= {}
        j = 0
        for i in range(N):
            if A[i] not in dis:
                dis[A[i]] = 1
            else:
                dis[A[i]]+=1
            if i>=k-1:
                ans.append(len(dis.keys()))
                if dis[A[j]]>1:
                    dis[A[j]] -=1
                else:
                    del dis[A[j]]
                j+=1
        return ans