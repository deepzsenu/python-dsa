"""26. Union of Two Sorted Arrays 
Easy Accuracy: 46.19 Submissions: 66562 Points: 2
Union of two arrays can be defined as the common and distinct elements in the two arrays.
Given two sorted arrays of size n and m respectively, find their union.


Example 1:

Input: 
n = 5, arr1[] = {1, 2, 3, 4, 5}  
m = 3, arr2 [] = {1, 2, 3}
Output: 1 2 3 4 5
Explanation: Distinct elements including 
both the arrays are: 1 2 3 4 5.
 

Example 2:

Input: 
n = 5, arr1[] = {2, 2, 3, 4, 5}  
m = 5, arr2[] = {1, 1, 2, 3, 4}
Output: 1 2 3 4 5
Explanation: Distinct elements including 
both the arrays are: 1 2 3 4 5.
 

Example 3:

Input:
n = 5, arr1[] = {1, 1, 1, 1, 1}
m = 5, arr2[] = {2, 2, 2, 2, 2}
Output: 1 2
Explanation: Distinct elements including 
both the arrays are: 1 2.

Your Task: 
You do not need to read input or print anything. 
Complete the function findUnion() that takes two arrays arr1[], arr2[],
and their size n and m as input parameters and returns a
list containing the union of the two arrays. 
 

Expected Time Complexity: O(n+m).
Expected Auxiliary Space: O(n+m).
 

Constraints:
1 <= n, m <= 105
1 <= arr[i], brr[i] <= 106
"""

"""Using Set and sorting naive approach"""
class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def mergeArrays(self,a,b,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here  
        
        s= set()
        
        for i in a:
            s.add(i)
        for i in b:
            s.add(i)
            
        return sorted(s)