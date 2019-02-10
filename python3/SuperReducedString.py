#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    new = ""
    for letter in s:
        if new and new[-1] == letter:
            new = new[:-1]
        else:
            new += letter
    
    if new:
        return new
    else:
        return "Empty String"
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
