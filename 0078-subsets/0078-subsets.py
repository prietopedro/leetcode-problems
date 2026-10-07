class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        output = []
        def bt(i, current = []):
            if i >= len(nums):
                output.append(current[:])
                return
            bt(i + 1, current)
            current.append(nums[i])
            bt(i + 1,current)
            current.pop()
        bt(0)
        return output