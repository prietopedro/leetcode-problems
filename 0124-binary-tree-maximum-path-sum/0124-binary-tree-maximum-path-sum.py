# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        #get max path (with no division) from left and from right
        #update some global variable with max, being maxL + maxR + curr, (or maxL, or maxR), or maxL + curr, or maxR + curr
        #return max of maxL,maxR + curr
        best = -inf
        def dfs(node):
            nonlocal best
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            best = max(best, node.val + left + right)

            return node.val + max(left, right)
        
        dfs(root)
        return best