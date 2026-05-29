class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # track seen lowercase
        # track seen uppercase
        # if upper case and not seen lowercase -> NOT good
        # if lower case and in uppercase -> NOT good
        # need to track the bad ones to count at the end
        seen_lowercase = [False] * 26
        seen_uppercase = [False] * 26
        non_special = [False] * 26
        for c in word:
            cIndex = ord('a') - ord(c.lower())
            if non_special[cIndex]:
                continue
            if c.upper() == c and not seen_lowercase[cIndex]:
                non_special[cIndex] = True
            if c.lower() == c and seen_uppercase[cIndex]:
                non_special[cIndex] = True

            if c.upper() == c:
                seen_uppercase[cIndex] = True
            if c.lower() == c:
                seen_lowercase[cIndex] = True
                
        output = 0
        for i in range(26):
            output += seen_lowercase[i] and seen_uppercase[i] and not non_special[i]
        return output