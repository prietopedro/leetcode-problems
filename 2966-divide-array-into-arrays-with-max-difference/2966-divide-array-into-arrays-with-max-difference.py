class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        output = []
        curr = []
        for num in nums:
            if len(curr) == 3:
                output.append(curr)
                curr = []
            if curr and num - k > curr[0]:
                return []
            curr.append(num)
        output.append(curr)
        return output
