class Solution:
    def makeFancyString(self, s: str) -> str:
        if not s: return s
        fancy = s[0]
        count = 1
        for i in range(1,len(s)):
            if s[i] == fancy[-1] and count == 2: 
                continue

            if s[i] == fancy[-1]: 
                count += 1
            else: 
                count = 1
            
            fancy += s[i]
        return fancy