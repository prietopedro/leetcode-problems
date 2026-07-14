class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [1,2]
        for i in range(3,n + 1):
            stairs.append(stairs[-1] + stairs[-2])
        return stairs[n - 1]
