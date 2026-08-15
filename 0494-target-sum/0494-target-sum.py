class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ## if i == len(nums) and current == target:
            ## return 1
        ## elif i >= len(nums):
            ## return 0
        
        ## dp[i][current] = dp[i + 1][current + nums[i]] + dp[i + 1][current - nums[i]]
        # @cache
        # def dp(i, current):
        #     nonlocal target
        #     if i == len(nums) and current == target:
        #         return 1
        #     if i >= len(nums):
        #         return 0
        
        #     return dp(i + 1,current + nums[i]) + dp(i + 1,current - nums[i])
        # return dp(0,0)
        total = sum(nums)
        offset = total
        m = 2 * total + 1
        n = len(nums)

        dp = [0] * m

        # Base case:
        # i == len(nums)
        # current == target -> 1 way
        if -total <= target <= total:
            dp[target + offset] = 1

        for i in range(n - 1, -1, -1):
            next_dp = [0] * m
            for j in range(m):
                current = j - offset

                # current + nums[i]
                if current + nums[i] <= total:
                    next_dp[j] += dp[j + nums[i]]

                # current - nums[i]
                if current - nums[i] >= -total:
                    next_dp[j] += dp[j - nums[i]]
            dp = next_dp

        return dp[offset]
