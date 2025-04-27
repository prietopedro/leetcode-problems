class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        output = []
        for s in strs:
            output.append(f'{len(s)}-{s}')
        return ''.join(output)

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        output = []
        while i < len(s):
            count = 0
            while s[i] != '-':
                count = (count * 10) + int(s[i])
                i += 1
            output += [s[i+1:i+1+count]]
            i = i+1+count
        return output

            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))