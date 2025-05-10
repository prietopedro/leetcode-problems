class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        num1_sum,num2_sum = sum(nums1),sum(nums2)
        num1_zeroes,num2_zeroes = sum(not x for x in nums1),sum(not x for x in nums2)
        if num1_sum == num2_sum and num1_zeroes + num2_zeroes == 0:
            return num1_sum
        if num2_sum + num2_zeroes >= num1_sum + num1_zeroes and num2_sum - num1_sum + num2_zeroes >= num1_zeroes and num1_zeroes:
            return num2_sum + num2_zeroes
        if num1_sum + num1_zeroes >= num2_sum + num2_zeroes and num1_sum - num2_sum + num1_zeroes >= num2_zeroes and num2_zeroes:
            return num1_sum + num1_zeroes
        return -1 
