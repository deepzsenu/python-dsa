"""
14. Stickler Thief 
Easy Accuracy: 50.32 Submissions: 59522 Points: 2
Stickler the thief wants to loot money from a society 
having n houses in a single line. He is a weird person and 
follows a certain rule when looting the houses. 
According to the rule, he will never loot two consecutive houses. 
At the same time, he wants to maximize the amount he loots. 
The thief knows which house has what amount of money but is 
unable to come up with an optimal looting strategy.
He asks for your help to find the maximum money 
he can get if he strictly follows the rule. 
Each house has a[i]amount of money present in it.

Example 1:

Input:
n = 6
a[] = {5,5,10,100,10,5}
Output: 110
Explanation: 5+100+5=110
Example 2:

Input:
n = 3
a[] = {1,2,3}
Output: 4
Explanation: 1+3=4
Your Task:
Complete the functionFindMaxSum()which takes an array arr[] and 
n as input which returns the maximum money he can get following the rules

Expected Time Complexity:O(N).
Expected Space Complexity:O(N).

Constraints:
1 ≤ n ≤ 104
1 ≤ a[i] ≤ 10
"""
"""Failed to pass all the testcase"""
class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        # code here
        s1 = 0
        s2 = 0
        for i in range(0,n,2):
            s1+=a[i]
        for i in range(1,n,2):
            s2+=a[i]
        return max(s1,s2)
    
"""SECOND METHOD"""
class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        # code here
        if n==1:
            return a[0]
        prevprev = a[0]
        prev = max(a[0], a[1])        
        for i in range(2,n):
            curr = max(prev,a[i]+prevprev)
            prevprev = prev
            prev = curr
            
        return prev