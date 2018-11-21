#!/usr/bin/env python
"""
https://www.hackerrank.com/challenges/bigger-is-greater/problem
"""

import math
import os
import random
import re
import sys


# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    n = len(w)
    w = list(w)
    if n < 2:
        return "no answer"

    for i in range(n - 2, -1, -1):
        min_dist = sys.maxsize
        e = -1
        for j in range(n - 1, i, -1):
            distance = ord(w[j]) - ord(w[i])
            if distance <= 0:
                continue
            else:
                min_dist = min(min_dist, distance)
                e = j if distance == min_dist else e
        if e != -1:
            print(f"e={e}")
            tmp = w[i]
            w[i] = w[e]
            w[e] = tmp
            s = w[i + 1:]
            s.sort()
            print(f"s={s}")
            return "".join(w[:(i + 1)]) + "".join(s)
        else:
            continue
    return "no answer"


if __name__ == '__main__':
    fptr = open("./output.txt", 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
