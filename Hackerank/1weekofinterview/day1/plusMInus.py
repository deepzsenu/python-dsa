#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = []
    p = []
    j = []
    for i in arr:
        if i >0:
            p.append(i)
        if i<0:
            n.append(i)
        if  i==0:
            j.append(i)
            
    ns = len(arr)
    po = len(p)/ns
    no = len(n)/ns
    so = len(j)/ns
    print(po)
    print(no)
    print(so)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
