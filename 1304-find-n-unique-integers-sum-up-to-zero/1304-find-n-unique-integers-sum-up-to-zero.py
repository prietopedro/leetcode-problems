class Solution:
    def sumZero(self, n: int) -> List[int]:
        output = []
        curr = 1
        for _ in range(n // 2):
            output.append(curr)
            output.append(-curr)
            curr += 1
        if len(output) != n:
            output.append(0)
        return output
