"""Number of occurrence
BasicAccuracy: 59.34%Submissions: 92236Points: 1
Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.

Example 1:

Input:
N = 7, X = 2
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 4
Explanation: 2 occurs 4 times in the
given array.
Example 2:

Input:
N = 7, X = 4
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 0
Explanation: 4 is not present in the
given array.
Your Task:
You don't need to read input or print anything. Your task is to complete the function count() which takes the array of integers arr, n and x as parameters and returns an integer denoting the answer.

Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
1 ≤ Arr[i] ≤ 106
1 ≤ X ≤ 106"""



def fistOcc(arr, x):
    l = 0
    h = len(arr)-1
    while(l<=h):
        m = (l+h)//2
        if arr[m]<x:
            l = m+1
        elif arr[m]>x:
            h = m-1
        else:
            if m == 0 or arr[m] != arr[m-1]:
                return m
            else:
                h = m-1
    return -1
def lastOcc(arr, x):
    l = 0
    h = len(arr)-1
    while(l<=h):
        m = (l+h)//2
        if arr[m]<x:
            l = m+1
        elif arr[m]>x:
            h = m-1
        else:
            if m == len(arr)-1 or arr[m] != arr[m+1]:
                return m
            else:
                l = m+1
    return -1
class Solution:

	def count(self,arr, n, x):
		# code here
		f = fistOcc(arr,x)
# 		print(f)
		l = lastOcc(arr,x)
# 		print(l)
		if  f== -1:
		    return 0
        else:
            return lastOcc(arr,x)-f +1