class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        min_cost = 0
        cost.sort()
        bought = 0
        for i in range(len(cost) - 1, -1, -1):
            if bought == 2:
                bought = 0
                continue
            min_cost += cost[i]
            bought += 1
        return min_cost
            