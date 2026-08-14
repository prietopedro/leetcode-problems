class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        best = 0
        left = 0

        seen = defaultdict(int)
        for right in range(len(s)):
            while seen[s[right]] > 1:
                seen[s[left]] -= 1
                left += 1
            seen[s[right]] += 1
            best = max(best,right - left + 1)
        return best
