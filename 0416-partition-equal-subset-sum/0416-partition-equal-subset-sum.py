class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        @cache
        def dp(i, target = total // 2):
            if target == 0: ## what if target is actually 0
                return True
            if target < 0 or i >= len(nums):
                return False
            
            return dp(i + 1, target - nums[i]) or dp(i + 1, target)
        return dp(0)