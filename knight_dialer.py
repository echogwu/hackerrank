"""
https://leetcode.com/problems/knight-dialer/
"""


class Solution:
    m = {
        (1, 1): [6, 8],
        (2, 1): [7, 9],
        (3, 1): [4, 8],
        (4, 1): [0, 3, 9],
        (5, 1): [],
        (6, 1): [0, 1, 7],
        (7, 1): [2, 6],
        (8, 1): [1, 3],
        (9, 1): [2, 4],
        (0, 1): [4, 6],
    }

    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 10
        total = 0
        for i in range(10):
            total += self.getDistinctNumbers(i, N - 1)
        return total

    def getDistinctNumbers(self, start_pos: int, hops: int):
        if hops == 1:
            return len(self.m[(start_pos, 1)])
        s = 0
        for i in self.m[(start_pos, 1)]:
            if (i, hops - 1) in self.m:
                if type(self.m[(i, hops - 1)]) == list:
                    s += len(self.m[(i, hops - 1)])
                else:
                    s += self.m[(i, hops - 1)]
            else:
                s += self.getDistinctNumbers(i, hops - 1)
        self.m[(start_pos, hops)] = s
        return s


s = Solution()
inp = [1, 2, 3]
exp = [10, 20, 46]
for i, e in zip(inp, exp):
    print(i, e)
    assert s.knightDialer(i) == e, f"i={i}, e={e}, reality={s.knightDialer(i)}"
