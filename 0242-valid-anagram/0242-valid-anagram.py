class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = defaultdict(int)
        for c in s:
            sCount[c] += 1
        
        for c in t:
            sCount[c] -= 1
            if sCount[c] < 0:
                return False
        
        return sum(sCount.values()) == 0
        