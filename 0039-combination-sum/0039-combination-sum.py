class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        curr = []
        seen = set()
        def rec(i, target):
            if i >= len(candidates) or target < 0:
                return
            if target == 0:
                hash_k = ','.join([str(x) for x in curr])
                if hash_k in seen:
                    return
                seen.add(hash_k)
                output.append(curr[:])
            
            curr.append(candidates[i])
            rec(i, target - candidates[i])
            curr.pop()
            rec(i + 1, target)
        rec(0, target)
        return output

            