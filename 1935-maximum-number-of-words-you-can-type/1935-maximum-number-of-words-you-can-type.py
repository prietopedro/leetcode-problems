class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        output = 0
        current = True
        for c in text:
            if c == " ":
                output += current
                current = True
                continue
            if not current:
                continue
            if c in brokenLetters:
                current = False
        return output + current
