"""11. Smallest Positive missing number 
Medium Accuracy: 45.14 Submissions: 23964 Points: 4
Given an array arr[] of size N, find the smallest positive number missing from the array.

 

Example 1:

Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 6
Explanation: Smallest positive missing
number is 6.
 

Example 2:

Input:
N = 5
arr[] = {0,-10,1,3,-20}
Output: 2
 

Your Task:
You don't need to read input or print anything. 
The task is to complete the function findMissing() which takes arr 
and N as input parameters and returns the smallest positive missing number.

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= N <= 106
-106 <= arr[i] <= 106"""

class Solution:
    def findMissing(self,arr, size): 
    # your code goes here
        mini = 1
        for i in range(size):
            if arr[i]>0:
                p = (arr[i]-1)%size
                if arr[p]>arr[i] or arr[p]<=0:
                    arr[p], arr[i] = arr[i], arr[p]
                    
        for i in range(size):
            if arr[i] == mini:
                mini+=1
        return mini