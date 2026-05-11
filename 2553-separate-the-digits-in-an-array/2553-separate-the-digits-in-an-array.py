class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        output = []
        for num in nums[::-1]:
            while num:
                output.append(num % 10)
                num //= 10
        return output[::-1]