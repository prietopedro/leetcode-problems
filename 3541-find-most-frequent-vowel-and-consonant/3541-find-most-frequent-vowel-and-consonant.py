class Solution:
    def maxFreqSum(self, s: str) -> int:
        counter = Counter(s)
        vowels = 'aeiou'
        vowel_max,consonant_max = 0,0
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
            if c in vowels:
                vowel_max = max(vowel_max,counter[c])
            else:
                consonant_max = max(consonant_max,counter[c])
        return vowel_max + consonant_max
