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

        if amount == 0:
            return 1
        n = amount + 1
        m = len(coins) + 1

        dp = [0] * n 
        dp[amount] = 1

        for i in range(m - 2, -1, -1):
            next_dp = [0] * n
            for j in range(amount - 1, -1, -1):
                next_dp[j] = dp[j]
                next_dp[amount] = 1

                if j + coins[i] <= amount:
                    next_dp[j] += next_dp[j + coins[i]]
            dp = next_dp

        return dp[0]
                