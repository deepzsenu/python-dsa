"""
11. Mountain Subarray Problem 
Easy Accuracy: 28.76% Submissions: 5807 Points: 2
We are given an array of integers and a range, we need 
to find whether the subarray which falls in this range
has values in the form of a mountain or not. All values
of the subarray are said to be in the form of a mountain 
if either all values are increasing or decreasing or first 
increasing and then decreasing. More formally a subarray [a1, a2, a3 … aN]
is said to be in form of a mountain if there exists an integer K, 1 <= K <= N such that,
a1 <= a2 <= a3 .. <= aK >= a(K+1) >= a(K+2) …. >= aN
You have to process Q queries. In each query you are given two integer L
and R, denoting starting and last index of the subarrays respectively.

Example 1:

Input:
N = 8
a[] = {2,3,2,4,4,6,3,2}
Q = 2
Queries = (0,2), (1,3)
Output:
Yes
No
Explanation: For L = 0 and R = 2, a0 = 2,
a1 = 3 and a2 = 2, since they are in the
valid order,answer is Yes.
For L = 1 and R = 3, a1 = 3, a2 = 2 and
a3 = 4, since a1 > a2 and a2 < a4 the
order isn't valid, hence the answer is
No.
Your Task:

Complete the function processQueries() which takes the array,
size of array queries and number of queries as parameter. 
It should return a vector/ArrayList/array (depending upon language cpp/Java/Python) of boolean values, 
true if the subarray is in mountain form, false otherwise. The driver code will print "Yes"
if the returned value is true, otherwise "No".

Expected Time Complexity: O(N + Q).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N, Q <= 105
1 <= a[i] <= 106, for each valid i
0 <= L <= R <= N-1
"""

"""
    did not work for all test cases
    
    """
    

class Solution:
    def processqueries(self,arr,n,m,q):
        # code here
        string = ["No"]*m
        for i in range(m):
            
            s = q[i][0]
            e = q[i][1]
            while s<e:
                if arr[s]>arr[s+1]:
                    break
                s+=1
            while(s<e):
                if arr[s]<arr[s+1]:
                    break;
                s+=1
            if s == e:
                string[i] ="Yes"
        return string
    
    
"""OPtimal Approach"""



class Solution:
    def processqueries(self,arr,n,m,q):
        # code here
        l = [-1]*n
        r = [-1]*n
        l[0] =0
        lastInc =0
        for i in range(1,n):
            if arr[i] > arr[i-1]:
                lastInc = i
            l[i] = lastInc
            
        r[n-1] = n-1
        firstDec = n-1
        for i in range(n-2, -1,-1):
            if arr[i]>arr[i+1]:
                firstDec = i
            r[i] = firstDec
            
        ans = []
        
        for i in range(m):
            left = q[i][0]
            rig = q[i][1]
            if r[left]>=l[rig]:
                ans.append("Yes")
            else:
                ans.append("No")
                
        return ans
