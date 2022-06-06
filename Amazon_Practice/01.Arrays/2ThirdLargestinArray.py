"""Given an array of distinct elements. Find the third largest element in it.

Suppose you have A[] = {1, 2, 3, 4, 5, 6, 7}, 
its output will be 5 because it is the 3 largest element in the array A.

Example 1:

Input:
N = 5
A[] = {2,4,1,3,5}
Output: 3
"""

"""First Method using arr.sort()""" #(Naive Solution)

class Solution:
    def thirdLargest(self,a, n):
        # code here
        a.sort()
        if len(a)>2:
            return a[n-3]
            
        else:
            return -1
        
        
"""Second Method Using Heap"""

import heapq as h
class Solution:
    
    def thirdLargest(self,a, n):
        # code here
        h.heapify(a)
        j = h.nlargest(3,a)
        return min(j)
    
"""Third method Iterative"""
class Solution:
    def thirdLargest(self,a, n):
        # code here
        if len(a)<3:
            return -1
        fi = a[0]
        se = 0
        thi = 0
        for i in range(1,n):
            if a[i]>fi:
                thi = se
                se = fi
                fi = a[i]
                
            elif a[i]>se:
                thi = se
                se = a[i]
            elif a[i]>thi:
                thi = a[i]
                
        return thi
    
    
"""Forth methd iterative and comparision""" #(Naive)
class Solution:
    def thirdLargest(self,a, n):
        fi = a[0]
        se = -1
        th = -1
        for i in range(n):
            if a[i]>fi:
                fi = a[i]
                
        for i in range(n):
            if a[i]>se and a[i]<fi:
                se = a[i]
        for i in range(n):
            if a[i]>th and a[i]<se:
                th = a[i]
                
        return th
