class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = 1

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if 0 <= row + 1 < m:
                    dp[row][col] += dp[row + 1][col]
                if 0 <= col + 1 < n:
                    dp[row][col] += dp[row][col + 1]
        return dp[0][0]
            