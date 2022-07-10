"""14. Find All Four Sum Numbers 
Medium Accuracy: 41.1% Submissions: 61584 Points: 4
Lamp
This problem is part of GFG SDE Sheet. Click here to view more.   
Given an array of integers and another number. Find all the unique quadruple from the given array that sums up to the given number.

Example 1:

Input:
N = 5, K = 3
A[] = {0,0,2,1,1}
Output: 0 0 1 2 $
Explanation: Sum of 0, 0, 1, 2 is equal
to K.
Example 2:

Input:
N = 7, K = 23
A[] = {10,2,3,4,5,7,8}
Output: 2 3 8 10 $2 4 7 10 $3 5 7 8 $
Explanation: Sum of 2, 3, 8, 10 = 23,
sum of 2, 4, 7, 10 = 23 and sum of 3,
5, 7, 8 = 23.
Your Task:
You don't need to read input or print anything. Your task is to complete the function fourSum() which takes the array arr[] and the integer k as its input and returns an array containing all the quadruples in a lexicographical manner. Also note that all the quadruples should be internally sorted, ie for any quadruple [q1, q2, q3, q4] the following should follow: q1 <= q2 <= q3 <= q4.  (In the output each quadruple is separate by $. The printing is done by the driver's code)

Expected Time Complexity: O(N3).
Expected Auxiliary Space: O(N2).

Constraints:
1 <= N <= 100
-1000 <= K <= 1000
-100 <= A[] <= 100"""


class Solution:
    def fourSum(self, arr, k):
        # code here
        result =[]
        arr.sort()
        
        for i in range(len(arr)-3):
            if i>0 and arr[i] == arr[i-1]:
                continue
            
            for j  in range(i+1, len(arr)-2):
                if j>i+1 and arr[j] == arr[j-1]:
                    continue
                
                sum = k-arr[i]-arr[j]
                l = j+1
                r = len(arr)-1
                while l<r:
                    if arr[l]+arr[r]==sum:
                        result.append([arr[i],arr[j],arr[l],arr[r]])
                        
                        while l<r and arr[l]==arr[l+1]:
                            l+=1
                        while l<r and arr[r]==arr[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif arr[l]+arr[r]<sum:
                        l+=1
                    else:
                        r-=1
        return result