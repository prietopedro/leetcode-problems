class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums) + 1)
        for i in range(len(nums)):
            output[i + 1] = output[i] * nums[i]
        back = 1
        for i in range(len(nums) - 1,-1,-1):
            output[i + 1] = back * output[i]
            back *= nums[i]
        return output[1:]