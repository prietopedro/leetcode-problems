class Solution:
    def robotWithString(self, s: str) -> str:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        t = []
        output = []
        min_char = 'a'
        for c in s:
            t.append(c)
            counter[c] -= 1
            while min_char != "z" and counter[min_char] == 0:
                min_char = chr(ord(min_char) + 1)
            while t and t[-1] <= min_char:
                output.append(t.pop())
        return ''.join(output)