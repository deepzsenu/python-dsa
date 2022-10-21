"""Get Element At Index
BasicAccuracy: 58.67%Submissions: 12245Points: 1
You are given an array arr(0-based indexing). The size of the array is given by n. You need to get the element at index i and return it. If no element exists at i then return -1.

Example 1:

Input:
n = =6
arr[] = {1 2 3 4 5 6}
index = 0
Output: 1
Explanation: The array is {1 2 3 4 5 6}.
The index given is 0. so element at 0th
index is 1.
Example 2:

Input:
n = 4
arr[] = {1 2 3 4}
index = 4
Output: -1
Explanation: The array is {1 2 3 4}. The
index given is 4. Here no element exists
at the 4th index, so the answer is -1.
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function getByIndex() that takes arr, n, i as input and return the required result. The driver code takes care of the printing.

Expected Time Complexity: O(1).
Expected Auxiliary Space: O(1).

Constraints:
1 <= n<= 103
0 <= arri <= 106
1 <= index <= 106"""

def getByIndex(arr,n,idx):
    # return required ans
    if idx <= n:
        return arr[idx]

    else:
        return -1

#{
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        idx=int(input())
        
        print(getByIndex(arr,n,idx))
# } Driver Code Ends