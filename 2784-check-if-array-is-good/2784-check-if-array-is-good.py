class Solution:
    def isGood(self, nums: List[int]) -> bool:
        seen = set()
        max_num = -inf
        duplicate = None
        for num in nums:
            if num in seen:
                if duplicate or max_num > num:
                    return False
                duplicate = num
            seen.add(num)
            max_num = max(max_num, num)
        return duplicate == len(nums) - 1 and duplicate == max_num