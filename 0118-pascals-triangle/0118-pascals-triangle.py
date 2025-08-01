class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows: return []
        output = [[1]]
        for i in range(1,numRows):
            row = [1] * (len(output[-1]) + 1)

            for j in range(len(row)):
                if j == 0 or j == len(row) - 1:
                    continue
                row[j] = output[-1][j - 1] + output[-1][j]
            output.append(row)

        return output


