class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        left = 0
        for right in range(len(nums)):
            if nums[right] in seen:
                return True
            seen.add(nums[right])
            if len(seen) > k:
                seen.remove(nums[right - k])
        return False