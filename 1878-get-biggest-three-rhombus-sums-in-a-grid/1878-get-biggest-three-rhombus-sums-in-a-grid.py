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
                best = grid[row][col]
                if best not in seen:
                    best_rows.append(best)
                    best_rows.sort(reverse=True)
                    if len(best_rows) > 3:
                        best_rows.pop()
                seen.add(best)
                max_r = min(col, len(grid[0]) - 1 - col, (len(grid) - 1 - row) // 2)

                for change in range(max_r):
                    s = change + 1  # rhombus "radius"
                    lr, lc = row + s, col - s       # left corner
                    br, bc = row + 2 * s, col       # bottom corner
                    rr, rc = row + s, col + s       # right corner

                    # Start with just the 4 corners
                    total = grid[row][col] + grid[br][bc]

                    # Top-left edge (row,col) -> (lr,lc), excluding endpoints
                    # left[lr][lc] = sum from (row,col) down-left to (lr,lc)
                    total += left[lr][lc] - grid[lr][lc] - left[row][col]

                    # Bottom-left edge (lr,lc) -> (br,bc), excluding endpoints  
                    # right[br][bc] = sum from (lr,lc) area... but easier to use:
                    total += right[br][bc] - grid[br][bc] - right[lr][lc]

                    # Top-right edge (row,col) -> (rr,rc), excluding endpoints
                    total += right[rr][rc] - grid[rr][rc] - right[row][col]

                    # Bottom-right edge (rr,rc) -> (br,bc), excluding endpoints
                    total += left[br][bc] - grid[br][bc] - left[rr][rc]

                    # Add back the corners that got excluded above
                    # left[lr][lc] and right[rr][rc] excluded lr and rr
                    total += grid[lr][lc] + grid[rr][rc]

                    if total not in seen:
                        best_rows.append(total)
                        best_rows.sort(reverse=True)
                        if len(best_rows) > 3:
                            best_rows.pop()
                    seen.add(total)
        return best_rows