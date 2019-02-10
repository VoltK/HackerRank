#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    counter1 = 0
    for x in range(1, n):
        if x == p:
            break
        if x % 2 != 0:
            counter1 += 1
        
    counter2 = 0
    for x in range(n, 0, -1):
        if x == p:
            break
        if  x % 2 == 0:
            counter2 += 1
        
    return min(counter1, counter2)

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
