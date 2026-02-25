class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sCount = defaultdict(int)
        tCount = defaultdict(int)
        for c1,c2 in zip(s,t):
            sCount[c1] += 1
            sCount[c2] -= 1
            tCount[c2] += 1
            tCount[c1] -= 1
        
        return sCount == tCount
