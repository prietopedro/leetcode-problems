class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', ']': '[','}':'{'}
        for c in s:
            if c not in mapping:
                stack.append(c)
            elif not stack or stack[-1] != mapping[c]:
                return False
            else:
                stack.pop()
        return True if not stack else False