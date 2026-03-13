class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        left, right = 0, min(workerTimes) * (mountainHeight + 1) * (mountainHeight)
        ret = right

        while left < right:
            t = (left + right) // 2
            height = 0
            for w in workerTimes:
                tw = t // w
                height += (-1 + sqrt(1 + 4 * 2 * tw)) // 2
                
            if height >= mountainHeight:
                # ret = min(ret, m)
                right = t
            else:
                left = t + 1

        return left