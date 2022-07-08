"""Medium Accuracy: 33.31% Submissions: 2500 Points: 4
Given a list of points on the 2-D plane and an integer K. The 
task is to find K closest points to the origin and print them.

Note: The distance between two points on a plane is the Euclidean
distance.You are require to prints the points in increasing order of 
their distance from the origin. If two points are at same distance from
origin then print points in sorted order.

Example 1:

Input:
N = 3, K = 2
Points[] = {(3,3),(5,-1),(-2,4)}
Output: 3 3 -2 4
Explanation: Distance between (-2, 4) and
origin is sqrt(20).
Distance between (3, 3) and origin is
sqrt(18).
Distance between (5, -1) and origin is
sqrt(26).
Since two(K) shortest distance from origin
are from points (-2, 4) and (3, 3).
Example 2:

Input:
N = 3, K = 2
Points[] = {(1,3),(-1,3),(5,8)}
Output: -1 3 1 3
Explanation: Distance between (-1, 3) and
origin is sqrt(10).
Distance between (1, 3) and origin is
sqrt(10).
Distance between (5, 8) and origin is
sqrt(89).
Since two(K) shortest distance from origin
are from points (-1, 3) and (1, 3) 
Your Task:
You don't need to read input or print anything. 
Your task is to complete kClosest() function and return 
the 2D array points[][] of size N x 2 denoting the (X,Y)
cooridinates of each point and an integer K. Your task is to return
a 2D array(vector/arraylist depending upon the language you choose) of 
size K x 2 denoting the (X,Y) coordinates of the K-closest points to the origin. 

Expected Time Complexity: O(nLogn)
Expected Auxiliary Space: O(n) 

Constraints: 
1 <= N <= 105
1 <= K <= N
-103 <= (X,Y) <= 103"""

"""GFG Solution"""
"""class Solution:
    def kClosest(self,points,k):
        points.sort(key = lambda x:(x[0]**2+x[1]**2, x))
        return points[:k]
"""

"""Tried the same"""

def kpoint(points, k):
    points.sort(key = lambda x:(x[0]**2+x[1]**2, x))
    # print(points)
    return points[:k]

points  = [[1,3], [-1,3], [5,8]]
k =2

print(kpoint(points,k))

"""Another solution using minheap"""
import heapq
class Solution:
    def kClosest(self,points,k):
        mheap = []
        for x,y in points:
            dist = (x**2)+(y**2)
            mheap.append([dist, x,y])
            
        heapq.heapify(mheap)
        res= []
        while k>0:
            dist, x,y = heapq.heappop(mheap)
            res.append([x,y])
            k-=1
        return res
    