"""Easy Accuracy: 46.94 Submissions: 100k+ Points: 2
Lamp
This problem is part of GFG SDE Sheet. Click here to view more.   
Given an array having both positive and negative integers. The task is to compute the length of the
largest subarray with sum 0.

Example 1:

Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.
Your Task:
You just have to complete the function maxLen() which takes two arguments an array A and n,
where n is the size of the array A and returns the length of the largest subarray with 0 sum.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 105
-1000 <= A[i] <= 1000, for each valid i"""



"""The solution is same as the question no 1"""

def findmax(arr, n):
    d = {}
    sum_arr = 0
    max_i = 0
    for i in range(n):
        sum_arr +=arr[i]
        if sum_arr ==  0:
            max_i = i+1
            
        if sum_arr not in d:
            d[sum_arr] = i
        else:
            if i-d[sum_arr] > max_i:
                print(max_i, end = " ")
                max_i = i-d[sum_arr]
                print(max_i)
                
    print(d)
    return max_i

arr =  [15,-2,2,-8,1,7,10,23] #[1,2,-1,-2,3,-1,-2, 4 , 5]
n = len(arr)
print(arr)
print(findmax(arr, n))
        