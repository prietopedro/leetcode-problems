class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # for each point we calculate distance and push to heap
        # keep heap size limited to k
        # return heap
        heap = []
        for x,y in points:
            dist = -sqrt((x ** 2) + (y ** 2))
            heapq.heappush(heap, (dist,x,y))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x,y] for (_,x,y) in heap]