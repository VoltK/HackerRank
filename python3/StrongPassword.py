#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count = 0
    if not any(x.isdigit() for x in password):
        count += 1
    if not any(x.isupper() for x in password):
        count += 1
    if not any(x.islower() for x in password):
        count += 1
    if not any(x in "!@#$%^&*()-+" for x in password):
        count += 1
    return max(count,6-n)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
