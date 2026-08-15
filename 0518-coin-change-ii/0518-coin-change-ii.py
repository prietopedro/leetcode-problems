class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(i, total = 0):
            if total == amount:
                return 1
            if i >= len(coins) or total > amount:
                return 0
            
            return dp(i, total + coins[i]) + dp(i + 1, total)
        return dp(0)