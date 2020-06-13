#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.


def minimumBribes(q):
    result = 0
    for idx, num in enumerate(q):
        if num - 3 > idx:
            return "Too chaotic"
        for i in range(max(num-2, 0), idx):
            if q[i] > num:
                result += 1
    return result


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
