# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def rec(node):
            if not node:
                return (0,0)
            left, left_best = rec(node.left)
            right, right_best = rec(node.right)
            return (max(left,right) + 1, max(left_best, right_best, left + right))
        _,best = rec(root)
        return best
