class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        seen = set()

        def dfs(r, c, i):
            if not (0 <= r < rows and 0 <= c < cols):
                return False
            if (r, c) in seen or board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True

            seen.add((r, c))

            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            seen.remove((r, c))
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False