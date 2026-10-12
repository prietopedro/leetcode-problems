class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        seen = set()
        m,n = len(grid),len(grid[0])
        diff = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(row,col):
            if not (0 <= row < m and 0 <= col < n):
                return 0
            if grid[row][col] == "0" or (row,col) in seen:
                return 0

            seen.add((row,col))
            for rd,cd in diff:
                dfs(row + rd, col + cd)

            return 1 

        output = 0
        for row in range(m):
            for col in range(n):
                output += dfs(row,col)
        return output