class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        for i in range(len(edges) - 1, -1, -1):
            x,y = edges[i]
            s = [(y,x)]
            visited = set([y])
            while s:
                curr,prev = s.pop()
                for nei in graph[curr]:
                    if nei == x and curr != y:
                        return edges[i]
                    if nei == prev:
                        continue
                    if nei in visited:
                        break
                    visited.add(nei)
                    s.append((nei,curr))
        return [-1,-1]