#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = {}
    for sock in ar:
        pairs[sock] = pairs.get(sock,0) + 1
    amount = 0
    for val in pairs.values():
        if val != 1:
            if val % 2 == 0:
                amount += val // 2
            else:
                amount += (val - 1) // 2
    return amount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
