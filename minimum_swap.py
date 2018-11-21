#!/bin/usr/env python
"""
https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen
"""

import math
import os
import random
import re
import sys
import time


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)
    if n in (0, 1):
        return 0
    return swap(arr, 0, n)


def swap(arr, start, end):
    print(f"array to be swapped: {arr[start: end]}, start={start}, end={end}")
    # time.sleep(3)
    if end - start <= 1:
        return 0

    if end - start == 2:
        if arr[start] != start + 1:
            arr[start], arr[end - 1] = arr[end - 1], arr[start]
            print(f"after swapping between 2 elements sub array: {arr}")
            return 1
        else:
            return 0

    pivot, swap_pivot = pickPivot(arr, start, end)
    print(f"pivot: {pivot}")
    swap_sort = quickSort(arr, start, end, pivot)
    swap_left = swap(arr, start, pivot)
    swap_right = swap(arr, pivot + 1, end)
    return swap_pivot + swap_sort + swap_left + swap_right


# def pickPivot(arr, start, end):
#     middle_value = (end + start) // 2 + 1
#     supposed_pos_for_middle_value = middle_value - 1
#     pos_for_middle_value = -1
#     for index in range(start, end):
#         if arr[index] == middle_value:
#             pos_for_middle_value = index
#         if arr[index] == index + 1:
#             return index, 0
#     arr[pos_for_middle_value], arr[supposed_pos_for_middle_value] = \
#     arr[supposed_pos_for_middle_value], arr[pos_for_middle_value]
#     print(f"after picking the pivot: {arr}")
#     return supposed_pos_for_middle_value, 1


def pickPivot(arr, start, end):
    middle_value = (end + start) // 2 + 1
    supposed_pos_for_middle_value = middle_value - 1
    pos_for_middle_value = -1
    for index in range(start, end):
        if arr[index] == middle_value:
            pos_for_middle_value = index
            break
        # if arr[index] == index + 1:
        #     return index, 0
    if arr[supposed_pos_for_middle_value] == middle_value:
        return supposed_pos_for_middle_value, 0
    else:
        arr[pos_for_middle_value], arr[supposed_pos_for_middle_value] = \
        arr[supposed_pos_for_middle_value], arr[pos_for_middle_value]
        print(f"after picking the pivot: {arr}")
        return supposed_pos_for_middle_value, 1


def quickSort(arr, start, end, pivot):
    print(f"quick sort arr: {arr[start:end]}")
    swaps = 0
    left, right = start, end - 1
    while left < pivot and pivot < right:
        while arr[left] < arr[pivot]:
            left += 1
        while arr[right] > arr[pivot]:
            right -= 1
        if left < pivot and right > pivot:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            print(f"after quick sort: {arr}")
            swaps += 1
        else:
            break
    print(f"after quick sort: {arr[start: end]}")
    return swaps


if __name__ == '__main__':
    tests = [
        # [4, 3, 1, 2],
        # [2, 3, 4, 1, 5],
        [1, 3, 5, 2, 4, 6, 7],
        [
            2, 31, 1, 38, 29, 5, 44, 6, 12, 18, 39, 9, 48, 49, 13, 11, 7, 27, 14, 33, 50, 21, 46, 23, 15, 26, 8, 47, 40,
            3, 32, 22, 34, 42, 16, 41, 24, 10, 4, 28, 36, 30, 37, 35, 20, 17, 45, 43, 25, 19
        ],
    ]
    expected_result = [3, 46]
    for test, exp in zip(tests, expected_result):
        print(f"============={test}: {exp}=======")
        res = minimumSwaps(test)
        print(res)
        assert res == exp
    # swap = []
    # print(test(swap))
    # print(test(swap))
    # print(test(swap))
    # print(test(swap))
