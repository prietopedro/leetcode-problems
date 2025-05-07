class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])
        times = [[inf for col in range(n)] for row in range(m)]
        times[0][0] = 0
        heap = [(0,0,0)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while heap:
            time,row,col = heapq.heappop(heap)
            for x,y in directions:
                nr,nc = row + x,col + y
                if 0 <= nr < m and 0 <= nc < n:
                    next_time = max(time + 1,moveTime[nr][nc] + 1)
                    if times[nr][nc] <= next_time: continue
                    times[nr][nc] = max(time + 1,moveTime[nr][nc] + 1)
                    heapq.heappush(heap,(times[nr][nc],nr,nc))
        return times[-1][-1]

