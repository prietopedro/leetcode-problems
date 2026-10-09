class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # for each row place queen (mark column)
            # for each row place queen where not in column and doesnt clash
                # ...
        
        # (0,0), (1,1), (2,2), (3,3)
        # (0,1), (1,2)
        # if y2-y1 == x2 - x1

        # (0,3),(1,2),(2,1),(3,0)
        # (0,2), (1,1),(2,0)
        # if y1+y2 == x2 + x1

        output = []
        seen_cols = set()
        left,right = set(), set()
        def rec(row,current):
            if row == n:
                print(current)
                output.append(current[:])
                return
            for col in range(n):
                if col in seen_cols or (row - col) in left or (row + col) in right:
                    continue
                current.append("".join((["."] * col) + ["Q"] + ["."] * (n - col - 1)))
                seen_cols.add(col)
                left.add(row - col)
                right.add(row + col)
                rec(row + 1, current)
                seen_cols.remove(col)
                left.remove(row - col)
                right.remove(row + col)
                current.pop()
        rec(0,[])
        return output



