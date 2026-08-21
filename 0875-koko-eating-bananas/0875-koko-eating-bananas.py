class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        def feasable(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile / k)
            return hours <= h
        while left <= right:
            middle = left + (right - left) // 2
            if feasable(middle):
                right = middle - 1
            else:
                left = middle + 1
        return left