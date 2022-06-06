"""Medium Accuracy: 51.7 Submissions: 12054 Points: 4
Lamp
This problem is part of GFG SDE Sheet. Click here to view more.
Given a collection of Intervals, the task is to merge all of the overlapping Intervals.

Example 1:

Input:
Intervals = {{1,3},{2,4},{6,8},{9,10}}
Output: {{1, 4}, {6, 8}, {9, 10}}
Explanation: Given intervals: [1,3],[2,4]
[6,8],[9,10], we have only two overlapping
intervals here,[1,3] and [2,4]. Therefore
we will merge these two and return [1,4],
[6,8], [9,10].
Example 2:

Input:
Intervals = {{6,8},{1,9},{2,4},{4,7}}
Output: {{1, 9}}
Your Task:
Complete the function overlappedInterval()
that takes the list N intervals as input parameters
and returns sorted list of intervals after merging.

Expected Time Complexity: O(N*Log(N)).
Expected Auxiliary Space: O(Log(N)) or O(N).

Constraints:
1 ≤ N ≤ 100
0 ≤ x ≤ y ≤ 1000"""


class Solution:
    def overlappedInterval(self, Int):
        Int.sort()
        res = []
        res.append(Int[0])
        j = 0
        for i in range(len(Int)):
            if Int[i][0] <= res[j][1]:
                res[j][1] = max(Int[i][1], res[j][1])
                
            else:
                res.append(Int[i])
                j += 1
            
        return res