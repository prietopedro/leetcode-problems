class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m,n = len(grid),len(grid[0])
        visited = set()
        def dfs(row,col):
            if not (0 <= row < m and 0 <= col < n):
                return 0
            if grid[row][col] == 0 or (row,col) in visited:
                return 0
            visited.add((row,col))
            return 1 + (
                dfs(row + 1,col) +
                dfs(row - 1,col) +
                dfs(row, col + 1) +
                dfs(row, col - 1)
            )
        best = 0
        for row in range(m):
            for col in range(n):
                best = max(best,dfs(row,col))
        return best
