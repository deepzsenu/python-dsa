#
# @lc app=leetcode id=632 lang=python
#
# [632] Smallest Range Covering Elements from K Lists
#

# @lc code=start
import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # Initialize the min_heap to store tuples of (value, list_index, element_index)
        min_heap = []
        max_val = float('-inf')
        current_range = float('inf')
        smallest_range = []
        
        # Initialize the heap with the first element from each list
        for i, lst in enumerate(nums):
            heapq.heappush(min_heap, (lst[0], i, 0))  # (value, list_index, element_index)
            max_val = max(max_val, lst[0])  # Track the maximum element seen so far
        
        while True:
            # Extract the minimum element from the min_heap
            min_val, list_index, element_index = heapq.heappop(min_heap)
            
            # Calculate the current range
            if max_val - min_val < current_range:
                current_range = max_val - min_val
                smallest_range = [min_val, max_val]
            
            # Move to the next element in the list
            element_index += 1
            if element_index >= len(nums[list_index]):
                break  # If the list is exhausted, we can't proceed
            
            # Push the next element from the same list into the min_heap
            next_val = nums[list_index][element_index]
            heapq.heappush(min_heap, (next_val, list_index, element_index))
            max_val = max(max_val, next_val)  # Update the maximum value seen
        
        return smallest_range

        
# @lc code=end

