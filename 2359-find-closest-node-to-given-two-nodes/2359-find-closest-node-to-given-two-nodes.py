class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        node1_visited = set()
        node2_visited = set()
        while node1 is not None or node2 is not None:
            best = inf
            node1_visited.add(node1)
            # if node1 is not None:
            if node1 in node2_visited: best = min(node1,best)
            if edges[node1] != -1 and edges[node1] not in node1_visited: node1 = edges[node1]
            else: node1 = None
            # if node2 is not None:
            node2_visited.add(node2)
            if node2 in node1_visited: best = min(node2,best)
            if node2 and edges[node2] != -1 and edges[node2] not in node2_visited: node2 = edges[node2]
            else: node2 = None

            if best != inf:
                return best
        return -1
                
