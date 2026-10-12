# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        # keep some minimum and maximum
        #at the beginning the min and max would be -inf and inf
        # check current node must fall between both ends
        # moving left -> update the max
        # moving right -> update the min
        if not root:
            return True
        s = [(root,-inf,inf)]
        while s:
            node,min_val,max_val = s.pop()
            if not (min_val < node.val < max_val):
                return False
            if node.left:
                s.append((node.left,min_val,node.val))
            if node.right:
                s.append((node.right,node.val,max_val))
        return True