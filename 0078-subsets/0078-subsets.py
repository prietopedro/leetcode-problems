class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        def backtrack(i,current = []):
            current.append(nums[i])
            output.append(current[:])
            for j in range(i + 1,len(nums)):
                backtrack(j,current)
                current.pop()
            return output

        for i in range(len(nums)):
            backtrack(i,[])
        return output
        
            
