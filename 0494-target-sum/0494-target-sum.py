class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ## if i == len(nums) and current == target:
            ## return 1
        ## elif i >= len(nums):
            ## return 0
        
        ## dp[i][current] = dp[i + 1][current + nums[i]] + dp[i + 1][current - nums[i]]
        @cache
        def dp(i, current):
            nonlocal target
            if i == len(nums) and current == target:
                return 1
            if i >= len(nums):
                return 0
        
            return dp(i + 1,current + nums[i]) + dp(i + 1,current - nums[i])
        return dp(0,0)