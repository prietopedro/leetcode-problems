class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        NEI = [(1,0), (-1,0), (0,1), (0,-1)]
        m,n = len(grid), len(grid[0])
        def dfs(row,col):
            paths = 0
            for dr,dc in NEI:
                nr,nc = row + dr, col + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if (nr,nc) in seen or not grid[nr][nc]:
                    continue
                seen.add((nr,nc))
                paths += dfs(nr,nc)
            return 1 + paths

        best = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] not in seen and grid[row][col]:
                    seen.add((row,col))
                    best = max(best, dfs(row,col))
        return best