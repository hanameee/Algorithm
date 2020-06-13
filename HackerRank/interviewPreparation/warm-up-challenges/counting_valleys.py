#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.


def countingValleys(n, s):
    total_sum = 0
    result = 0
    for i in range(0, n):
        if s[i] == "U":
            total_sum += 1
        else:
            total_sum -= 1
        if total_sum == 0 and s[i] == "U":
            result += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
