#!/usr/bin/env python

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the getWays function below.
def getWays(n, c):
    idx = defaultdict(lambda: -1)
    print(n, c, idx)
    return getCombos(c, idx, 0, n)


def getCombos(c, idx, s, t):
    print(f"start from index {s}, total should be {t}")
    if t <= 0 or t <= c[s]:
        return 0
    if idx[s, t] != -1:
        return idx[s, t]
    tmp = 0
    for i in range(s, len(c)):
        for j in range(i, len(c)):
            print(f"i: {i}, j: {j}")
            tmp += getCombos(c, idx, j, t - c[j])
    idx[s, t] = tmp
    print(idx)
    return tmp


if __name__ == '__main__':
    fptr = open("./output.txt", 'w')

    # nm = input().split()
    #
    # n = int(nm[0])
    #
    # m = int(nm[1])
    #
    # c = list(map(int, input().rstrip().split()))
    n = 2
    m = 2
    c = [1, 2]

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.close()
