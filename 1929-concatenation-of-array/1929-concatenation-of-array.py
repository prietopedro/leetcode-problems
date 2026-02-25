class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_nums = []
        for i in range(len(nums) * 2):
            new_nums.append(nums[i % len(nums)])
        return new_nums