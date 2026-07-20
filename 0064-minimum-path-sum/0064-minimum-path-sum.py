class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[inf for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for row in range(m):
            for col in range(n):
                if 0 <= row - 1 < m:
                    dp[row][col] = min(dp[row][col],dp[row - 1][col] + grid[row][col])
                if 0 <= col - 1 < n:
                    dp[row][col] = min(dp[row][col],dp[row][col - 1] + grid[row][col])
        return dp[-1][-1]