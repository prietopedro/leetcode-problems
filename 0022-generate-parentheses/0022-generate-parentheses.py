class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        curr = []
        curr_stack = []
        def bt(left):
            if left == 0 and not curr_stack:
                output.append(''.join(curr[:]))
                return
            if left:
                curr_stack.append('(')
                curr.append('(')
                bt(left - 1)
                curr_stack.pop()
                curr.pop()
            if curr_stack:
                curr_stack.pop()
                curr.append(')')
                bt(left)
                curr_stack.append('(')
                curr.pop()
            

        bt(n)
        return output