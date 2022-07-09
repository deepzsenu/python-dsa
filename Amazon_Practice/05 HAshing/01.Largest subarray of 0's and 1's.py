"""1. Largest subarray of 0's and 1's 
Easy Accuracy: 38.92 Submissions: 67270 Points: 2
Given an array of 0s and 1s. Find the length of the
largest subarray with equal number of 0s and 1s.

Example 1:

Input:
N = 4
A[] = {0,1,0,1}
Output: 4
Explanation: The array from index [0...3]
contains equal number of 0's and 1's.
Thus maximum length of subarray having
equal number of 0's and 1's is 4.
Example 2:

Input:
N = 5
A[] = {0,0,1,0,0}
Output: 2
Your Task:
You don't need to read input or print anything.
Your task is to complete the function maxLen() which takes the array arr[] 
and the size of the array as inputs and returns the length of the largest 
subarray with equal number of 0s and 1s.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 105
0 <= A[] <= 1"""

"""GFG solution """

class Solution:
    def maxLen(self,arr, N):
        # code here
        hashmap = {0:-1}
        total_sum = 0
        for i in range(N):
            if arr[i]== 0:
                arr[i] = -1
        pre_sum = 0
        res = 0 
        
        for i in range(N):
            pre_sum +=arr[i]
            if pre_sum in hashmap:
                res = max(res, abs(i-hashmap[pre_sum]))
                
            else:
                hashmap[pre_sum] = i
                
        return res

"""Brute force"""
# A simple program to find the largest subarray
# with equal number of 0s and 1s

# This function Prints the starting and ending
# indexes of the largest subarray with equal
# number of 0s and 1s. Also returns the size
# of such subarray.
def findSubArray(arr, n):

	sum = 0
	maxsize = -1

	# Pick a starting point as i

	for i in range(0, n-1):
	
		sum = -1 if(arr[i] == 0) else 1

		# Consider all subarrays starting from i

		for j in range(i + 1, n):
		
			sum = sum + (-1) if (arr[j] == 0) else sum + 1

			# If this is a 0 sum subarray, then
			# compare it with maximum size subarray
			# calculated so far

			if (sum == 0 and maxsize < j-i + 1):
				
				maxsize = j - i + 1
				startindex = i
			
		
	
	if (maxsize == -1):
		print("No such subarray");
	else:
		print(startindex, "to", startindex + maxsize-1);

	return maxsize

# Driver program to test above functions
arr = [1,0, 1,1,1,1,1,0]#[1, 0, 0, 1, 0, 1, 1]
size = len(arr)
findSubArray(arr, size)


"""Using hashing"""

# Python 3 program to find largest
# subarray with equal number of
# 0's and 1's.

# Returns largest subarray with
# equal number of 0s and 1s
def maxLen(arr, n):

	# NOTE: Dictionary in python in
	# implemented as Hash Maps.
	# Create an empty hash map (dictionary)
	hash_map = {}
	curr_sum = 0
	max_len = 0
	ending_index = -1

	for i in range (0, n):
		if(arr[i] == 0):
			arr[i] = -1
		else:
			arr[i] = 1

	# Traverse through the given array
	for i in range (0, n):
	
		# Add current element to sum
		curr_sum = curr_sum + arr[i]

		# To handle sum = 0 at last index
		if (curr_sum == 0):
			max_len = i + 1
			ending_index = i

		# If this sum is seen before,
		if curr_sum in hash_map:
			
			# If max_len is smaller than new subarray
			# Update max_len and ending_index
			if max_len < i - hash_map[curr_sum]:
				max_len = i - hash_map[curr_sum]
				ending_index = i
		else:

			# else put this sum in dictionary
			hash_map[curr_sum] = i
		
	for i in range (0, n):
		if(arr[i] == -1):
			arr[i] = 0
		else:
			arr[i] = 1
			
	print (ending_index - max_len + 1, end =" ")
	print ("to", end = " ")
	print (ending_index)

	return max_len

# Driver Code
arr = [1, 0, 0, 1, 0, 1, 1]
n = len(arr)

maxLen(arr, n)
	
# This code is contributed


