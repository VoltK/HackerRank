#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    highest = max(height)

    if k >= highest:
        return 0
    else:
        return highest - k


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
