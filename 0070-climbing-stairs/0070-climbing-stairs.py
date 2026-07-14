class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1: 1, 2: 2}
        def rec(n, cache):
            if n in cache:
                return cache[n]
            cache[n] = rec(n - 1,cache) + rec(n - 2,cache)
            return cache[n]
        return rec(n,cache)