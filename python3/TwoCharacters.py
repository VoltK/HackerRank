 #!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the alternate function below.
def alternate(s):
    lng = 0
    for comb in combinations(set(s), 2):
       string = "".join(x for x in s if x in comb)
       if all(string[x-1] != string[x] for x in range(1, len(string))):
           lng = max(lng, len(string))
    return lng
       

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
