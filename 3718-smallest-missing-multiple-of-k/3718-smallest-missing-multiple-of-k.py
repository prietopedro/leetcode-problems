class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        have = set(nums)
        curr = 1
        while curr * k in have:
            curr += 1
        return curr * k
        