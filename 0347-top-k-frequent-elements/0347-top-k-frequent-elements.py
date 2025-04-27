class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        count = [[] for i in range(max(counter.values()) + 1)]
        for key in counter:
            count[counter[key]].append(key)
        output = []
        for i in range(len(count) - 1, -1, -1):
            output += count[i]
            k -= len(count[i])
            if k == 0: return output
        return output

