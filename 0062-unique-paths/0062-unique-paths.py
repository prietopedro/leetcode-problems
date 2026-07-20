class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(x,y,m,n):
            if not (0 <= x < m and 0 <= y < n):
                return 0
            if x == m - 1 and y == n - 1:
                return 1
            return dp(x + 1,y,m,n) + dp(x,y + 1,m,n)
        
        return dp(0,0,m,n)
            