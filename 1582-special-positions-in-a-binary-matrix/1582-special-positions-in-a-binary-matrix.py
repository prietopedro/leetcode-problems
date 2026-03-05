class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        m,n = len(mat),len(mat[0])
        for row in range(m):
            for col in range(n):
                rows[row] += mat[row][col]
                cols[col] += mat[row][col]
        output = 0
        for row in range(m):
            for col in range(n):
                output += rows[row] == 1 and cols[col] == 1 and mat[row][col] == 1
        return output