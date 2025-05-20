class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        max_sub = [0] * (len(nums) + 1)
        for start,end in queries:
            max_sub[start] += 1
            max_sub[end + 1] -= 1
        current = 0
        print(max_sub)
        for i,num in enumerate(nums):
            current += max_sub[i]
            if current < num: return False
        return True