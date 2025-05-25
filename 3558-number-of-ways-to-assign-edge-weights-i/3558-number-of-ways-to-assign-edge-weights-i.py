class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = (10 ** 9) + 7
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        seen = set()
        q = [1]
        level = -1
        while q:
            level += 1
            next_level = []
            for _ in range(len(q)):
                curr = q.pop()
                seen.add(curr)
                for nei in graph[curr]:
                    if nei not in seen:
                        next_level.append(nei)
            q = next_level
        
        return ((2 ** level) // 2) % MOD

       

            
                
                
            