#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    for q in queries:
        arr[q[0]-1] += q[2]
        arr[q[1]] -= q[2]
    answer = 0
    cumulative_sum = 0
    for value in arr:
        cumulative_sum += value
        answer = max(answer, cumulative_sum)
    return answer


nm = input().split()
n = int(nm[0])
m = int(nm[1])
queries = []
for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))
result = arrayManipulation(n, queries)


print(result)
