class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        left = 0
        right = len(height) - 1
        while left < right:
            best = max(best, min(height[left],height[right]) * (right - left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return best