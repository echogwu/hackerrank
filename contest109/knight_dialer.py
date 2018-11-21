class Solution:
    map = {
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
        0: [4, 6],
    }

    memo = {}

    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 10
        sum = 0
        for i in range(0, 10):
            sum += self.knightDialerFromOneNumber(i, N - 1)
        return sum % (pow(10, 9) + 7)

    def knightDialerFromOneNumber(self, pos, hops):
        if pos == 5:
            return 0
        if (pos, hops) not in self.memo:
            if hops == 1:
                self.memo[(pos, 1)] = len(self.map[pos])
            else:
                sum = 0
                for i in self.map[pos]:
                    sum += self.knightDialerFromOneNumber(i, hops - 1)
                self.memo[(pos, hops)] = sum
        return self.memo[(pos, hops)]


s = Solution()
print(s.knightDialer(1))
print(s.knightDialer(2))
print(s.knightDialer(3))
