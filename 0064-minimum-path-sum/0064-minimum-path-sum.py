class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions_cost = [[inf for _ in range(n)] for _ in range(m)]
        directions_cost[0][0] = grid[0][0]
        h = [(grid[0][0],0,0)]
        seen = set([(0,0)])
        directions = [(0,1),(1,0)]
        while h:
            cost,row,col = heapq.heappop(h)
            for xr,xc in directions:
                nr,nc = row + xr,col + xc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] + cost < directions_cost[nr][nc]:
                    val = grid[nr][nc] + cost
                    directions_cost[nr][nc] = val
                    heapq.heappush(h,(val,nr,nc))
        return directions_cost[-1][-1]