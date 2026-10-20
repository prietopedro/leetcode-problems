


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        counter = 0
        
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)

            for nei in graph[node]:
                dfs(nei)
            return 1
        output = 0
        for i in range(n):
            output += dfs(i)
        return output
