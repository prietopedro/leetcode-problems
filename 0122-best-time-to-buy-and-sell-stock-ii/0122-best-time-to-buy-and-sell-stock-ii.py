class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        current_price = prices[0]
        profit = 0
        for price in prices:
            profit += max(price - current_price,0)
            current_price = price
        return profit
