"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def helper(node):
            if not node: 
                return None
            if node.val in visited:
                return visited[node.val]

            new_node = Node(node.val)
            visited[node.val] = new_node
            for nei in node.neighbors:
                nei = helper(nei)
                if nei:
                    new_node.neighbors.append(nei)
            return new_node
        return helper(node)