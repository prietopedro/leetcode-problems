class Solution:
    def processStr(self, s: str) -> str:
        def reverse(output):
            for i in range(len(output) // 2):
                output[i], output[-i - 1] = output[-i - 1], output[i]
        
        def duplicate(output):
            for i in range(len(output)):
                output.append(output[i])

        output = []
        for c in s:
            if c == '*':
                if output:
                    output.pop() 
            elif c == "#":
                duplicate(output)
            elif c == '%':
                reverse(output)
            else:
                output.append(c)
        
        return "".join(output)