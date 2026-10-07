class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        output = []
        def bt(i,current, target):
            if target == 0:
                output.append(current[:])
                return
            if i >= len(candidates) or candidates[i] > target:
                return
            current.append(candidates[i])            
            bt(i + 1, current, target - candidates[i])
            current.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            bt(i + 1, current, target)
        
        bt(0, [], target)
        return output