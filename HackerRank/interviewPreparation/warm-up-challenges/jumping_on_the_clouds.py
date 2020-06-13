#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


# 6
# 0 0 0 0 1 0

def jumpingOnClouds(n, c):
    result = 0
    current_idx = 0
    while True:
        if current_idx == n-1:
            return result
        if current_idx <= n-3 and c[current_idx+2] == 0:
            result += 1
            current_idx += 2
        else:
            result += 1
            current_idx += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
