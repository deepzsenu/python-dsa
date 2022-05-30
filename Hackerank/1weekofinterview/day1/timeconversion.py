#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    l = list(s.split(":"))
    print(l)
    h,m,s,t = (l[0]),(l[1]),(l[2][:2]),l[2][2:]
    if  int(h)<12 and t == "PM":
        h = str(int(h)+12)
    if int(h) == 12 and t =="AM":
        h="00"
    
    st = str(h)+":"+str(m)+":"+str(s)
    return st


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
