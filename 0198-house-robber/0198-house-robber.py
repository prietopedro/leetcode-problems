class Solution:
    def rob(self, nums: List[int]) -> int:
        
        first,second,third = 0,0,0
        for house in nums:
            fourth = house + max(first,second)
            first,second,third = second, third, fourth
        return max(second,third)