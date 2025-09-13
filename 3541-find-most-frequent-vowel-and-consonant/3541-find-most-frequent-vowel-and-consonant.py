class Solution:
    def maxFreqSum(self, s: str) -> int:
        counter = Counter(s)
        max_vowel = 0
        max_consonant = 0
        for key,value in counter.items():
            if key in {'a','e','i','o','u'}:
                max_vowel = max(max_vowel,value)
            else:
                max_consonant = max(max_consonant,value)
        return max_vowel + max_consonant