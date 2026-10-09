class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        
        seen = set()
        def dfs(row,col,i):
            if i >= len(word):
                return True
            if not (0 <= row < m and 0 <= col < n):
                return False
            if board[row][col] != word[i] or (row,col) in seen:
                return False
            seen.add((row,col))
            val = (
                dfs(row + 1, col, i + 1) or
                dfs(row - 1, col, i + 1) or
                dfs(row, col + 1, i + 1) or
                dfs(row, col - 1, i + 1)
            )
            seen.remove((row,col))
            return val
        for row in range(m):
            for col in range(n):
                if dfs(row,col,0):
                    return True
        return False