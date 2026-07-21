class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        def dfs(x,y,m,n):
            if not (0 <= x < m and 0 <= y < n):
                return
            if grid[x][y] == '0' or (x,y) in seen:
                return
            seen.add((x,y))

            return dfs(x + 1,y,m,n) or dfs(x - 1, y,m,n) or dfs(x, y + 1,m,n) or dfs(x, y - 1,m,n)
        m,n = len(grid),len(grid[0])
        output = 0
        for row in range(m):
            for col in range(n):
                output += grid[row][col] == "1" and (row,col) not in seen
                dfs(row,col,m,n)
        return output