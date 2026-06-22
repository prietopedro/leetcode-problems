class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        seen = [0] * 26
        for c in text:
            seen[ord('a') - ord(c)] += 1
        min_char_count = inf
        for c in "balon":
            if c == 'l' or c == 'o':
                min_char_count = min(min_char_count, seen[ord('a') - ord(c)] // 2)
            else:
                min_char_count = min(min_char_count, seen[ord('a') - ord(c)])
        return min_char_count if min_char_count != inf else 0