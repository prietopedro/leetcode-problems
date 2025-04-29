class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        best_num = max(nums)
        left = 0
        window = 0
        output = 0
        first_i = deque([])
        for right in range(len(nums)):
            if nums[right] == best_num:
                window += 1
                first_i.append(right)
            
            while window == k:
                output += len(nums) - right
                window -= nums[left] == best_num
                left += 1
        return output

