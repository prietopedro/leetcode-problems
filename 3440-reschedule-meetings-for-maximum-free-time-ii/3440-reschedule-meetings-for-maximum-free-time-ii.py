class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = []
        events = sorted([(startTime[i],endTime[i]) for i in range(len(startTime))])
        current = 0
        for start,end in events:
            gaps.append(start - current)
            current = end
        gaps.append(eventTime - current)
        if not gaps: return 0
        
        best = max(gaps)
        max_right = [0] * (len(gaps) + 1)
        for i in range(len(gaps) - 1,-1,-1):
            max_right[i] = max(max_right[i + 1], gaps[i])

        for i in range(len(gaps) - 1):
            best = max(best, gaps[i] + gaps[i + 1])
        max_gap_left = 0
        next_max_gap_left = gaps[0]
        # print(events)
        for i in range(len(events)):
            gap_left = next_max_gap_left if i != 0 else max_gap_left 
            max_gap_right = max_right[i + 2] if i + 2 < len(max_right) else 0
            event_duration = events[i][1] - events[i][0]
            if event_duration <= max_gap_right or event_duration <= gap_left:
                best = max(best,gaps[i] + events[i][1] - events[i][0] + gaps[i + 1])

            max_gap_left = next_max_gap_left
            next_max_gap_left = max(next_max_gap_left,gaps[i])

        return best
            
  
        