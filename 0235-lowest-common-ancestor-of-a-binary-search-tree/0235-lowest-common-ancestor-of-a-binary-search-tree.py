# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        if p.val > q.val:
            p,q = q,p
        while curr:
            if p.val <= curr.val <= q.val:
                return curr
            elif q.val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        return None