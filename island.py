class Solution:

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])

        land = 0
        adj = 0
        for r in range(row):
            for c in range(column - 1):
                if grid[r][c] + grid[r][c + 1] == 2:
                    adj += 1
                    land += 1
                elif grid[r][c]:
                    land += 1
            if grid[r][column - 1]:
                land += 1
            print(f"row: {r}, land so far: {land}")

        for c in range(column):
            for r in range(row - 1):
                if grid[r][c] + grid[r + 1][c] == 2:
                    adj += 1

        print(land, adj)
        return 4 * land - 2 * adj


if __name__ == "__main__":
    solution = Solution()
    result = solution.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
    print(result)
