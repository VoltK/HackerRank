#!/bin/python3

import math
import os
import random
import re
import sys
import calendar

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if calendar.isleap(year) or ((year <= 1917) & (year%4 == 0)):
        date = f'12.09.{str(year)}'
    elif year == 1918:
        date = '26.09.1918'
    else:
        date = f'13.09.{str(year)}'
    return date


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
