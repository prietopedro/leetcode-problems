class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances = []
        for x,y in points:
            dist = sqrt((x * x + y * y))
            heapq.heappush_max(distances,(dist,x,y))
            if len(distances) > k:
                heapq.heappop_max(distances)
        return [[x,y] for _,x,y in distances]