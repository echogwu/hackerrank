class Solution:

    red = set()
    blue = set()

    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        empty = True
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1 and empty:
                    red.add((i,j))
                elif A[i][j] == 1 and

    def isAdjecent(A, i, j):
        if i -1 >= 0 and A[i-1][j] == 1:
            if (i-1, j) in red:
                return "r"
            else:
                return "b"
