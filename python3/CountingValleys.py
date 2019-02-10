#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    steps = {"U": 1, "D": -1}
    valley = 0
    al = 0
    for step in s:
        al += steps[step]
        if al == 0 and step == "U":
            valley += 1
    return valley



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
