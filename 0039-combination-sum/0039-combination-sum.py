class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        output = []
        def bt(i, current, target):
            if target == 0:
                output.append(current[:])
                return
            if target < 0 or i >= len(candidates):
                return
            bt(i + 1, current, target)
            current.append(candidates[i])
            bt(i, current, target - candidates[i])
            current.pop()
        bt(0,[],target)
        return output