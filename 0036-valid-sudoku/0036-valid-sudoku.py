class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = 9
        row_seen = defaultdict(set)
        col_seen = defaultdict(set)
        quad_seen = defaultdict(set)
        for x in range(m):
            for y in range(m):
                q_x = x // 3
                q_y = y // 3
                if board[x][y] != '.':
                    if board[x][y] in row_seen[x]:
                        return False
                    if board[x][y] in quad_seen[(q_x,q_y)]:
                        return False
                    if board[x][y] in col_seen[y]:
                        return False
                    col_seen[y].add(board[x][y])
                    quad_seen[(q_x,q_y)].add(board[x][y])
                    row_seen[x].add(board[x][y])

        return True