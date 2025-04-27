class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        total_zeroes = 0
        for num in nums:
            if num != 0: total *= num
            total_zeroes += num == 0
        output = [0] * len(nums)
        if total_zeroes >= 2:
            return output
        for i,num in enumerate(nums):
            if num == 0:
                output[i] = total
            elif num != 0 and not total_zeroes:
                output[i] = total // num

        return output

