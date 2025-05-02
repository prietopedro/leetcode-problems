class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        rows = len(matrix)
        cols = len(matrix[0])
        prev = 'R'
        row,col = 0,0
        seen = set()
        while len(output) != rows * cols:
            print(row,col)
            output.append(matrix[row][col])
            seen.add((row,col))
            if prev == 'R':
                nr,nc = row,col + 1
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen:
                    row,col = nr,nc
                    prev = 'R'
                else:
                    row,col = row + 1,col
                    prev = 'D'
            elif prev == 'L':
                nr,nc = row,col - 1
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen:
                    row,col = nr,nc
                    prev = 'L'
                else:
                    row,col = row - 1,col
                    prev = 'U'
            elif prev == 'U':
                nr,nc = row - 1,col
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen:
                    row,col = nr,nc
                    prev = 'U'
                else:
                    row,col = row,col + 1
                    prev = 'R'
            elif prev == 'D':
                nr,nc = row + 1,col
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen:
                    row,col = nr,nc
                    prev = 'D'
                else:
                    row,col = row,col - 1
                    prev = 'L'
        return output
            
