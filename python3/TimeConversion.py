#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s.endswith('PM'):
        if s[:2] == '12':
            new = s[:-2]
        else:
            new = str(int(s[:2]) + 12) + s[2:-2]
    else:
        if s[:2] == '12':
            new = "00" + s[2:-2]
        else:
            new = s[:-2]
    return new

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
