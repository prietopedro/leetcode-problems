class Solution:
    def clearStars(self, s: str) -> str:
        output = []
        smallest = []
        removed = 0
        for i,c in enumerate(s):
            if c == '*':
                _,i = heapq.heappop(smallest)
                output[-i] = None
            else:
                heapq.heappush(smallest,(c,-i))
            output.append(c)
        return ''.join(c for c in output if c != None and c != '*')