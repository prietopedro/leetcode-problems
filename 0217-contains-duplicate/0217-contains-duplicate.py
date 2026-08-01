class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ## we can sort and check adjectent items
        ## we can keep a seen and check if we have seen the value before
        ## we can add everything to a set and compare length
        return len(nums) != len(set(nums))