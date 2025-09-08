class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def contains_zero(num):
            for c in str(num):
                if c == '0': return True
            return False
        for i in range(1,n):
            if contains_zero(i) or contains_zero(n - i):
                continue
            return [i,n-i]