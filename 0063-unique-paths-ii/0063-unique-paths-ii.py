class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        if m == 1 and n == 1:
            return int(obstacleGrid[0][0] != 1)
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * n for _ in range(m)]
        dp[-1][-1] = 1
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if 0 <= row + 1 < m and obstacleGrid[row + 1][col] == 0:
                    dp[row][col] += dp[row + 1][col]
                if 0 <= col + 1 < n and obstacleGrid[row][col + 1] == 0:
                    dp[row][col] += dp[row][col + 1]
        return dp[0][0] 