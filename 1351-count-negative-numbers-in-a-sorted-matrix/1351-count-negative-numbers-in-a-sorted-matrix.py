class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        total = 0
        for row in range(n):
            low = 0
            high = n 
            while low < high:
                middle = (low + high) // 2
                if grid[row][middle] >= 0:
                    low = middle + 1
                else:
                    high = middle
            total += n - low
            
        return total
            