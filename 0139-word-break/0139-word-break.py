class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def rec(i):
            if i >= len(s):
                return True
            for word in wordDict:
                if s[i:i+len(word)] == word and rec(i + len(word)):
                    return True

            return False
        return rec(0)