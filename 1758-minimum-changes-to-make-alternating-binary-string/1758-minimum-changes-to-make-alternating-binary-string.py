class Solution:
    def minOperations(self, s: str) -> int:
        zeroes = 0
        ones = 0
        for i,num in enumerate(s):
            if i % 2 == 0:
                zeroes += num == "1"
                ones += num == "0"
            else:
                zeroes += num == "0"
                ones += num == "1"
        return min(zeroes,ones)