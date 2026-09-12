class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curr = []
        output = []
        nums.sort()
        def rec(i):
            if i >= len(nums):
                output.append(curr[:])
                return
            curr.append(nums[i])
            rec(i + 1)
            curr.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            rec(i + 1)
        rec(0)
        return output