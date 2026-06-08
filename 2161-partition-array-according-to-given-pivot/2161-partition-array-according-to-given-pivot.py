class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        output = []
        greater = []
        pivot_founds = 0
        for num in nums:
            if num < pivot:
                output.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                pivot_founds += 1
        output += [pivot] * pivot_founds
        output += greater
        return output