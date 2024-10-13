#
# @lc app=leetcode id=2406 lang=python
#
# [2406] Divide Intervals Into Minimum Number of Groups
#

# @lc code=start
class Solution:
    def minGroups(self, intervals):
        events = []
        
        # Create events for the start and end of each interval
        for interval in intervals:
            events.append((interval[0], 1))  # Start of an interval (+1 to active count)
            events.append((interval[1] + 1, -1))  # End of an interval (-1 to active count)

        # Sort events: first by time, second by type (end before start for same time)
        events.sort()
        
        active = 0
        max_active = 0
        
        # Sweep through events
        for time, event in events:
            active += event
            max_active = max(max_active, active)
        
        return max_active

        
        
# @lc code=end

