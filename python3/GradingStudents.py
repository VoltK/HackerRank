#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    updated = []

    for grade in grades:
        if grade < 38:
            updated.append(grade)
        else:
            mult_5 = (x for x in range(grade, 101) if x % 5 == 0)
            for mult in mult_5:
                if mult - grade < 3:
                    rounded = grade + (mult - grade)
                    updated.append(rounded)
                elif mult - grade == 3:
                    updated.append(grade)

         
    return updated

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
