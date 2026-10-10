# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        def rec(node):
            if not node:
                return 0
            nonlocal best
            left = rec(node.left)
            right = rec(node.right)
            best = max(best, left + right)
            return max(left,right) + 1
        rec(root)
        return best
