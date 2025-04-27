class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        deleted = 0
        for i in range(len(nums)):
            if nums[i] == val:
                deleted += 1
            else:
                nums[i - deleted] = nums[i]
        return len(nums) - deleted