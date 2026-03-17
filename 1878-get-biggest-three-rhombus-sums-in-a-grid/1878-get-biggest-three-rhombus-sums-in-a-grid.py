class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        left = [row[:] for row in grid]
        right = [row[:] for row in grid]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row != 0 and col != len(grid[0]) - 1:
                    left[row][col] = left[row - 1][col + 1] + grid[row][col]
                if col != 0 and row != 0:
                    right[row][col] = right[row - 1][col - 1] + grid[row][col]

        best_rows = []
        seen = set()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                max_r = min(col, len(grid[0]) - 1 - col, (len(grid) - 1 - row) // 2)
                for change in range(max_r + 1):
                    if change != 0:
                        s = change
                        lr, lc = row + s, col - s       
                        br, bc = row + 2 * s, col       
                        rr, rc = row + s, col + s
                        total = grid[row][col] + grid[br][bc]
                        total += left[lr][lc] - grid[lr][lc] - left[row][col]
                        total += right[br][bc] - grid[br][bc] - right[lr][lc]

                        total += right[rr][rc] - grid[rr][rc] - right[row][col]

                        total += left[br][bc] - grid[br][bc] - left[rr][rc]

                        total += grid[lr][lc] + grid[rr][rc]
                    else:
                        total = grid[row][col]

                    if total not in seen:
                        best_rows.append(total)
                        best_rows.sort(reverse=True)
                        if len(best_rows) > 3:
                            best_rows.pop()
                    seen.add(total)
        return best_rows