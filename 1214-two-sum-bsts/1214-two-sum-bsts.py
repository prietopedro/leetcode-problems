# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        stack = [(root1,root2)]
        while stack:
            node1,node2 = stack.pop()
            if not node1 or not node2:
                continue
            total = node1.val + node2.val
            if total == target:
                return True
            
            if total > target:
                stack.append((node1,node2.left))
                stack.append((node1.left, node2))
            else:
                stack.append((node1,node2.right))
                stack.append((node1.right, node2))
        return False