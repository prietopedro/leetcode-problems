class Solution:
    def maxScore(self, s: str) -> int:
        ones = sum(int(x) for x in s)
        zeroes = 0
        best = -inf
        for i in range(len(s) - 1):
            num = int(s[i])
            ones -= num
            zeroes += num == 0
            best = max(best, ones + zeroes)
        return best