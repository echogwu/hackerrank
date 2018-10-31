#!/usr/bin/env python

import math
import os
import random
import re
import sys
"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""


# Complete the rotLeft function below.
def rotLeft(a, d):
    return a[d:] + a[:d]


if __name__ == '__main__':
    fptr = open("./output.txt", 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()