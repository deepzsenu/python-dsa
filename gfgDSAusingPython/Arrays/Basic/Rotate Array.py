"""
Rotate Array
EasyAccuracy: 37.06%Submissions: 100k+Points: 2
Given an unsorted array arr[] of size N. Rotate the array to the left (counter-clockwise direction) by D steps, where D is a positive integer. 

 

Example 1:

Input:
N = 5, D = 2
arr[] = {1,2,3,4,5}
Output: 3 4 5 1 2
Explanation: 1 2 3 4 5  when rotated
by 2 elements, it becomes 3 4 5 1 2.
Example 2:

Input:
N = 10, D = 3
arr[] = {2,4,6,8,10,12,14,16,18,20}
Output: 8 10 12 14 16 18 20 2 4 6
Explanation: 2 4 6 8 10 12 14 16 18 20 
when rotated by 3 elements, it becomes 
8 10 12 14 16 18 20 2 4 6.
 

Your Task:
Complete the function rotateArr() which takes the array, D and N as input parameters and rotates the array by D elements. The array must be modified in-place without using extra space. 

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= N <= 106
1 <= D <= 106
0 <= arr[i] <= 105"""

def reverseA(arr,s,e):
    while(s<e):
        arr[s], arr[e] = arr[e], arr[s]
        s+=1
        e-=1

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        if D>N:
            D = D%N
        reverseA(A,0,N-1)
        reverseA(A,0,N-D-1)
        reverseA(A,N-D, N-1)