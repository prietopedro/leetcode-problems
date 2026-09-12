class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(x,y,i, seen):
            if not (0 <= x < len(board) and 0 <= y < len(board[0])):
                return False
            if board[x][y] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            
            seen.add((x,y))
            nei = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
            for nX, nY in nei:
                if (nX,nY) in seen:
                    continue
                seen.add((nX,nY))
                res = dfs(nX,nY, i + 1, seen)
                seen.remove((nX,nY))
                if res:
                    return res
            return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                res = dfs(row,col, 0, set())
                if res:
                    return True
        return False