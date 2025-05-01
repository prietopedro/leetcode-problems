class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_price = inf
        profit = 0
        for price in prices:
            profit += max(price - current_price,0)
            current_price = price
        return profit
