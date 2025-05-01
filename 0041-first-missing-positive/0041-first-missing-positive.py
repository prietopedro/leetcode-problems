class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            curr = nums[i]
            while curr != inf and 0 < curr <= len(nums):
                hold = nums[curr - 1]
                nums[curr - 1] = inf
                curr = hold
        for i,num in enumerate(nums):
            if num != inf:
                return i + 1
        return -1
                
