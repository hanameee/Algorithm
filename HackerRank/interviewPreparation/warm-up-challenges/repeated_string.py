#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
# aba
# 10


def repeatedString(s, n):
    a_count = 0
    a_arr = [0]
    for i in range(len(s)):
        if s[i] == "a":
            a_count += 1
        a_arr.append(a_count)
    div, mod = divmod(n, len(s))
    result = div*a_arr[-1] + a_arr[mod]
    return result


s = input()

n = int(input())

print(repeatedString(s, n))
