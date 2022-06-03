"""Given an array(0-based indexing), 
you have to find the max sum of i*A[i] where A[i] is the element at index i in the array.
The only operation allowed is to rotate(clock-wise or counter clock-wise) 
the array any number of times.

Example 1:

Input:
N = 4
A[] = {8,3,1,2}
Output: 29
Explanation: Above the configuration
possible by rotating elements are
3 1 2 8 here sum is 3*0+1*1+2*2+8*3 = 29
1 2 8 3 here sum is 1*0+2*1+8*2+3*3 = 27
2 8 3 1 here sum is 2*0+8*1+3*2+1*3 = 17
8 3 1 2 here sum is 8*0+3*1+1*2+2*3 = 11
Here the max sum is 29 
Your Task:
Your task is to complete the function max_sum which takes two arguments 
which is the array A [ ] and its size and returns an integer value denoting the required max sum.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).


"""
""" DOES NOT WORK 
def rev(arr,s,e):
    while s<=e:
        arr[s],arr[e] = arr[e], arr[s]
        s+=1
        e-=1
    
def rotate(arr,n,k):
    rev(arr,0,n-1)
    rev(arr,0,n-k-1)
    rev(arr,n-k, n-1)
def max_sum(a,n):
    #code here
    sum_=0
    for i in range(n):
        s = 0
        rotate(arr,n,i)
        for i in range(len(arr)):
            s += arr[i]*i
        sum_ = max(sum_,s)
        
    return sum_
    """
    
import math
def max_sum(arr,n):
    #code here
    sum_ = 0
    ans  = - math.inf
    temp  = 0
    for i in range(n):
        sum_+=arr[i]
        temp+=arr[i]*i
        
    ans = temp
    for i in range(n):
        temp+= sum_-(n*arr[n-1-i])
        ans = max(temp, ans)
        
    return ans
