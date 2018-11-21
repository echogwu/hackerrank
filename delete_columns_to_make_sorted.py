"""
https://leetcode.com/contest/weekly-contest-111/problems/delete-columns-to-make-sorted/
"""


class Solution:

    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        m = len(A)
        if m in (0, 1):
            return 0
        n = len(A[0])
        counter = 0

        for i in range(n):
            s = A[0][i]
            flag = False
            for j in range(1, m):
                if s <= A[j][i]:
                    s = A[j][i]
                    continue
                else:
                    flag = True
                    break
            if flag:
                counter += 1

        return counter


A = ["zyx", "wvu", "tsr"]
s = Solution()
print(s.minDeletionSize(A))
