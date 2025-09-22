class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_frequency = 0
        seen = defaultdict(int)
        occ = 0
        for num in nums:
            seen[num] += 1
            if seen[num] > max_frequency:
                max_frequency = seen[num]
                occ = seen[num]
            elif seen[num] == max_frequency:
                occ += seen[num]
        return occ