class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cum_sum = 0
        highest = 0
        for alt in gain:
            cum_sum += alt
            highest = max(highest,cum_sum)
        return highest