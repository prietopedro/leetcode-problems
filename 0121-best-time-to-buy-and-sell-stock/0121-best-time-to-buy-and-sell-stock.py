class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = inf
        max_profit = 0
        for num in prices:
            min_val = min(min_val, num)
            max_profit = max(max_profit, num - min_val)
        return max_profit