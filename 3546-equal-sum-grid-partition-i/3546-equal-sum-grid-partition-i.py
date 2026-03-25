class Solution:
    def traverse(self, grid, total, by_column=False):
        x1 = len(grid) if not by_column else len(grid[0])
        x2 = len(grid[0]) if not by_column else len(grid)
        current = 0
        for x in range(x1):
            if x != 0 and total / 2 == current:
                return True
            for y in range(x2):
                current += grid[x if not by_column else y][y if not by_column else x]
        return False

    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(x for row in grid for x in row)
        
        return self.traverse(grid,total) or self.traverse(grid,total,True)