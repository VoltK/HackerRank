#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):

    fall_apple = [a + x for x in apples]
    fall_orange = [b + x for x in oranges]

    total = {'apples': 0, 'oranges': 0}

    for apple in fall_apple:
        if apple in range(s, t+1):
            total['apples'] += 1
    
    for orange in fall_orange:
        if orange in range(s, t+1):
            total['oranges'] += 1
    
    print(total['apples'])
    print(total['oranges'])



if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
