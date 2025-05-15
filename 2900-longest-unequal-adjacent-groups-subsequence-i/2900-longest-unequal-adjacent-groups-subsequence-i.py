class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        output = []
        last_group = -1
        for c,g in zip(words,groups):
            if g == last_group: continue
            last_group = g
            output.append(c)
        return output