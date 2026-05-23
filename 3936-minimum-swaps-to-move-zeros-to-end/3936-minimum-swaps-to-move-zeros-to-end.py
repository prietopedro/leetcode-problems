class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        zeroes = sum(1 for x in nums if x == 0)
        swaps = 0
        for i in range(len(nums) - 1, len(nums) - 1 - zeroes, -1):
            if nums[i] != 0:
                swaps += 1
        return swaps
