class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_amount = 0
        current = 0
        seen = set()
        left = 0
        for num in nums:
            while num in seen:
                current -= nums[left]
                seen.remove(nums[left])
                left += 1
            current += num
            seen.add(num)
            max_amount = max(max_amount,current)
        return max_amount