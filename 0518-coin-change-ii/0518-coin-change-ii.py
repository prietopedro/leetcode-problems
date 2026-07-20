class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(i,left):
            if left == 0:
                return 1
            if left < 0:
                return 0
            if i >= len(coins):
                return 0
            output = dp(i, left - coins[i]) + dp(i + 1, left)
            return output
        return dp(0,amount)