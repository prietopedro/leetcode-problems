class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        best = -inf
        for i in range(2):
            rob1,rob2 = 0,0
            for i in range(i,len(nums) - 1 + i):
                rob3 = max(nums[i] + rob1, rob2)
                rob1,rob2 = rob2,rob3
            best = max(best,rob2)
        return best