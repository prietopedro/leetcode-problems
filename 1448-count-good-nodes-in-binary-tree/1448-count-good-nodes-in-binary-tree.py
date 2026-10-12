# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def countGood(node, max_val = -inf):
            if not node:
                return 0
            new_max = max(node.val,max_val)
            return int(node.val >= max_val) + countGood(node.left,new_max) + countGood(node.right,new_max)
        return countGood(root)