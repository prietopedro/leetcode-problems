class Solution:
    def sumAndMultiply(self, n: int) -> int:
        total_sum = 0
        output = []
        for strNum in str(n):
            if strNum != '0':
                output.append(strNum)
            total_sum += int(strNum)
        if not output:
            return 0
        return total_sum * int("".join(output))