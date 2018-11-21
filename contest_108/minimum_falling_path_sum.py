class Solution:
    dp = {}

    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        return min(self.minSum(A, 0, c) for c in range(len(A[0])))

    def minSum(self, A, r, c):
        n = len(A)
        if c < 0 or c > n - 1:
            return float("inf")
        if r == n - 1:
            return A[r][c]
        if (r, c) in self.dp:
            return self.dp[(r, c)]
        self.dp[(r, c)] = A[r][c] + min(self.minSum(A, r + 1, i) for i in [c - 1, c, c + 1])
        return self.dp[(r, c)]


s = Solution()
A = [[-19, 57], [-40, -5]]
print(s.minFallingPathSum(A))
