class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        output = []
        for i in range(0,len(s),k):
            word = s[i:i + k]
            word += fill * (k - len(word))
            output.append(word)
        return output