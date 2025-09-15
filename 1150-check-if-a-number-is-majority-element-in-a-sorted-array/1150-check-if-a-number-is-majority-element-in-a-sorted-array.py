class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] <= target:
                left = middle + 1
            else:
                right = middle
        left -= 1
        return len(nums) // 2 <= left and nums[left - len(nums) // 2] == target