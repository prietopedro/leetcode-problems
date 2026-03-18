class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_frequency = 0
        frequency_map = defaultdict(int)
        longest = 0
        left = 0
        for right in range(len(s)):
            frequency_map[s[right]] += 1
            max_frequency = max(max_frequency,frequency_map[s[right]])
            if right - left + 1 - max_frequency > k:
                frequency_map[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest


