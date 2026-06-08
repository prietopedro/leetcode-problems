class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater = []
        num_of_pivots = 0
        for i in range(len(nums)):
            if nums[i] > pivot:
                greater.append(nums[i])
            elif nums[i] == pivot:
                num_of_pivots += 1
            else:
                nums[i - len(greater) - num_of_pivots] = nums[i]
        for i in range(num_of_pivots):
            nums[len(nums) - len(greater) - num_of_pivots + i] = pivot
        for i in range(len(greater)):
            nums[len(nums) - len(greater) + i] = greater[i]
        return nums
        
        
