class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase = set()
        uppercase = set()
        count = 0
        for c in word:
            if c.lower() in lowercase and c.upper() in uppercase:
                continue
            if c.lower() == c:
                lowercase.add(c)
            else:
                uppercase.add(c)
            if c.lower() in lowercase and c.upper() in uppercase:
                count += 1
        return count