class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_index = -1
        max_index = -1
        invalid_index = -1
        output = 0
        for i in range(len(nums)):
            if not (minK <= nums[i] <= maxK):
                invalid_index = i
            if nums[i] == minK: 
                min_index = i
            if nums[i] == maxK:
                max_index = i

            output += max(min(min_index,max_index) - invalid_index,0)
            
        return output