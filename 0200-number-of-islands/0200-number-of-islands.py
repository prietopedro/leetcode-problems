class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        output = 0
        m,n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row,col) not in seen:
                    q = deque([(row,col)])
                    seen.add((row,col))
                    while q:
                        cr,cc = q.popleft()
                        for nr,nc in [(cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)]:
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1" and (nr,nc) not in seen:
                                seen.add((nr,nc))
                                q.append((nr,nc))
                    output += 1
        return output
    
