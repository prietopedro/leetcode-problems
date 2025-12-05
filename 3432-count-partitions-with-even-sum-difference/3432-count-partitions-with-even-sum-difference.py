class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        output = 0
        for i in range(len(nums) - 1):
            num = nums[i]
            left_sum += num
            right_sum -= num
            if (right_sum - left_sum) % 2 == 0:
                output += 1
        return output