#!/usr/bin/env python

import math
import os
import random
import re
import sys
"""
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

The solution for this is:
1. convert uphill to +1 and downhill to -1, all the steps will become a list of [-1, 1, 1, -1, ...]
2. what makes a valley starting point is sum(0..i)=0 and sum(0..i+1)=-1. What makes a valley ending point is sum(0..j)<0 and sum(0..j+1)=0
3. considering the number of the steps could be up to 10^6, use generator to not take up all the space to store the list elements
4. there might be staring point but no ending point, so use min(staring_counter, ending_counter)
"""


# Complete the countingValleys function below.
def countingValleys(n, s):
    s = map(lambda x: 1 if x == "U" else -1, s)
    valley_starting_counter = 0
    valley_ending_counter = 0
    sub_sum_behind = 0
    sub_sum = 0
    for x in s:
        sub_sum_behind = sub_sum
        sub_sum += x
        if sub_sum_behind == 0 and sub_sum < 0:
            valley_starting_counter += 1
        if sub_sum_behind < 0 and sub_sum == 0:
            valley_ending_counter += 1

    return min(valley_starting_counter, valley_ending_counter)


if __name__ == '__main__':
    fptr = open("./output.txt", 'w')

    n = int(input("please input the number of total steps: "))

    s = input("please input the steps, 'U' means uphill, 'D' means downhill like 'UUDDDUDU': ")

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
