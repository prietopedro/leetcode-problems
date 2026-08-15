class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # @cache
        # def dp(i, total = 0):
        #     if total == amount:
        #         return 1
        #     if i >= len(coins) or total > amount:
        #         return 0
            
        #     return dp(i, total + coins[i]) + dp(i + 1, total)
        # return dp(0)
        n = amount + 1
        m = len(coins) + 1

        dp = [[0] * n for _ in range(m)]

        # total == amount -> 1 way, regardless of i
        for i in range(m):
            dp[i][amount] = 1

        for i in range(m - 2, -1, -1):
            for j in range(amount - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]

                if j + coins[i] <= amount:
                    dp[i][j] += dp[i][j + coins[i]]

        return dp[0][0]
                