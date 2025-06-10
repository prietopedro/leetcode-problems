class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        min_num = -inf
        for num in preorder:
            while stack and stack[-1] <= num:
                min_num = stack.pop()
            if num <= min_num:
                return False
            stack.append(num)
        return True
                
                