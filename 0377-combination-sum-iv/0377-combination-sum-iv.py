class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # @cache
        # def dp(target):
        #     if target == 0:
        #         return 1
        #     if target < 0:
        #         return 0
        #     output = 0
        #     for num in nums:
        #         output += dp(target - num)
        #     return output
        # return dp(target)
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(1, target + 1):
            for num in nums:
                if t >= num:
                    dp[t] += dp[t - num]
        return dp[-1]