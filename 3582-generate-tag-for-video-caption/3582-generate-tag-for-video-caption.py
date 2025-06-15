class Solution:
    def generateTag(self, caption: str) -> str:
        output = ['#']
        str_arr = caption.split()
        for word in str_arr:
            current = []
            for i,c in enumerate(word):
                num = ord(c.lower()) - ord('a')
                if num < 0 or num > 25:
                    continue
                if not current:
                    current.append(c.upper())
                else:
                    current.append(c.lower())
            output.append(''.join(current))
        if len(output) > 1:
            output[1] = output[1].lower()
            
        return ''.join(output)[:100]
                    
                