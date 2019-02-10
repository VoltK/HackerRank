#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    pos = []
    for x in range(a[0], b[0] + 1):
        for num in a:
            if num % x == 0:
                pos.append(x)
    counter = 0
    for x in pos:
        for num in range(len(b)-1):
            if num % x == 0:
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
