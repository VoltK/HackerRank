#!/bin/python3

import os
import sys
from itertools import zip_longest
#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    
    counter = 0
    for num in range(a[-1], b[0]+1):
        if all(num % x == 0 for x in a) and all(y % num == 0 for y in b):
                counter += 1
    return counter


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
