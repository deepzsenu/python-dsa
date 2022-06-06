"""20. Container With Most Water 
Medium Accuracy: 53.18% Submissions: 11121 Points: 4
Given N non-negative integers a1,a2,....an where each represents a point at coordinate (i, ai).
N vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i,0).
Find two lines, which together with x-axis forms a container, such that it contains the most water.

Example 1:

Input:
N = 4
a[] = {1,5,4,3}
Output: 6
Explanation: 5 and 3 are distance 2 apart.
So the size of the base = 2. Height of
container = min(5, 3) = 3. So total area
= 3 * 2 = 6.
Example 2:

Input:
N = 5
a[] = {3,1,2,4,5}
Output: 12
Explanation: 5 and 3 are distance 4 apart.
So the size of the base = 4. Height of
container = min(5, 3) = 3. So total area
= 4 * 3 = 12.
Your Task :
You only need to implement the given function maxArea. 
Do not read input, instead use the arguments given in the function and return the desired output. 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
2<=N<=105
1<=A[i]<=100
    """
    
    
"""Brute Force aPproach"""

def maxArea(A,n):
    #code here
    water = 0
    r = n-1
    while r>=0:
        l = 0 
        while l<r:
            water =max(water, (min(A[r], A[l])*(r-l)))
            l+=1
        r-=1
        
    return water


"""OPtimal Approach using two pointers"""




def maxArea(arr,n):
    #code here
    water = 0
    left = 0
    right = n-1
    while left<right:
        water = max(water, min(arr[left], arr[right])*(right-left))
        
        if arr[left]<arr[right]:
            preleft = arr[left]
            while arr[left]<=preleft and left<right:
                left+=1
        
        else:
            preright = arr[right]
            while arr[right]<=preright and left<right:
                right-=1
                
    return water