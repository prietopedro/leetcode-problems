class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        seen = defaultdict(int)
        output = 0
        for word in words:
            reversed_word = word[1] + word[0]
            if seen[reversed_word]:
                seen[reversed_word] -= 1
                output += 4
            else:
                seen[word] += 1
        return output + (any(val and word[0] == word[1] for word,val in seen.items()) * 2)

        