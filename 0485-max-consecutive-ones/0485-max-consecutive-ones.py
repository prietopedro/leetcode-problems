class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        consecutive = 0
        for num in nums:
            consecutive += 1
            if num == 0:
                consecutive = 0
            max_ones = max(max_ones, consecutive)
        return max_ones