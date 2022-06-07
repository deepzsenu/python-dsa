"""Medium Accuracy: 45.44% Submissions: 44164 Points: 4
Given an unsorted array arr[] of n positive integers. 
Find the number of triangles that can be formed with three
different array elements as lengths of three sides of triangles. 

Example 1:

Input: 
n = 3
arr[] = {3, 5, 4}
Output: 
1
Explanation: 
A triangle is possible 
with all the elements 5, 3 and 4.
Example 2:

Input: 
n = 5
arr[] = {6, 4, 9, 7, 8}
Output: 
10
Explanation: 
There are 10 triangles
possible  with the given elements like
(6,4,9), (6,7,8),...
 

Your Task: 
This is a function problem. You only need to complete the function 
findNumberOfTriangles() that takes arr[] and n as input parameters
and returns the count of total possible triangles.

Expected Time Complexity: O(n2).
Expected Space Complexity: O(1)"""
class Solution:
    #Function to count the number of possible triangles.
    def findNumberOfTriangles(self, arr, n):
        #code here
        arr.sort()
        ans =0
        for i in range(n):
            k = i+2
            for j in range(i+1, n):
                while k<n and arr[k]<arr[i]+arr[j]:
                    k+=1
                ans +=k-(j+1)
                
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findNumberOfTriangles(arr,n))

# } Driver Code Ends