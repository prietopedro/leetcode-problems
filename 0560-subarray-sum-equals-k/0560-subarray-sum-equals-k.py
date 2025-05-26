class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        running_sum = 0
        output = 0
        for num in nums:
            running_sum += num
            seen[running_sum] += 1
            output += seen[running_sum - k]
        return output