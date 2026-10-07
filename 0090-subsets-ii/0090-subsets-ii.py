class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        output = []
        nums.sort()
        def bt(i, current):
            if i >= len(nums):
                output.append(current[:])
                return
            current.append(nums[i])
            bt(i + 1, current)
            current.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            bt(i + 1, current)
        bt(0,[])
        return output