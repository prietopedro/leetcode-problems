class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m,n = len(grid),len(grid[0])
        DIRECTIONS = [(0,1),(1,0),(0,-1),(-1,0)]
        q = deque([])
        fresh_oranges = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    q.append((row,col,0))
                if grid[row][col] == 1:
                    fresh_oranges += 1
        max_time = 0
        while q:
            row,col,time = q.popleft()
            max_time = max(max_time,time)
            print(row)
            for dr,dc in DIRECTIONS:
                nr,nc = dr + row, dc + col
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if grid[nr][nc] != 1:
                    continue
                grid[nr][nc] = 2
                fresh_oranges -= 1
                q.append((nr,nc, time + 1))

        return max_time if not fresh_oranges else -1