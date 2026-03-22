class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strings:
            complete = [0]
            for i in range(1,len(s)):
                diff = ord(s[i]) - ord(s[i - 1])
                if diff < 0:
                    diff = 26 + diff
                complete.append(diff)
            seen[tuple(complete)].append(s)
        return list(seen.values())