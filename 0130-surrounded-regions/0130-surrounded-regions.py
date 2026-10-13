class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        q = deque([])
        for row in range(m):
            if board[row][0] == "O":
                q.append((row,0))
            if board[row][n - 1] == "O":
                q.append((row,n - 1))
        for col in range(n):
            if board[0][col] == "O":
                q.append((0,col))
            if board[m - 1][col] == "O":
                q.append((m - 1, col))
        DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            row,col = q.popleft()
            board[row][col] = "S"

            for dr,dc in DIRECTIONS:
                nr,nc = dr + row, dc + col
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if board[nr][nc] == "O":
                    board[nr][nc] = "S"
                    q.append((nr,nc))


        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "S":
                    board[row][col] = "O"
