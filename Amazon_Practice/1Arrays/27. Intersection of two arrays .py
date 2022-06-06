"""27. Intersection of two arrays 
Easy Accuracy: 45.86 Submissions: 62333 Points: 2
Given two arrays a[] and b[] respectively of size n and m, the task is to print the count
of elements in the intersection (or common elements) of the two arrays.

For this question, the intersection of two arrays can be defined as the set containing distinct 
common elements between the two arrays. 

Example 1:

Input:
n = 5, m = 3
a[] = {89, 24, 75, 11, 23}
b[] = {89, 2, 4}

Output: 1

Explanation: 
89 is the only element 
in the intersection of two arrays.
Example 2:

Input:
n = 6, m = 5
a[] = {1, 2, 3, 4, 5, 6}
b[] = {3, 4, 5, 6, 7} 

Output: 4

Explanation: 
3 4 5 and 6 are the elements 
in the intersection of two arrays.
Your Task:
You don't need to read input or print anything. 
Your task is to complete the function NumberofElementsInIntersection() 
which takes two integers n and m and their respective arrays a[] and b[]  as input
. The function should return the count of the number of elements in the intersection.

 

Expected Time Complexity: O(n + m).
Expected Auxiliary Space: O(min(n,m)).

Constraints:
1 ≤ n, m ≤ 105
1 ≤ a[i], b[i] ≤ 105"""
# """1. Uisng array""" (m*logn)
class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
        set_ = []
        for i in range(n):
            if a[i] in b and a[i] not in set_  :
                set_.append((a[i]))
                
        for i in range(m):
            if b[i] in a and b[i] not in set_:
                set.append((b[i]))
                
        return len(set_)
    
"""2. comparing elements"""

class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
        a.sort()
        b.sort()
        i = 0
        j = 0
        se= []
        while (i < n and j < m):
     
            if (a[i] > b[j]):
                j += 1
     
            else:
                if (b[j] > a[i]):
                    i += 1
     
                else:
                    se.append(a[i])
                    i += 1
                    j += 1
        return len(se)

"""3. Using SET Properties"""
#O(N)
class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
        s1 = set(a)
        s2 = set(b)
        intr = (s1&s2)
        
        return len(intr)
    
""""""