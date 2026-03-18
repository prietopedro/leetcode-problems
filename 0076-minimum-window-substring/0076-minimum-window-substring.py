class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best_starting,best_length = inf,inf
        
        sub = defaultdict(int)
        needed = 0
        for c in t:
            needed += c not in sub
            sub[c] += 1
        
        window = defaultdict(int)
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            needed -= window[s[right]] == sub[s[right]]
            while not needed:
                if best_length > right - left + 1:
                    best_length = right-left + 1
                    best_starting = left
                needed += window[s[left]] == sub[s[left]]
                window[s[left]] -= 1
                left += 1
        return s[best_starting:best_starting + best_length] if best_starting != inf else ""
