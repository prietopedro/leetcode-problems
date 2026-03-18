class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = inf
        window_sum = 0

        left = 0
        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target and left <= right:
                min_size = min(min_size, right - left + 1)
                window_sum -= nums[left]
                left += 1


        return min_size if min_size != inf else 0