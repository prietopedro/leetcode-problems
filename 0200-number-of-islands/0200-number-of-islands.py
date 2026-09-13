class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        m = len(grid)
        n = len(grid[0])
        def dfs(row,col):
            nonlocal m,n
            if (row,col) in seen:
                return
            if not (0 <= row < m and 0 <= col < n):
                return
            if grid[row][col] == "0":
                return
            seen.add((row,col))
            dfs(row + 1, col) 
            dfs(row - 1, col) 
            dfs(row, col + 1) 
            dfs(row, col - 1)
            return
        output = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row,col) not in seen:
                    print(row,col)
                    dfs(row,col)
                    output += 1
        return output