# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        s = [(root, -inf)]
        output = 0
        while s:
            curr,max_val = s.pop()
            output += curr.val >= max_val
            new_max = max(curr.val,max_val)
            if curr.left:
                s.append((curr.left,new_max))
            if curr.right:
                s.append((curr.right,new_max))
        return output
