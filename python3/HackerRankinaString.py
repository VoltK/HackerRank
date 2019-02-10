#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    flag = "NO"
    for word in combinations(s, 10):
        if "".join(word) == 'hackerrank':
            flag = 'YES'
    return flag   


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
