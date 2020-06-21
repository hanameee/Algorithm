#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.


def rotLeft(a, d):
    newA = a[d:] + a[0:d]
    result = " ".join(map(str, newA)).rstrip()
    return result


nd = input().split()
n = int(nd[0])
d = int(nd[1])
a = list(map(int, input().rstrip().split()))
print(rotLeft(a, d))
