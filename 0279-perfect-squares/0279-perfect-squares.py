class Solution:
    # def numSquares(self, n: int) -> int:
        # @cache
        # def dp(i, target):

        #     if 0 == target:
        #         return 0

        #     if i ** 2 > target:
        #         return inf
            
        #     return min(
        #         dp(i, target - (i ** 2)) + 1,
        #         dp(i + 1, target)
        #     )

        # return dp(1, n)

        # loop end -> start
        #     loop start -> end
        def numSquares(self, n: int) -> int:
            dp = [0] + [float('inf')] * n

            squares = [i * i for i in range(1, isqrt(n) + 1)]

            for i in range(1, n + 1):
                for square in squares:
                    if square > i:
                        break

                    dp[i] = min(dp[i], dp[i - square] + 1)

            return dp[n]

