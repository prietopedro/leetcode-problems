class Solution:
    def countSubstrings(self, s: str) -> int:
        def count(s,left,right):
            total = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                total += 1
                left -= 1
                right += 1
            return total

        total = 0
        for i in range(len(s)):
            total += 1 + count(s, i-1, i + 1) + count(s, i - 1, i)
            
        return total


