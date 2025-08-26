class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        max_area = 0
        for w,h in dimensions:
            diagonal = sqrt((w ** 2) + (h ** 2))
            if diagonal == max_diagonal:
                max_area = max(max_area,w * h)
            elif diagonal > max_diagonal:
                max_diagonal = diagonal
                max_area = w * h
        return max_area