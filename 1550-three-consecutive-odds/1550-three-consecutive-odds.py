class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        left = total = 0
        for right in range(len(arr)):
            if arr[right] % 2 != 1:
                left = right + 1
                total = 0
                continue
            total += 1
            if total == 3:
                return True
        return False
