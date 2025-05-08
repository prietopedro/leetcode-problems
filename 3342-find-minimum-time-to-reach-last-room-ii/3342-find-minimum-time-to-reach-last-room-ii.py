class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows,cols = len(moveTime),len(moveTime[0])
        heap = [(0,0,0,0)]
        ans = [[inf for _ in range(cols)] for _ in range(rows)]
        ans[0][0] = 0
        while heap:
            time,row,col,moves = heapq.heappop(heap)
            if row == rows - 1 and col == cols - 1:
                return time
            to_add = (moves % 2) + 1
            for nr,nc in [(row + 1,col),(row - 1,col),(row, col + 1), (row, col - 1)]:
                if 0 <= nr < rows and 0 <= nc < cols:
                    next_time = max(moveTime[nr][nc] + to_add, time + to_add)
                    if next_time >= ans[nr][nc]: continue
                    ans[nr][nc] = next_time
                    heapq.heappush(heap,(next_time,nr,nc,moves + 1))
        return ans[-1][-1]
