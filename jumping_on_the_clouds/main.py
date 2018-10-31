#!/usr/bin/env python

import math
import os
import random
import re
import sys
"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

The solution for this is:
1. an array of clouds could be dividec into multiple segments, 0001000100100 can be divided into 0001, 0001, 001, 00
2. set a zero_start_index and zero_end_index and each segment will take  math.ceil((zero_end_index - zero_start_index) / 2) + 1 steps to get over the 1 to the next segment
3. the last segment takes steps: math.ceil((zero_end_index - zero_start_index) / 2)
"""

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    zero_start_index, zero_end_index = 0, 0
    step_counter = 0
    for i in range(len(c)):
        if c[i] == 1:
            zero_end_index = i - 1
            step_counter += math.ceil((zero_end_index - zero_start_index) / 2) + 1
            zero_start_index = i + 1

    zero_end_index = len(c) - 1
    step_counter += math.ceil((zero_end_index - zero_start_index) / 2)

    return step_counter


if __name__ == '__main__':

    fptr = open("./output.txt", 'w')

    n = int(input("Please input the number of the clouds: "))
    print("Please input the sequence of clouds as '0'(safe) or '1'(not safe): ")
    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
