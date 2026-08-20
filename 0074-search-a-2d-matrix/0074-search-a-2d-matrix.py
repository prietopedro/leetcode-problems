class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## binary through the whole matrix
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = (m * n) - 1
        while left <= right:
            middle = left + (right - left) // 2
            row = middle // n
            col = middle % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = middle - 1
            else:
                left = middle + 1
        return False

