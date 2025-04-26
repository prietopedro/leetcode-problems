class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = []
        min_index = min(len(s) for s in strs)
        for i in range(min_index):
            char = strs[0][i]
            matches = 0
            for s in strs:
                if s[i] == char: matches += 1
            if matches != len(strs): break
            output.append(char)
        return ''.join(output)
