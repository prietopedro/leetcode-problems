class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        N = len(colors)

        adj = defaultdict(list)
        indegree = [0] * N
        for a, b in edges:
            adj[a].append(b)
            indegree[b] += 1
        
        # topo sort + cycle detection
        q = deque(x for x in range(N) if indegree[x] == 0)
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(topo) != N:
            return -1

        # dp on topo ordering for a given color
        @cache
        def dp(node, color):
            if not adj[node]:
                return int(colors[node] == color)
            
            best = 0
            match = int(colors[node] == color)
            for nei in adj[node]:
                best = max(best, match + dp(nei, color))
            return best

        # try every color
        best = 0
        for color in set(colors):
            for start in range(N):
                best = max(best, dp(start, color))
        return best