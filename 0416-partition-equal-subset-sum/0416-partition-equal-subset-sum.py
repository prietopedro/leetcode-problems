class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        @cache
        def go(i, left):
            if left == target:
                return True
            if left > target or i == len(nums):
                return False
            return go(i + 1, left + nums[i]) or go(i + 1, left)

        return go(0, 0)