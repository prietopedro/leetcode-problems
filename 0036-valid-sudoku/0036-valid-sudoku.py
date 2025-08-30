class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = 9
        row_seen = defaultdict(set)
        col_seen = defaultdict(set)
        quad_seen = defaultdict(set)
        numbers = {'1','2','3','4','5','6','7','8','9'}
        for x in range(m):
            for y in range(m):
                q_x = x // 3
                q_y = y // 3
                if board[x][y] in numbers:
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
0,0

[
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".","9","."],
    [".",".",".","5","6",".",".",".","."],
    ["4",".","3",".",".",".",".",".","1"],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]]
