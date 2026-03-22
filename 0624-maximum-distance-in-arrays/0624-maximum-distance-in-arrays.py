class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        current_min = arrays[0][0]
        current_max = arrays[0][-1]
        best = -inf
        for i in range(1,len(arrays)):
            best = max(best,abs(arrays[i][-1] - current_min), abs(current_max - arrays[i][0]), abs(arrays[i][0] - current_max))
            current_min = min(current_min,arrays[i][0])
            current_max = max(current_max, arrays[i][-1])
        return best