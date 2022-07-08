"""Accuracy: 50.04 Submissions: 19952 Points: 2
Given a non-empty array of integers, find the top k elements which have the
highest frequency in the array. If two numbers have the same frequency then 
the larger number should be given preference. 

Note: Print the elements according to the frequency count (from highest to lowest)
and if the frequency is equal then larger number will be given preference.

Example 1:

Input:
N = 6
nums = {1,1,1,2,2,3}
k = 2
Output: {1, 2}
Example 2:

Input:
N = 8
nums = {1,1,2,2,3,3,3,4}
k = 2
Output: {3, 2}
Explanation: Elements 1 and 2 have the
same frequency ie. 2. Therefore, in this
case, the answer includes the element 2
as 2 > 1.
User Task:
The task is to complete the function topK() that takes the array and integer
k as input and returns a list of top k frequent elements.

Expected Time Complexity : O(NlogN)
Expected Auxilliary Space : O(N)"""
from collections import Counter as cnt
 
def topk(nums , k):
    count  = cnt(nums)
    n = len(nums)
    buc = [[] for i in range(n+1)]
    print(count)
    for key, v in count.items():
        buc[v].append(key)
    print(buc)   
    rev = reversed(buc)
    ans = []
    
    for i in rev:
        i.sort()
        for j in reversed(i):
            print(i)
            ans.append(i)
            if len(ans) == k:
                print(ans)
                
    print(ans)
        
    print(buc)
    # cns  = sorted(count.items())#(sorted(count.items ,key=lambda x:x[1]))
    # # for i in cns:
    # #     print(i, count[i])
    # print(cns)
    # print(count)
    pass

nums = [1,1,1,2,2,2,3]
k = 2
topk(nums , k)

"""from collections import Counter as cnt
import heapq
class Solution:
    
	def topK(self, nums, k):
		#Code here
		d = cnt(nums)
		h = []
		heapq.heapify(h)
		for i in d.keys():
		    heapq.heappush(h, (d[i], i))
            if len(h)> k:
		        heapq.heappop(h)
		        
		ans = []
		while h:
		    c,d = heapq.heappop(h)
		    ans.append(d)
		return ans[::-1]

    


"""