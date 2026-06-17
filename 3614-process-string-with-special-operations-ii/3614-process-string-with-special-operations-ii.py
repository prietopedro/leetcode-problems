class Solution:
    def processStr(self, s: str, k: int) -> str:
        total = 0
        for c in s:
            if c == '#':
                total *= 2
            elif c == '*':
                total -= 1 if total else 0
            elif c == "%":
                continue
            else:
                total += 1


        if k + 1 > total:
            return "."
        
        for c in reversed(s):
            if c == "*":
                total += 1
            elif c == "#":
                if k + 1 > (total + 1) // 2:
                    k -= total // 2
                total = (total + 1) // 2
            elif c == "%":
                k = total - k - 1
            else:
                if k + 1 == total:
                    return c
                total -= 1
        return "."

