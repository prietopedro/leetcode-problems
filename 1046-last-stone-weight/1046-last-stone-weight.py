class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            stone1,stone2 = heapq.heappop(heap),heapq.heappop(heap)
            if stone1 == stone2:
                continue
            new_stone = -stone1 + stone2
            heapq.heappush(heap,-new_stone)
        return -heap[0] if heap else 0