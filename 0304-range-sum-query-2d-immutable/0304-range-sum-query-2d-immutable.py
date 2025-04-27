class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum_arr = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for row in range(len(matrix)):
            total = 0
            for col in range(len(matrix[0])):
                total += matrix[row][col]
                self.sum_arr[row + 1][col + 1] = total + self.sum_arr[row][col + 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = (
            self.sum_arr[row2 + 1][col2 + 1] - # total for the box ending at latest indeces
            self.sum_arr[row1][col2 + 1] - # minus top box
            self.sum_arr[row2 + 1][col1] +  # minus left box
            self.sum_arr[row1][col1]) # plus overlap that we removed twice
        return total