class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        seen = []
        output = []
        for right in range(len(nums)):
            heapq.heappush(seen,(-nums[right],right))
            while len(seen) > k and seen[0][1] < right - k + 1:
                heapq.heappop(seen)
            if len(seen) >= k:
                output.append(-seen[0][0])
        return output



                
