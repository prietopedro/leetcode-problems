class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,i,r = 0,0,len(nums) - 1
        def swap_right(i,r):
            while nums[r] == 2 and r > i:
                r -= 1
            nums[i],nums[r] = nums[r],nums[i]
            return r
        def swap_left(i,l):         
            while nums[l] == 0 and l < i:
                l += 1
            nums[i],nums[l] = nums[l],nums[i]
            return l

        while i <= r:
            if nums[i] == 2: r = swap_right(i,r)
            if nums[i] == 0: l = swap_left(i,l)
            i += 1
            
        