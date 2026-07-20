class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # @cache
        # def dp(i,left):
        #     if left == 0:
        #         return 1
        #     if left < 0:
        #         return 0
        #     if i >= len(coins):
        #         return 0
        #     output = dp(i, left - coins[i]) + dp(i + 1, left)
        #     return output
        # return dp(0,amount)

        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(n - 1, -1, -1):
            for left in range(amount + 1):
                take = dp[i][left - coins[i]] if left >= coins[i] else 0
                skip = dp[i + 1][left]
                dp[i][left] = take + skip
        return dp[0][amount]