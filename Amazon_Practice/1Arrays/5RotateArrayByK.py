"""Given an unsorted array arr[] of size N. Rotate the array to the left
(counter-clockwise direction) by D steps, where D is a positive integer. 

 

Example 1:

Input:
N = 5, D = 2
arr[] = {1,2,3,4,5}
Output: 3 4 5 1 2
Explanation: 1 2 3 4 5  when rotated
by 2 elements, it becomes 3 4 5 1 2.
    """
    
#User function Template for python3
def rev(A, s, e):
    while s<e:
        A[s], A[e] = A[e], A[s]
        s+=1
        e-=1
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        if D>N:
            D = D%N
        rev(A,0,N-1)
        rev(A,0,N-D-1)
        rev(A,N-D, N-1)
        
"""SECOND METHOD"""

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        if D>N:
            D = D%N
        ii = 0
        itcount =0 
        while itcount<N:
            i = ii
            storeval = A[i]
            while itcount<N:
                itcount+=1
                ti = (i-D+N)%N
                tempStoreval = A[ti]
                A[ti] = storeval
                i = ti
                storeval = tempStoreval
                if ii == i:
                    break
            ii+=1
            
"""Third""" #but it will create a new list
from collections import deque
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        dq = deque(A)
        dq.rotate(-D)
        A = list(dq)
        print(A)        