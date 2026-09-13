class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        current = []
        output = []
        def backtrack(i):
            if i == len(digits):
                output.append("".join(current))
                return
            for letter in letters[int(digits[i])]:
                current.append(letter)
                backtrack(i + 1)
                current.pop()
        backtrack(0)
        return output