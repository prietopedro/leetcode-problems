# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        q = deque([(root, 1)])
        max_depth = 1
        while q:
            node,level = q.popleft()
            max_depth = max(max_depth, level)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return max_depth