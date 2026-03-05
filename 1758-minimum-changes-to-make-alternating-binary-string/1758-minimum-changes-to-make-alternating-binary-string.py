class Solution:
    def minOperations(self, s: str) -> int:
        zeroes = 0
        for i,num in enumerate(s):
            zeroes += i % 2 == 0 and num == "1"
            zeroes += i % 2 == 1 and num == "0"
        return min(zeroes,len(s) - zeroes)