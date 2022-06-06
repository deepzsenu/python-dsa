"""You are given an array A, of N elements. Find minimum index based distance between 
two elements of the array, x and y.

Example 1:

Input:
N = 4
A[] = {1,2,3,2}
x = 1, y = 2
Output: 1
Explanation: x = 1 and y = 2. There are
two distances between x and y, which are
1 and 3 out of which the least is 1.
    """

"""METHOD ONE"""


class Solution:
    def minDist(self, arr, n, x, y):
        
        if x not in arr or y not in arr:
            return -1

        min_dist = 10000000000000  # or math.inf
        x_index = -1
        y_index = -1

        for idx, item in enumerate(arr):
            if item == x:
                x_index = idx
            elif item == y:
                y_index = idx
            if x_index != -1 and y_index != -1:
                curr_dis = abs(y_index - x_index)
                min_dist = min(min_dist, curr_dis)

        return min_dist


"""This is also same as the above one """


class Solution:
    def minDist(self, arr, n, x, y):
        if(x not in arr or y not in arr):
            return -1

        mini = 10000000000000000000
        a, b = -1, -1
        for i in range(n):
            if(arr[i] == x):
                a = i
            if(arr[i] == y):
                b = i
            if(a != -1 and b != -1):
                mini = min(mini, abs(a-b))
        return mini
