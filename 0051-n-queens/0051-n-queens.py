class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # once i use a row i cant use that row
            # keep track of used rows
        # once i use a col i cant use that col
            # keep track of used cols
        # when i use a cell i cant use any other cell where abs(row1 - row2) == abs(col1 - col2)
            # store difference between row and col (row - col) for both left and right


        # for i to row , col
        # row = i // n
        # col = i % n

        output = []
        current = []
        curr_rows = set()
        curr_cols = set()
        curr_left = set()
        curr_right = set()
        def backtrack(curr, queens):
            row = curr // n
            col = curr % n
            if queens == n:
                output.append(current + ["."] * (n * n - len(current)))
                return
            if curr >= n * n:
                return
            
            can_set = (
                row not in curr_rows and
                col not in curr_cols and
                row - col not in curr_left and
                row + col not in curr_right and
                queens < n
            )
            if can_set:
                curr_rows.add(row)
                curr_cols.add(col)
                curr_left.add(row - col)
                curr_right.add(row + col)
                current.append("Q")
                backtrack(curr + 1, queens + 1)
                curr_rows.remove(row)
                curr_cols.remove(col)
                curr_left.remove(row - col)
                curr_right.remove(row + col)
                current.pop()
            
            current.append('.')
            backtrack(curr + 1, queens)
            current.pop()


        backtrack(0,0)
        modified_output = []
        for game in output:
            new_game = []
            level = ""
            for place in game:
                level += place
                if len(level) == n:
                    new_game.append(level)
                    level = ""
            modified_output.append(new_game)
        return modified_output


# 8 and 11
# 8 // 4 == 2
# 8 % 4 == 0

# 11 // 4 = 2
# 11 % 4 == 3

# [".Q..",
#  "...Q",
#  "..Q.",
#  "Q..."]

#  1,3
#  2,2