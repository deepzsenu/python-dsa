"""

Array Delete And Shift
EasyAccuracy: 67.98%Submissions: 9678Points: 2
You are given an array arr(0-based indexing). The size of the array is given by n. You need to delete an element at given index and print the modified array. The arr[i] of array is initially set to i+1.
Deletion means you need to shift all the elements after that index to the left by 1 position and set the last element as zero.

Example 1:

Input:
n = 5
index = 0
Output: 2 3 4 5 0
Example 2:

Input:
n = 6
index = 3
Output: 1 2 3 5 6 0
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function deleteFromArray() that takes arr, n, index as parameters and modifies the array arr as per requirements. 

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 <= n<= 103
0 <= index <= n-1"""

def deleteFromArray(arr,n,idx):
    #code here
    del arr[idx]
    arr.append(0)

