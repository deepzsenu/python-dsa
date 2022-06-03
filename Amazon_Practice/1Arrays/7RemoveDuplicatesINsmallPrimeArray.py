"""
Given an array consisting of only prime numbers, remove all duplicate numbers from it. 

Example 1:

Input:
N = 6
A[] = {2,2,3,3,7,5}
Output: 2 3 7 5
Explanation: After removing the duplicate
2 and 3 we get 2 3 7 5
"""
# this solution doesnot work as the array is not sorted 
"""class Solution:
    def removeDuplicates(self, arr):
        # code her
        i =0 
        j = 1
        while i<len(arr) and j<len(arr): 
            if arr[i]== arr[j]:
                arr.pop(j)
            else:
                j+=1
                i+=1
        return arr """
        
"""next"""

#worked but it has some extra space of (O)n that is not required
class Solution:
    def removeDuplicates(self, arr):
        # code her
        A = []
        for i in arr:
            if i not in A:
                A.append(i)
        return A
    
# so let's think of different approach:
"""efficient than the above approach but uses extra space
coz we are using dic for comparing and dic uses internal hashing that makes this solutionn efficient
than above solution"""
class Solution:
    def removeDuplicates(self, arr):
        # code her
        d = dict()
        l = []
        for i in arr:
            if i not in d:
                d[i] =1
                l.append(i)                
                
        return l
