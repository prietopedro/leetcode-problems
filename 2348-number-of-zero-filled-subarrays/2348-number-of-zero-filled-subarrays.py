class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        left = 0
        total = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                left = right + 1
                continue
            total += right - left + 1
        return total