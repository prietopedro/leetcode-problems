class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best_length = 0
        left = 0
        seen = defaultdict(bool)
        for right in range(len(s)):
            while seen[s[right]]:
                seen[s[left]] = False
                left += 1
            seen[s[right]] = True
            best_length = max(best_length, right - left + 1)
        return best_length