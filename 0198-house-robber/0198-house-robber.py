class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 = 0,0
        for house in nums:
            rob3 = max(rob1 + house, rob2)
            rob1,rob2 = rob2, rob3
        return rob2