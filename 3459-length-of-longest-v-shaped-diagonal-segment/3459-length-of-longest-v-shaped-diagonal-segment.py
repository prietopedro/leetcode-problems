class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        @cache
        def dp(row,col,currentDirection,hasMadeTurnYet,prev):
            nonlocal m,n
            if not (0 <= row < m and 0 <= col < n):
                return 0

            target = ''
            if prev == 2:
                target = '0'
            elif prev == 0 or prev == 1:
                target = '2'

            if str(grid[row][col]) not in target and prev != None:
                return 0

            best = 0
            directions = [(-1,-1),(-1,1),(1,1),(1,-1)]
            dx,dy = directions[currentDirection]
            best = max(best,1 + dp(row + dx, col + dy, currentDirection, hasMadeTurnYet, grid[row][col]))
            if not hasMadeTurnYet:
                next_direction = (i + 1) % 4
                dx,dy = directions[next_direction]
                best = max(best,1 + dp(row + dx, col + dy, next_direction, True, grid[row][col]))
                              
            return best

        best = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] != 1:
                    continue
                for i in range(4):
                    best = max(best, dp(row,col,i,False,None))
        return best

        [1,1,1,2,0,0],
        [0,0,0,0,1,2]

        # -1,-1 -> -1,1
        # -1,1 -> 1,1
        # 1,1 -> 1,-1
        # 1,-1 -> -1,-1