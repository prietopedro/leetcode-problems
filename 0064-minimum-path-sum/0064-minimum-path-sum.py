class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [0] * n
        dp[0] = grid[0][0]
        for col in range(1, n):
            dp[col] = dp[col - 1] + grid[0][col]

        # Remaining rows
        for row in range(1, m):
            dp[0] += grid[row][0]
            for col in range(1, n):
                dp[col] = min(dp[col], dp[col - 1]) + grid[row][col]

        return dp[-1]