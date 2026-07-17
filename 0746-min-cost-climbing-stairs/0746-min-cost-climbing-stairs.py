class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def rec(i):
            if i >= len(cost):
                return 0
            return min(cost[i] + rec(i + 1), cost[i] + rec(i + 2))
        return min(rec(0),rec(1))