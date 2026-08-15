class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # dp = len(coins) * amount
        # if amount == 0 and i == len(coins):
            # return 0
        # if amount < 0 or i >= len(coins):
            # return 0
        # dp[i][amount] = min(1 + dp[i][amount - coins[i]], dp[i + 1][amount])

        @cache
        def dp(i, amount):
            if amount == 0 and i == len(coins):
                return 0
            if amount < 0 or i >= len(coins):
                return inf
            return min(1 + dp(i,amount - coins[i]), dp(i + 1, amount))
        returning = dp(0,amount)
        print(returning)
        if returning != inf:
            return returning
        return -1