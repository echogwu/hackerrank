#!/usr/bin/env python

import math
import os
import random
import re
import sys
"""
https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

"""


# Complete the hourglassSum function below.
def hourglassSum(arr):
    largest = -sys.maxsize - 1
    for row in range(4):
        for col in range(4):
            largest = max(
                largest, arr[row][col] + arr[row][col + 1] + arr[row][col + 2] + arr[row + 1][col + 1] +
                arr[row + 2][col] + arr[row + 2][col + 1] + arr[row + 2][col + 2]
            )

    return largest


if __name__ == '__main__':
    fptr = open("./output.txt", 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
