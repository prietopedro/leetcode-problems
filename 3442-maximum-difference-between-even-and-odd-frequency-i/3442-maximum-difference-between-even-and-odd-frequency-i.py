class Solution:
    def maxDifference(self, s: str) -> int:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        min_even = min(num for num in counter.values() if not num % 2)
        max_odd = max(num for num in counter.values() if num % 2)
        return max_odd - min_even
