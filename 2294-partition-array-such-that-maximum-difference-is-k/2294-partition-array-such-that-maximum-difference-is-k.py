class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_num,max_num = -inf,inf
        output = 0
        for num in nums:
            if num - min_num > k:
                output += 1
                min_num = num
            max_num = num
        return output
