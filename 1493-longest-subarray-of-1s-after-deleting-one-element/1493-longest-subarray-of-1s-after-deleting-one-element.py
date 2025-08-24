class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = deletions = best = 0
        for right in range(len(nums)):
            deletions += nums[right] == 0
            while deletions > 1:
                deletions -= nums[left] == 0
                left += 1
            best = max(best,right - left)
        return best