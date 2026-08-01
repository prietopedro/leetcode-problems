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
            return dp(i, remaining - coins[i]) + dp(i + 1, remaining)
        return dp(0)