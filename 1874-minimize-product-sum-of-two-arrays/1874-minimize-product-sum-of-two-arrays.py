class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        a = [x for x in nums1]
        b = [-x for x in nums2]
        heapq.heapify(a)
        heapq.heapify(b)
        total = 0
        while a:
            x = heapq.heappop(a)
            y = -heapq.heappop(b)
            total += (x * y)
        return total

