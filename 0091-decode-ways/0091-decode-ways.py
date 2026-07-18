class Solution:
    def numDecodings(self, s: str) -> int:
        # @cache
        # def rec(i):
        #     if i >= len(s):
        #         return 1

        #     if s[i] == "0":
        #         return 0

        #     output = rec(i + 1)
        #     if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26 :
        #         output += rec(i + 2)
        #     return output
        # return rec(0)  
            

        double, single = 0,1
        for i in range(len(s) - 1, -1, -1):
            current = 0
            if s[i] != '0':
                current = single
            
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                current += double
            double,single = single,current
        return single
