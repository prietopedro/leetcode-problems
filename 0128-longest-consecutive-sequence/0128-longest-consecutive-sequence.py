class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in seen:
                continue
            window = 0
            curr = num
            while curr in seen:
                window += 1
                curr += 1
            longest = max(longest,window)
        return longest
