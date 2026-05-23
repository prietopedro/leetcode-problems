class Solution:
    def check(self, nums: List[int]) -> bool:
        flipped = False
        for i in range(len(nums)):
            if nums[i] >= nums[i - 1]: continue
            if flipped: return False
            flipped = True
        return True