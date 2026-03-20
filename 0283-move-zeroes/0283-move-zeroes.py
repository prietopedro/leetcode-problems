class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zeroes = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zeroes] = nums[i]
                non_zeroes += 1
        for i in range(non_zeroes,len(nums)):
            nums[i] = 0

        