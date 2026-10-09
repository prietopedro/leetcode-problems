class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9":"wxyz"}

        output = []
        def bt(i, current):
            if i == len(digits):
                output.append("".join(current))
                return
            for digit in letters[digits[i]]:
                current.append(digit)
                bt(i + 1, current)
                current.pop()
        bt(0,[])
        return output