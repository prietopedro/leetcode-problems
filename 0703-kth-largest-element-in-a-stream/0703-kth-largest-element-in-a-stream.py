class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.size = k
        for num in nums:
            self.add(num)




    def add(self, val: int) -> int:
        if len(self.heap) < self.size or val > self.heap[0]:
            heapq.heappush(self.heap,val)
        if len(self.heap) > self.size:
            heapq.heappop(self.heap)
        return self.heap[0]
    


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)