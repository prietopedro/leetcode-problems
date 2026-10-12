# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val,q_val,c_val = p.val, q.val,root.val
        max_val, min_val = max(p_val,q_val),min(p_val,q_val)
        if min_val <= c_val <= max_val:
            return root
        elif min_val > c_val:
            return self.lowestCommonAncestor(root.right,p,q)
        return self.lowestCommonAncestor(root.left,p,q)
        
        
