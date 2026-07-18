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
        for coin in coins:
            for i in range(coin,len(dp)):
                dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[-1] if dp[-1] != inf else -1