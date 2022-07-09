"""4. Match specific pattern 
Easy Accuracy: 51.27 Submissions: 16701 Points: 2
Given a dictionary of words and a pattern. Every character in the pattern is uniquely 
mapped to a character in the dictionary. Find all such words in the dictionary that match the given pattern. 

Example 1:

Input:
N = 4
dict[] = {abb,abc,xyz,xyy}
pattern  = foo
Output: abb xyy
Explanation: xyy and abb have the same
character at index 1 and 2 like the
pattern.
Your Task:
You don't need to read input or print anything. Your task is to complete the function
findMatchedWords() which takes an array of strings dict[] consisting of the words in the dictionary and 
a string, Pattern and returns an array of strings consisting of all the words in the dict[] that match the 
given Pattern in lexicographical order.

Expected Time Complexity: O(N*K) (where K is the length of the pattern).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 10"""

"""GFG solution"""
def check(word):
    d ={}
    res =""
    i =0
    for ch in word:
        if ch not in d:
            d[ch] = i
            i+=1
        res+=str(d[ch])
    return res
def findSpecificPattern(Dict, pattern):
    #Code here
    j = []
    l = len(pattern)
    h = check(pattern)
    for word in Dict:
        if len(word) == l and check(word) == h:
            j.append(word)
            
    return j


"""Articals"""

link = "https://www.geeksforgeeks.org/find-all-strings-that-match-specific-pattern-in-a-dictionary/"