class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        counter = [0] * 26
        for c1,c2 in zip(s,t):
            counter[ord(c1) - ord('a')] += 1
            counter[ord(c2) - ord('a')] -= 1
        return all(x == 0 for x in counter)
