class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen = defaultdict(int)
        output = 0
        for x,y in dominoes:
            output += seen[(x,y)]
            output += seen[(y,x)] if x != y else 0
            seen[(x,y)]+=1
        return output