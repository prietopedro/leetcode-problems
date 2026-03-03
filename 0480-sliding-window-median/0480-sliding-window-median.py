class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList()
        left = 0
        output = []
        mid = k // 2
        for right in range(len(nums)):
            window.add(nums[right])
            if len(window) == k:
                if k % 2 > 0:
                    output.append(window[mid])
                else:
                    output.append((window[mid] + window[mid - 1]) / 2)
                window.remove(nums[left])
                left+= 1

        return output