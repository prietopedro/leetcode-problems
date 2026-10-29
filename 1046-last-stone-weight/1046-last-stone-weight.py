class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        
        heapq.heapify_max(stones)
        while len(stones) > 1:
            s1,s2 = heapq.heappop_max(stones),heapq.heappop_max(stones)
            if s1 == s2:
                continue
            heapq.heappush_max(stones,s1 - s2)
        return sum(stones)