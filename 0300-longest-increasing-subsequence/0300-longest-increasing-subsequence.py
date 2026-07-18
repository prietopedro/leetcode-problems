class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        seen = [0] * len(nums) 
        for i,num in enumerate(nums):
            for j in range(i - 1, -1, -1):
                if nums[j] >= num:
                    continue
                seen[i] = max(seen[i], seen[j])
            seen[i] += 1
        return max(seen)