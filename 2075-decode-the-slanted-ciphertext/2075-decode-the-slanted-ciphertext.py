class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        total_chars = 0
        for c in encodedText:
            total_chars += c != ' '
        movement = len(encodedText) // rows
        
        i = 0
        current = 0
        output = []
        while total_chars > 0:
            output.append(encodedText[current])
            if encodedText[current] != " ":
                total_chars -= 1
            if current + movement + 1 >= len(encodedText):
                i += 1
                current = i
            else:
                current += movement + 1
        return "".join(output)
