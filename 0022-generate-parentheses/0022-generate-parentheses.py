class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        output = []
        def generate(opened, current):
            if len(current) == n * 2 and not opened:
                output.append("".join(current))
                return
            if opened + len(current) > n * 2:
                return

            if opened:
                current.append(")")
                generate(opened - 1, current)
                current.pop()

            current.append("(")
            generate(opened + 1, current)
            current.pop()
        generate(0,[])
        return output