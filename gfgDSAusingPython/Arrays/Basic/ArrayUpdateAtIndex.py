"""Array Update At Index
EasyAccuracy: 90.78%Submissions: 7736Points: 2
You are given an array arr(0-based indexing). The size of the array is given by n. You need to update an element at the given index. The arr[i] of the array is initially set to i+1.

 THAT: You only have to update elements, you don't need to print or return anything. 

Example 1:

Input:
n = 5
index = 4,element = 8
Explanation: Element at 4th index updated to 8
Example 2:

Input:
n = 2
index = 0,element = 99
Explanation: Element at 0th index updated to 99
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function updateArray() that takes arr, n, index, element as parameters and modifies the array arr as per requirements. (element at index is printed by the driver's code)

Expected Time Complexity: O(1).
Expected Auxiliary Space: O(1).

Constraints:
1 <= n<= 103
0 <= element <= 106
0 <= index <= n-1"""

def updateArray(arr,n,idx,element):
    #code here
    arr[idx] = element


