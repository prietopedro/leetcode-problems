class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and (abs(ord(stack[-1]) - ord(c)) == 1 or abs(ord(stack[-1]) - ord(c)) == 25):
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack) if stack else ''
                