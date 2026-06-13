class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        output = []
        for word in words:
            word_weight = 0
            for c in word:
                word_weight += weights[ord(c) - ord('a')]
            output.append(chr(ord('a') + 25 - (word_weight % 26)))
        return "".join(output)