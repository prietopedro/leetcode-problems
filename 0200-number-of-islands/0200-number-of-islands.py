class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        m = len(grid)
        n = len(grid[0])
        def dfs(row,col):
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if grid[nr][nc] == "0" or (nr, nc) in seen:
                    continue

                seen.add((nr, nc))
                dfs(nr, nc)
        output = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row,col) not in seen:
                    seen.add((row,col))
                    dfs(row,col)
                    output += 1
        return output