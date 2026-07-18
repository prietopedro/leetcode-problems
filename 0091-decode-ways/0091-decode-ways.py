class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def rec(i):
            if i >= len(s):
                return 1

            if s[i] == "0":
                return 0

            output = rec(i + 1)
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26 :
                output += rec(i + 2)
            return output
        return rec(0)  
            

            
