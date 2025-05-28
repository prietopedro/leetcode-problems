class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        @cache
        def rec(i,j):
            left_i,left_j = m - i,n - j
            if i >= m:
                return max(left_j,0)
            if j >= n:
                return max(left_i,0)

            if word1[i] == word2[j]:
                return rec(i + 1,j + 1)

            middle = 1 + rec(i + 1,j + 1)
            left = 1 + rec(i + 1,j)
            right = 1 + rec(i,j + 1)
            return min(left,right,middle)
        return rec(0,0)
