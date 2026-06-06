class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right_sum = sum(nums)
        left_sum = 0
        output = []
        for num in nums:
            left_sum += num
            output.append(abs(left_sum - right_sum) )
            left_sum += num
        return output