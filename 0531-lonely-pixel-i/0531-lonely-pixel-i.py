class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)

        for row in range(len(picture)):
            for col in range(len(picture[0])):
                rows[row] += picture[row][col] == "B"
                cols[col] += picture[row][col] == "B"
        output = 0
        for row in range(len(picture)):
            for col in range(len(picture[0])):
                output += picture[row][col] == "B" and rows[row] == 1 and cols[col] == 1
        return output