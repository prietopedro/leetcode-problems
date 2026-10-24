class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        seen = {k: 0}
        q = [(0,k)]

        while q:
            time,node = heapq.heappop(q)
            if seen[node] > time:
                continue
            for nei,nei_time in graph[node]:
                if nei in seen and nei_time + time >= seen[nei]:
                    continue
                seen[nei] = nei_time + time
                heapq.heappush(q,(seen[nei],nei))

        return max(seen.values()) if len(seen) == n else -1

