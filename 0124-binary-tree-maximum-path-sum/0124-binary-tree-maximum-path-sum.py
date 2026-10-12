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
        def maxPathHelper(node):
            nonlocal best
            if not node:
                return -inf
            maxL = maxPathHelper(node.left)
            maxR = maxPathHelper(node.right)
            curr = node.val
            best = max(
                best,
                maxL + maxR + curr,
                maxL,
                maxR,
                maxL + curr,
                maxR + curr,
                curr
            )
            return max(maxL,maxR,0) + curr
        
        maxPathHelper(root)
        return best