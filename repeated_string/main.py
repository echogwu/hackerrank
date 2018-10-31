#!/usr/bin/env python

import math
import os
import random
import re
import sys
"""
https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

"""


# Complete the repeatedString function below.
def repeatedString(s, n):
    single_around, indexed_a_counter = number_of_a_by_index(s, n % len(s))
    return single_around * (n // len(s)) + indexed_a_counter


def number_of_a_by_index(s, end_index):
    total_a_counter, indexed_a_counter = 0, 0
    index = 0
    for x in iter(s):
        index += 1
        if x == "a":
            total_a_counter += 1
            if index <= end_index:
                indexed_a_counter += 1
    return total_a_counter, indexed_a_counter


if __name__ == '__main__':

    fptr = open("./output.txt", 'w')

    s = input("Please input the repeating string of letters, for instance 'dbcad': ")

    n = int(input("please input which letters do you want to search the letter 'a': "))

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
