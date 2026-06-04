class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        product = 1
        output = [0] * len(nums)
        for num in nums:
            if num == 0:
                zeroes += 1
            else:
                product *= num

            if zeroes >= 2:
                return output
        
        for i,num in enumerate(nums):
            if zeroes and num != 0:
                output[i] = 0
            elif zeroes:
                output[i] = product
            else:
                output[i] = product // nums[i]
        return output
