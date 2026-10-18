class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        q = deque([(0,None)])
        visited = set([0])
        while q:
            curr,prev = q.popleft()
            for nei in graph[curr]:
                if nei == prev:
                    continue
                if nei in visited:
                    return False
                visited.add(nei)
                q.append((nei,curr))
        return len(visited) == n