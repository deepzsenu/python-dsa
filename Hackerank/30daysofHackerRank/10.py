#!/bin/python3

import math
import os
import random
import re
import sys


n = int(input())
j = "{0:b}".format((n))
s = j.replace("0", " ")
j = list(map(str, s.split(" ")))
m = max(j)
print(len(m))
