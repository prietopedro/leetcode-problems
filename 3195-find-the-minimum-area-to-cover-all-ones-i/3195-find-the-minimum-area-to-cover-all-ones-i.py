class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        min_x,max_x = m - 1,0
        min_y,max_y = n - 1,0
        for x in range(m):
            for y in range(n):
                if grid[x][y] != 1: continue
                min_x = min(x,min_x)
                min_y = min(y,min_y)
                max_x = max(x,max_x)
                max_y = max(y,max_y)
        print(min_x,max_x)
        print(min_y,max_y)
        return (max_x - min_x + 1) * (max_y - min_y + 1)
                
