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
        q = deque([(root, -inf)])
        output = 0
        while q:
            curr,max_val = q.popleft()
            output += curr.val >= max_val
            new_max = max(curr.val,max_val)
            if curr.left:
                q.append((curr.left,new_max))
            if curr.right:
                q.append((curr.right,new_max))
        return output
