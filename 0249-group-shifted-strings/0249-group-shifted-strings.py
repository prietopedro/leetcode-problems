class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for i,s in enumerate(strings):
            starting = [1]
            for i in range(len(s) - 1):
                if s[i] <= s[i + 1]:
                    starting.append(ord(s[i + 1]) - ord(s[i]))
                else:
                    starting.append(ord('z') - ord(s[i]) + ord(s[i + 1]) - ord('a') + 1)
            seen[tuple(starting)].append(s)
        return list(seen.values())
        
