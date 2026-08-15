class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # dp = len(coins) * amount
        # if amount == 0 and i == len(coins):
            # return 0
        # if amount < 0 or i >= len(coins):
            # return 0
        # dp[i][amount] = min(1 + dp[i][amount - coins[i]], dp[i + 1][amount])

        # @cache
        # def dp(i, amount):
        #     if amount == 0 and i == len(coins):
        #         return 0
        #     if amount < 0 or i >= len(coins):
        #         return inf
        #     return min(1 + dp(i,amount - coins[i]), dp(i + 1, amount))
        # returning = dp(0,amount)
        # if returning != inf:
        #     return returning
        # return -1
        dp = [[inf] * (amount + 1) for _ in range(len(coins) + 1)]

        # amount = 0 requires 0 coins, regardless of which coins remain
        for i in range(len(coins) + 1):
            dp[i][0] = 0

        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, amount + 1):
                # Don't take coins[i]
                dp[i][j] = dp[i + 1][j]

                # Take coins[i]
                if j >= coins[i]:
                    dp[i][j] = min(
                        dp[i][j],
                        1 + dp[i][j - coins[i]]
                    )

        return dp[0][amount] if dp[0][amount] != inf else -1
