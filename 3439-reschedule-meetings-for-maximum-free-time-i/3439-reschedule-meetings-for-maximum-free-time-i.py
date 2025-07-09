class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = []
        events = sorted([(startTime[i],endTime[i]) for i in range(len(startTime))])
        current = 0
        for start,end in events:
            gaps.append(start - current)
            current = end
        if current < eventTime:
            gaps.append(eventTime - current)
        if not gaps: return 0
        best = 0
        left = 0
        window_sum = 0
        for right in range(len(gaps)):
            window_sum += gaps[right]
            best = max(window_sum,best)
            if right - left == k:
                window_sum -= gaps[left]
                left += 1
        return best
            