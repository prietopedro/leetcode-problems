class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        output = 0
        for i in range(2,len(nums)):
            output += nums[i - 2] + nums[i] == nums[i - 1] / 2
        return output