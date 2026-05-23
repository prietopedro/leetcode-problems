class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left, right = 0, len(arr)
        while left < right:
            middle = (left + right) // 2
            print(arr[middle], middle)
            if arr[middle] < middle:
                left = middle + 1
            else:
                right = middle
        return left if left < len(arr) and arr[left] == left else -1