#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    enc = ""
    for c in s:
        if c.isalpha():
            if c.isupper():
                new_letter = ord(c.lower()) + k
                if new_letter > 122:
                    enc += chr(new_letter - 26).upper()
                else:
                    enc += chr(new_letter).upper()
            else:
                new_letter = ord(c) + k
                if new_letter > 122:
                    enc += chr(new_letter - 26)
                else:
                    enc += chr(new_letter)
        else:
            enc += c
    return enc    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
