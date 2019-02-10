#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    results = {'positive': 0, 'negative': 0, 'zero': 0}
    for x in arr:
        if x > 0:
            results['positive'] += 1
        elif x < 0:
            results['negative'] += 1
        else:
            results['zero'] += 1
    print(round(results['positive']/len(arr), 6))
    print(round(results['negative']/len(arr), 6))
    print(round(results['zero']/len(arr), 6))

    



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
