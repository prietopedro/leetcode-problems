class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        n,m = sorted([n,m])
        return k * (m - k) if m > k else 0