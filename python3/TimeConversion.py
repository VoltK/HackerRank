#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s.endswith('PM'):
        new = str(int(s[:2]) + 12) + s[2:-2]
    else:
        new = int(s[:2]) + s[2:-2]
    return new

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
