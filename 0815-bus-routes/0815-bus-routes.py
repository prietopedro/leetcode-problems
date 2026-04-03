

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
            
        connections = defaultdict(list)
        current = deque([])
        seen_routes = set()

        for i,r in enumerate(routes):
            for s in r:
                connections[s].append(i)
                if s == source:
                    current.append((i,1))
                    seen_routes.add(i)

        while current:
            r,stops = current.popleft()
            for s in routes[r]:
                if target == s:
                    return stops
                for next_route in connections[s]:
                    if next_route in seen_routes:
                        continue
                    seen_routes.add(next_route)
                    current.append((next_route,stops + 1))
        return -1
                    
                