# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not inorder:
            return None
        node = TreeNode(preorder[0])
        left = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:],inorder[:left])
        node.right = self.buildTree(preorder[1 + left:],inorder[left + 1:])
        return node