class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        output = []
        num = 1
        for _ in range(n):
            output.append(num)
            if num * 10 <= n: 
                num *= 10
                continue
            while num >= n or num % 10 == 9:
                num //= 10
            num += 1
        return output