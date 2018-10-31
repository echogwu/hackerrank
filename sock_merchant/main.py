#!/usr/bin/env python

import math
import os
import random
import re
import sys
from collections import Counter
"""
https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    if len(ar) != n:
        return 0
    counter = dict(Counter(ar))
    result = 0
    for _, v in counter.items():
        result += v // 2
    return result


if __name__ == '__main__':

    fptr = open("./output.txt", 'w')

    n = int(input("please input the number of socks: "))
    print("please input the color of the socks represented by number, like '10 20 30 50 10': ")

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
