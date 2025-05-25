class Solution:
    def maxSubstrings(self, word: str) -> int:
        left = 0
        last_seen = {}
        output = 0
        for right in range(len(word)):
            last_seen[word[right]] = min(last_seen.get(word[right], inf),right)
            if right - last_seen[word[right]] + 1 >= 4:
                left = right + 1
                last_seen = {}
                output += 1
        return output
                
            
            