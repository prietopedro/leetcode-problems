class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = set(wordDict)
        @cache
        def rec(i,j):
            if s[i:j] in dic:
                return True
            
            for k in range(i + 1, j):
                res = rec(i,k) and rec(k, j)
                if res:
                    return True
            return False
        return rec(0,len(s))