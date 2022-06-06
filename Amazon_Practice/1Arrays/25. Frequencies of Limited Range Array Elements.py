"""25. Frequencies of Limited Range Array Elements 
Easy Accuracy: 47.5 Submissions: 89689 Points: 2
Given an array A[] of N positive integers which can contain integers
from 1 to P where elements can be repeated or can be absent from the array.
Your task is to count the frequency of all elements from 1 to N.
Note: The elements greater than N in the array can be ignored for 
counting and please read your task section of the problem carefully 
to understand how to output the array.


Example 1:

Input:
N = 5
arr[] = {2, 3, 2, 3, 5}
P = 5
Output:
0 2 2 0 1
Explanation: 
Counting frequencies of each array element
We have:
1 occurring 0 times.
2 occurring 2 times.
3 occurring 2 times.
4 occurring 0 times.
5 occurring 1 time.
Example 2:

Input:
N = 4
arr[] = {3,3,3,3}
P = 3
Output:
0 0 4 0
Explanation: 
Counting frequencies of each array element
We have:
1 occurring 0 times.
2 occurring 0 times.
3 occurring 4 times.
4 occurring 0 times.

Your Task:
Complete the function frequencycount() 
that takes the array and n as input parameters and modify the array itself
in place to denote the frequency count of each element from 1 to N. i,e
element at index 0 should represent the frequency of 1 and so on.


Note: Can you solve this problem without using extra space (O(1) Space) !


Constraints:
1 ≤ N ≤ 105
1 ≤ P ≤ 4*104 
1 <= A[i] <= P"""


"""Using Dictionaries"""
from collections import Counter as cnt
class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        m = cnt(arr)
        j =0
        for i in range(1,N+1):
            if i not in m:
                arr[j] = 0
            else:
                arr[j] = m[i]
            j+=1
            
            
"""SEcond approach with Constant space"""      
class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        counti = 0
        for i in range(N):
            if arr[i]>N:
                arr[i] = 0
                counti+=1
                
            else:
                arr[i]-=1
            
        for i in range(N):
            arr[arr[i]%N]+=N
            
        for i in range(N):
            if i ==0:
                arr[i] = arr[i]-(N*counti)
            arr[i]//=N     
            
            
