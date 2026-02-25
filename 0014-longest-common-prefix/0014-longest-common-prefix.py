class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_i = min(len(x) for x in strs)
        for i in range(min_i):
            char = None
            for c in strs:
                if not char:
                    char = c[i]
                if char != c[i]:
                    return strs[0][:i]
        return strs[0][:min_i]
