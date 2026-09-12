class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        curr = []
        candidates.sort()
        def rec(i, target):
            if target < 0:
                return
            if i >= len(candidates):
                if target == 0:
                    output.append(curr[:])
                return
            
            curr.append(candidates[i])
            rec(i + 1,target - candidates[i])
            curr.pop()
            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1
            rec(next_i, target)
        rec(0,target)
        return output
