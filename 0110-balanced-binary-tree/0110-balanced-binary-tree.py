# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        balanced = True
        def dfs(node):
            if not node:
                return 0
            nonlocal balanced
            left = dfs(node.left)
            right = dfs(node.right)
            print(left,right)
            if abs(left - right) > 1:
                balanced = False
            return 1 + max(left, right)
        dfs(root)
        return balanced