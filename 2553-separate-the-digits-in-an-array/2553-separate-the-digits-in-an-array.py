class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        output = []
        for num in nums:
            for c in str(num):
                output.append(int(c))
        return output