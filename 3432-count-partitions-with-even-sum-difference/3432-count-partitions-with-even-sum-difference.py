class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        current = 0
        total_partitions = 0
        for i in range(len(nums) - 1):
            current += nums[i]
            total -= nums[i]
            total_partitions += (total - current) % 2 == 0
        return total_partitions
