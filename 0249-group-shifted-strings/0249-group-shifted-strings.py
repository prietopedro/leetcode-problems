class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for i,s in enumerate(strings):
            starting = []
            for i in range(len(s) - 1):
                starting.append((ord(s[i]) - ord(s[i + 1])) % 26)
            seen[tuple(starting)].append(s)
        return list(seen.values())
        
