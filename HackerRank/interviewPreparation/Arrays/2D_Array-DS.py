#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):
    hSum = []
    for i in range(1, 5):
        for j in range(1, 5):
            hSum.append(arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] +
                        arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1])
    return max(hSum)


arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
print(arr[0][1])
print(hourglassSum(arr))
