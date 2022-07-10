"""7. First Non Repeating Character 
Easy Accuracy: 59.25% Submissions: 2077 Points: 2
Given a string S consisting of lowercase Latin Letters. Find the first non-repeating character in S.

Example 1:

Input:
N = 5
S = hello
Output: h
Explanation: 'h', 'e' and 'o' are the
non-repeating characters out of which
'h' has the least index.
Example 2:

Input:
N = 12
S = zxvczbtxyzvy
Output: c
Explanation: 'c', 'b' and 't' are the
non-repeating characters out of which
'c' has the least index.
Your Task:
You don't need to read input or print anything. Your task is to complete the function find() which takes the string S as its input and returns the first non-repeating character present in S or -1 if there is no non-repeating character. Since the return type is a string we first need to change the character into a string.

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(|S|)."""

from collections import Counter as cnt
def find(S):
    # code here
    cn= cnt(S)
    
    for i in S:
        if cn[i] == 1:
            return i
    return -1

