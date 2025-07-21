class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2: return s
        fancy = [s[0],s[1]]
        for i in range(2,len(s)):
            if s[i] == fancy[-1] and s[i] == fancy[-2]: 
                continue
            fancy += s[i]
        return ''.join(fancy)