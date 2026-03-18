class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counter = defaultdict(int)
        s2Counter = defaultdict(int)
        needed = 0
        for c in s1:
            needed += c not in s1Counter
            s1Counter[c] += 1
        
        left = 0
        for right in range(len(s2)):
            s2Counter[s2[right]] += 1
            needed -= s2Counter[s2[right]] == s1Counter[s2[right]]


            if right - left + 1 > len(s1):
                s2Counter[s2[left]] -= 1
                needed += s2Counter[s2[left]] == s1Counter[s2[left]] - 1
                left += 1
            
            if needed == 0:
                return True

        return False


