#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    colorDict = {}
    result = 0
    for color in ar:
        if color in colorDict:
            colorDict[color] += 1
        else:
            colorDict[color] = 1
    keys = colorDict.keys()
    for key in keys:
        result += colorDict[key]//2
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
