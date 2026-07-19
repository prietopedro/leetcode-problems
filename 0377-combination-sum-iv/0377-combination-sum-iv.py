class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            output = 0
            for num in nums:
                output += dp(target - num)
            return output
        return dp(target)