class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output,total = 0,0
        counts = defaultdict(int)
        counts[0] = 1
        for num in nums:
            total += num
            output += counts[total - k]
            counts[total] += 1
        return output

