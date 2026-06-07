# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
            nodes = {}
            for parent,child,isLeft in descriptions:
                if parent not in nodes:
                    nodes[parent] = TreeNode(parent)
                if child not in nodes:
                    nodes[child] = TreeNode(child)
                if isLeft: nodes[parent].left = nodes[child]
                else: nodes[parent].right = nodes[child]
            possible = set(nodes.keys())
            for key,value in nodes.items():
                if value.left and value.left.val in possible: possible.remove(value.left.val)
                if value.right and value.right.val in possible: possible.remove(value.right.val)

            return nodes[list(possible)[0]]
