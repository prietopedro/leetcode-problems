class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen = {}
        left = 0
        max_amount = 0
        for right in range(len(fruits)):
            if fruits[right] not in seen and len(seen) == 2:
                min_index = min(seen.values())
                del seen[fruits[min_index]]
                left = min_index + 1
            seen[fruits[right]] = right
            max_amount = max(max_amount,right - left + 1)
        return max_amount




