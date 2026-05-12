class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1
        missing = None
        duplicate = None
        for i in range(1, len(nums) + 1):
            if seen[i] == 0:
                missing = i
            if seen[i] > 1:
                duplicate = i
            if missing and duplicate:
                return duplicate,missing