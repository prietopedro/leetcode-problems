class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(i,remaining = amount):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            if i >= len(coins):
                return 0
            output = dp(i + 1, remaining)
            if remaining - coins[i] >= 0:
                output += dp(i, remaining - coins[i])
            return output
        return dp(0)

