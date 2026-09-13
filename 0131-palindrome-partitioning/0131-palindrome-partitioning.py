class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curr = []
        output = []

        def backtrack(start):
            if start == len(s):
                output.append(curr[:])
                return

            for end in range(start + 1, len(s) + 1):
                part = s[start:end]

                if part != part[::-1]:
                    continue

                curr.append(part)
                backtrack(end)
                curr.pop()

        backtrack(0)
        return output