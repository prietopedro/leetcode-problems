class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        node1_q = deque([node1])
        node2_q = deque([node2])
        node1_visited = set()
        node2_visited = set()
        while node1_q or node2_q:
            best = inf
            for _ in range(len(node1_q)):
                node = node1_q.popleft()
                node1_visited.add(node)
                if node in node2_visited:
                    best = min(node,best)
                if edges[node] != -1 and edges[node] not in node1_visited:
                    node1_q.append(edges[node])
            for _ in range(len(node2_q)):
                node = node2_q.popleft()
                node2_visited.add(node)
                if node in node1_visited:
                    best = min(node,best)
                if edges[node] != -1 and edges[node] not in node2_visited:
                    node2_q.append(edges[node])

            if best != inf:
                return best
        return -1
                
