class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        best_num = max(nums)
        left = 0
        window = 0
        output = 0
        for right in range(len(nums)):
            window += nums[right] == best_num
            while window == k:
                output += len(nums) - right
                window -= nums[left] == best_num
                left += 1
        return output

