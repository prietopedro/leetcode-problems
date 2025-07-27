class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        output = 0
        for i in range(1,len(nums) - 1):
            start = i
            while i < len(nums) - 2 and nums[i + 1] == nums[start]:
                i += 1
            print(i)
            if nums[start] - nums[start - 1] > 0 and nums[start] - nums[i + 1] > 0:
                output += 1
            if nums[start] - nums[start - 1] < 0 and nums[start] - nums[i + 1] < 0:
                output += 1
        return output