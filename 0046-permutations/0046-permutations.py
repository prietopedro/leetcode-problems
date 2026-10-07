class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        output = []
        def perm(current):
            if len(current) == len(nums):
                output.append(current[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in current:
                    continue
                current.append(nums[i])
                perm(current)
                current.pop()
        perm([])
        return output