class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7 
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        seen = set()
        q = [1]
        level = -1
        levels = {}
        levels[0] = 0
        parent = {}
        while q:
            level += 1
            next_level = []
            for _ in range(len(q)):
                curr = q.pop()
                levels[curr] = level
                seen.add(curr)
                for nei in graph[curr]:
                    if nei not in seen:
                        parent[nei] = curr
                        next_level.append(nei)
            q = next_level

        output = []        
        for x,y in queries: 
            distance = 0
            while levels[x] > levels[y]:
                x = parent[x]
                distance += 1
            while levels[y] > levels[x]:
                y = parent[y]
                distance += 1
            while x != y:
                x = parent[x]
                y = parent[y]
                distance += 2

            output.append((2 ** (distance - 1)) % MOD if distance else 0)

        return output