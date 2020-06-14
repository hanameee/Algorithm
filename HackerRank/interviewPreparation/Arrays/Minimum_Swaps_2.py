#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


def minimumSwaps(arr):
    arr = [num-1 for num in arr]
    idx_arr = [0 for i in range(len(arr))]
    ck = [0 for i in range(len(arr))]
    for idx, num in enumerate(arr):
        idx_arr[num] = idx
    swaps = 0
    for idx, num in enumerate(arr):
        if idx == num or ck[idx]:
            continue
        while num != idx:
            idx = idx_arr[idx]
            ck[idx] = 1
            swaps += 1
    return swaps


n = int(input())
arr = list(map(int, input().rstrip().split()))
print(minimumSwaps(arr))
