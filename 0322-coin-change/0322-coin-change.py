class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # @cache
        # def minAmount(coinsLeft):
            
        #     if coinsLeft == 0:
        #         return 0
        #     if coinsLeft < 0:
        #         return inf

        #     best = inf
        #     for coin in coins:
        #         best = min(best,1 + minAmount(coinsLeft - coin))
            
        #     return best
        # best = minAmount(amount)
        # return best if best != inf else -1

        dp = [inf] * (amount + 1)
        dp[0] = 0
        for i in range(1,len(dp)):
            for coin in coins:
                if i < coin:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != inf else -1