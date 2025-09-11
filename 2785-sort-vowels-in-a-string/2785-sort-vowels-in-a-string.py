class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A','E','I','O','U','a','e','i','o','u']
        vowels_set = set(vowels)
        seen = defaultdict(int)
        s = list(s)
        indexes = []
        for i,c in enumerate(s):
            if c in vowels_set:
                seen[c] += 1
                indexes.append(i)
        last_index = 0
        for vowel in vowels:
            while seen[vowel]:
                s[indexes[last_index]] = vowel
                seen[vowel] -= 1
                last_index += 1
        return ''.join(s)

            
