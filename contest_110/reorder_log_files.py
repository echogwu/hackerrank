"""
https://leetcode.com/contest/weekly-contest-110/problems/reorder-log-files/
"""
from collections import OrderedDict


class Solution(object):

    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        if len(logs) == 0:
            return []
        digits = []
        letters = []
        tmp = []

        for log in logs:
            print(log)
            value = log.split(maxsplit=1)
            if ord(value[1][0]) > 122 or ord(value[1][0]) < 97:
                digits.append(log)
            else:
                s = value[1] + " " + value[0]
                tmp.append(s)
        tmp.sort()
        for letter in tmp:
            value = letter.split()
            letter = value[-1] + " " + " ".join(value[:-1])
            letters.append(letter)
        return letters + digits


logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
expected = ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
s = Solution()
print(s.reorderLogFiles(logs))
