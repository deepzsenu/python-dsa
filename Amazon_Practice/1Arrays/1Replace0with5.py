"""
You are given an integer N. You need to convert all zeroes of N to 5.

Example 1:

Input:
N = 1004
Output: 1554
Explanation: There are two zeroes in 1004
on replacing all zeroes with "5", the new
number will be "1554".
"""
"""Method 1 Uisng string"""
def convertFive(n):
    #Code here
    
    return int(str(n).replace("0","5"))

"""Second Method using modulo operator"""
def convertFive(n):
    # Code here
    new_num = n
    change_num = 0
    j = 1
    while new_num>0:
        r = new_num%10
        if r == 0 :
            r = 5
        change_num+=r*j
        j = j*10
        new_num//=10
    return change_num